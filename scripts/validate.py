#!/usr/bin/env python3
import json,socket,sys,urllib.error,urllib.request
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; DATA=ROOT/"data"
def load(n,k): return json.loads((DATA/n).read_text(encoding="utf-8")).get(k,[])
def check(x):
    try:
        req=urllib.request.Request(x["url"],headers={"User-Agent":"language-media-validator/1.0"})
        with urllib.request.urlopen(req,timeout=12) as r: return True,f"{r.status} {r.headers.get('Content-Type','')}"
    except urllib.error.HTTPError as e: return False,f"HTTP {e.code}"
    except (urllib.error.URLError,socket.timeout,TimeoutError) as e: return False,str(getattr(e,"reason",e))
    except Exception as e: return False,str(e)
items=load("channels.json","channels")+load("radios.json","radios")
failed=0
for x in items:
    ok,msg=check(x); print(f"[{'OK' if ok else 'FAIL'}] {x['name']} — {msg}")
    failed += not ok
print(f"Checked: {len(items)} | Failed: {failed}")
sys.exit(1 if failed else 0)
