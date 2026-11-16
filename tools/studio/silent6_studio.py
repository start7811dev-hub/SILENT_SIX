#!/usr/bin/env python3
# SILENT SIX Studio — 요원 풀세트 생성기 (맥용, 추가 설치 없음)
# 실행: python3 silent6_studio.py  → 브라우저가 자동으로 열린다.
import base64, json, os, subprocess, sys, threading, time, urllib.request, urllib.error, uuid, webbrowser, zipfile
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

PORT = int(os.environ.get("S6_PORT", "8765"))
API = os.environ.get("S6_API_BASE", "https://api.openai.com/v1")
OUT = os.path.expanduser(os.environ.get("S6_OUT", "~/Desktop/SILENT6_output"))

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

def generate(req):
    fields = {"model": req["model"], "prompt": req["prompt"], "size": req["size"], "n": "1"}
    if req.get("quality"): fields["quality"] = req["quality"]
    if req.get("background"): fields["background"] = req["background"]
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
        with urllib.request.urlopen(rq, timeout=600) as rs: data = json.loads(rs.read())
    except urllib.error.HTTPError as e:
        txt = e.read().decode("utf8", "replace")
        try: msg = json.loads(txt)["error"]["message"]
        except Exception: msg = txt[:400]
        return {"ok": False, "error": "HTTP %d: %s" % (e.code, msg)}
    except Exception as e:
        return {"ok": False, "error": str(e)}
    d = data["data"][0]
    if d.get("b64_json"): img = base64.b64decode(d["b64_json"])
    else:
        with urllib.request.urlopen(d["url"], timeout=300) as rs: img = rs.read()
    folder = os.path.join(OUT, req["char"]); os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, req["name"] + ".png")
    with open(path, "wb") as f: f.write(img)
    return {"ok": True, "path": path, "file": "/out/%s/%s.png?t=%d" % (req["char"], req["name"], time.time())}

class H(BaseHTTPRequestHandler):
    def log_message(self, *a): pass
    def send(self, code, body, ctype="application/json"):
        if isinstance(body, (dict, list)): body = json.dumps(body).encode()
        self.send_response(code); self.send_header("Content-Type", ctype); self.send_header("Content-Length", str(len(body))); self.send_header("Cache-Control", "no-store"); self.end_headers(); self.wfile.write(body)
    def do_GET(self):
        p = self.path.split("?")[0]
        if p == "/":
            here = os.path.dirname(os.path.abspath(__file__))
            with open(os.path.join(here, "studio.html"), "rb") as f: self.send(200, f.read(), "text/html; charset=utf-8")
        elif p.startswith("/out/"):
            fp = os.path.normpath(os.path.join(OUT, p[5:]))
            if fp.startswith(os.path.normpath(OUT)) and os.path.isfile(fp):
                with open(fp, "rb") as f: self.send(200, f.read(), "image/png")
            else: self.send(404, {"ok": False})
        elif p == "/api/list":
            res = {}
            if os.path.isdir(OUT):
                for c in sorted(os.listdir(OUT)):
                    d = os.path.join(OUT, c)
                    if os.path.isdir(d): res[c] = sorted(f[:-4] for f in os.listdir(d) if f.endswith(".png"))
            self.send(200, {"out": OUT, "files": res})
        else: self.send(404, {"ok": False})
    def do_POST(self):
        n = int(self.headers.get("Content-Length", "0")); req = json.loads(self.rfile.read(n) or b"{}")
        if self.path == "/api/gen": self.send(200, generate(req))
        elif self.path == "/api/open":
            os.makedirs(OUT, exist_ok=True)
            if sys.platform == "darwin": subprocess.Popen(["open", OUT])
            self.send(200, {"ok": True, "out": OUT})
        elif self.path == "/api/zip":
            c = req.get("char", ""); src = os.path.join(OUT, c) if c else OUT
            zp = os.path.join(OUT, (c or "all") + "_fullset.zip")
            with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED) as z:
                for root, _, fs in os.walk(src):
                    for f in fs:
                        if f.endswith(".png"): fp = os.path.join(root, f); z.write(fp, os.path.relpath(fp, OUT))
            if sys.platform == "darwin": subprocess.Popen(["open", "-R", zp])
            self.send(200, {"ok": True, "path": zp})
        else: self.send(404, {"ok": False})

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    srv = ThreadingHTTPServer(("127.0.0.1", PORT), H)
    url = "http://127.0.0.1:%d/" % PORT
    print("SILENT SIX Studio 실행 중:", url, "\n저장 폴더:", OUT, "\n끝내려면 이 창에서 Ctrl+C")
    if not os.environ.get("S6_NOOPEN"): threading.Timer(0.6, lambda: webbrowser.open(url)).start()
    try: srv.serve_forever()
    except KeyboardInterrupt: pass
