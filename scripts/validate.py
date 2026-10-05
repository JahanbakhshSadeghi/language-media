#!/usr/bin/env python3
import json,socket,sys,urllib.error,urllib.request,subprocess,shutil
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; DATA=ROOT/"data"
def load(n,k): return json.loads((DATA/n).read_text(encoding="utf-8")).get(k,[])
def check(x):
    try:
        req=urllib.request.Request(x["url"],headers={"User-Agent":"language-media-validator/1.0"})
        with urllib.request.urlopen(req,timeout=15) as r:
            content_type=r.headers.get("Content-Type","")
        ffprobe=shutil.which("ffprobe")
        if not ffprobe:
            return True,f"HTTP OK {content_type}; ffprobe unavailable"
        p=subprocess.run([ffprobe,"-v","error","-select_streams","v:0","-show_entries","stream=width,height","-of","csv=p=0",x["url"]],capture_output=True,text=True,timeout=25)
        if p.returncode!=0: return False,f"ffprobe failed: {p.stderr.strip()[:180]}"
        vals=p.stdout.strip().split(",")
        if len(vals)!=2: return False,"ffprobe returned no video dimensions"
        w,h=map(int,vals)
        minimum=int(x.get("min_height",720))
        return (h>=minimum,f"HTTP OK {content_type}; video {w}x{h}")
    except urllib.error.HTTPError as e: return False,f"HTTP {e.code}"
    except (urllib.error.URLError,socket.timeout,TimeoutError,subprocess.TimeoutExpired) as e: return False,str(getattr(e,"reason",e))
    except Exception as e: return False,str(e)
items=load("channels.json","channels")+load("radios.json","radios")
failed=0
for x in items:
    ok,msg=check(x); print(f"[{'OK' if ok else 'FAIL'}] {x['name']} — {msg}")
    failed += not ok
print(f"Checked: {len(items)} | Failed: {failed}")
sys.exit(1 if failed else 0)
