#!/usr/bin/env python3
# SILENT SIX Clear Studio — 미션 클리어 이미지 생성기 (맥용, 추가 설치 없음)
# 실행: python3 clear_studio.py  → 브라우저가 자동으로 열린다.
# 미션 정의는 같은 폴더의 missions.json. 화면에서 고치고 저장하면 이 파일이 바뀐다.
import base64, json, os, ssl, subprocess, sys, threading, time, traceback, urllib.request, urllib.error, uuid, webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HERE = os.path.dirname(os.path.abspath(__file__))
PORT = int(os.environ.get("S6_PORT", "8766"))
API = os.environ.get("S6_API_BASE", "https://api.openai.com/v1")
OUT = os.path.expanduser(os.environ.get("S6_OUT", "~/Desktop/SILENT6_output/clear"))
PUBLIC = os.path.normpath(os.path.join(HERE, "..", "..", "public"))   # 저장소 안에서 실행하면 요원 참조 이미지를 여기서 읽는다
MISSIONS = os.path.join(HERE, "missions.json")
JOBS = {}

def opener(req, timeout):
    try:
        return urllib.request.urlopen(req, timeout=timeout)
    except urllib.error.URLError as e:
        if "CERTIFICATE_VERIFY_FAILED" in str(e) and os.path.exists("/etc/ssl/cert.pem"):
            return urllib.request.urlopen(req, timeout=timeout, context=ssl.create_default_context(cafile="/etc/ssl/cert.pem"))
        raise

def multipart(fields, files):
    b = "----s6" + uuid.uuid4().hex
    out = []
    for k, v in fields.items():
        out.append(("--%s\r\nContent-Disposition: form-data; name=\"%s\"\r\n\r\n%s\r\n" % (b, k, v)).encode())
    for name, fn, mime, data in files:
        out.append(("--%s\r\nContent-Disposition: form-data; name=\"%s\"; filename=\"%s\"\r\nContent-Type: %s\r\n\r\n" % (b, name, fn, mime)).encode())
        out.append(data); out.append(b"\r\n")
    out.append(("--%s--\r\n" % b).encode())
    return b"".join(out), "multipart/form-data; boundary=" + b

def safe_name(s):
    return "".join(c for c in s if c.isalnum() or c in "-_")[:60] or "image"

def to_jpg(png, jpg):
    # 게임에 올릴 크기(768x1152)의 JPG로 바꾼다. 맥에 기본으로 들어 있는 sips를 쓴다.
    try:
        r = subprocess.run(["sips", "-s", "format", "jpeg", "-s", "formatOptions", "88", "-z", "1152", "768", png, "--out", jpg], capture_output=True, timeout=60)
        return r.returncode == 0 and os.path.isfile(jpg)
    except Exception:
        return False

def generate(req):
    fields = {"model": req["model"], "prompt": req["prompt"], "size": req.get("size", "1024x1536"), "n": "1"}
    if req.get("quality"): fields["quality"] = req["quality"]
    files = []
    for i, r in enumerate(req.get("refs", [])):
        head, b64 = r.split(",", 1)
        mime = head.split(";")[0].replace("data:", "") or "image/png"
        ext = {"image/jpeg": "jpg", "image/webp": "webp"}.get(mime, "png")
        files.append(("image[]", "ref%d.%s" % (i, ext), mime, base64.b64decode(b64)))
    if files:
        body, ctype = multipart(fields, files); url = API + "/images/edits"
    else:
        body = json.dumps({k: (1 if k == "n" else v) for k, v in fields.items()}).encode(); ctype = "application/json"; url = API + "/images/generations"
    rq = urllib.request.Request(url, data=body, method="POST", headers={"Authorization": "Bearer " + req["key"], "Content-Type": ctype})
    try:
        with opener(rq, 900) as rs: data = json.loads(rs.read())
    except urllib.error.HTTPError as e:
        txt = e.read().decode("utf8", "replace")
        try: msg = json.loads(txt)["error"]["message"]
        except Exception: msg = txt[:400]
        return {"ok": False, "error": "HTTP %d: %s" % (e.code, msg)}
    except Exception as e:
        return {"ok": False, "error": str(e)}
    if not data.get("data"): return {"ok": False, "error": "응답에 이미지가 없다: " + json.dumps(data)[:300]}
    d = data["data"][0]
    if d.get("b64_json"): img = base64.b64decode(d["b64_json"])
    else:
        with opener(d["url"], 300) as rs: img = rs.read()
    os.makedirs(os.path.join(OUT, "png"), exist_ok=True)
    name = safe_name(req["name"])
    png = os.path.join(OUT, "png", name + ".png"); jpg = os.path.join(OUT, name + ".jpg")
    with open(png, "wb") as f: f.write(img)
    ok = to_jpg(png, jpg)
    return {"ok": True, "path": jpg if ok else png, "jpg": ok, "file": ("/out/%s.jpg" % name if ok else "/out/png/%s.png" % name) + "?t=%d" % time.time()}

def run_job(jid, req):
    try: JOBS[jid] = generate(req)
    except Exception as e:
        traceback.print_exc(); JOBS[jid] = {"ok": False, "error": "%s: %s" % (type(e).__name__, e)}

class H(BaseHTTPRequestHandler):
    def log_message(self, *a): pass
    def send(self, code, body, ctype="application/json"):
        if isinstance(body, (dict, list)): body = json.dumps(body, ensure_ascii=False).encode()
        self.send_response(code); self.send_header("Content-Type", ctype); self.send_header("Content-Length", str(len(body))); self.send_header("Cache-Control", "no-store"); self.end_headers(); self.wfile.write(body)
    def file(self, fp, ctype):
        with open(fp, "rb") as f: self.send(200, f.read(), ctype)
    def do_GET(self):
        p = self.path.split("?")[0]
        if p == "/": self.file(os.path.join(HERE, "clear.html"), "text/html; charset=utf-8")
        elif p == "/api/missions": self.file(MISSIONS, "application/json; charset=utf-8")
        elif p.startswith("/ref/"):
            fp = os.path.join(PUBLIC, "a_%s_0.jpg" % safe_name(p[5:]))
            if os.path.isfile(fp): self.file(fp, "image/jpeg")
            else: self.send(404, {"ok": False})
        elif p.startswith("/out/"):
            fp = os.path.normpath(os.path.join(OUT, p[5:]))
            if fp.startswith(os.path.normpath(OUT)) and os.path.isfile(fp): self.file(fp, "image/png" if fp.endswith(".png") else "image/jpeg")
            else: self.send(404, {"ok": False})
        elif p == "/api/job":
            jid = self.path.split("id=")[-1]
            if jid not in JOBS: self.send(200, {"done": True, "ok": False, "error": "작업을 찾을 수 없다. 프로그램을 다시 켠 뒤 다시 뽑아 주세요."})
            elif JOBS[jid] is None: self.send(200, {"done": False})
            else: r = dict(JOBS.pop(jid)); r["done"] = True; self.send(200, r)
        elif p == "/api/list":
            fs = sorted(f for f in os.listdir(OUT) if f.endswith(".jpg")) if os.path.isdir(OUT) else []
            self.send(200, {"out": OUT, "files": fs, "repo": os.path.isdir(PUBLIC)})
        else: self.send(404, {"ok": False})
    def do_POST(self):
        n = int(self.headers.get("Content-Length", "0")); req = json.loads(self.rfile.read(n) or b"{}")
        if self.path == "/api/gen":
            jid = uuid.uuid4().hex; JOBS[jid] = None
            threading.Thread(target=run_job, args=(jid, req), daemon=True).start()
            self.send(200, {"ok": True, "job": jid})
        elif self.path == "/api/missions":
            if not isinstance(req.get("missions"), list): self.send(400, {"ok": False, "error": "missions 목록이 없다"}); return
            if os.path.isfile(MISSIONS):
                try: os.replace(MISSIONS, MISSIONS + ".bak")
                except Exception: pass
            with open(MISSIONS, "w", encoding="utf8") as f: json.dump(req, f, ensure_ascii=False, indent=1)
            self.send(200, {"ok": True})
        elif self.path == "/api/open":
            os.makedirs(OUT, exist_ok=True)
            if sys.platform == "darwin": subprocess.Popen(["open", OUT])
            self.send(200, {"ok": True, "out": OUT})
        else: self.send(404, {"ok": False})

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    srv = ThreadingHTTPServer(("127.0.0.1", PORT), H)
    url = "http://127.0.0.1:%d/" % PORT
    print("SILENT SIX Clear Studio 실행 중:", url, "\n저장 폴더:", OUT, "\n끝내려면 이 창에서 Ctrl+C")
    if not os.environ.get("S6_NOOPEN"): threading.Timer(0.6, lambda: webbrowser.open(url)).start()
    try: srv.serve_forever()
    except KeyboardInterrupt: pass
