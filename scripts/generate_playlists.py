#!/usr/bin/env python3
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"data"; OUT=ROOT/"playlists"

def load(name,key):
    return json.loads((DATA/name).read_text(encoding="utf-8")).get(key,[])

def esc(v):
    return str(v or "").replace("&","&amp;").replace("\n"," ").strip()

def slug(value):
    return re.sub(r"[^a-z0-9]+", "_", value.lower()).strip("_")

def write(name,items):
    OUT.mkdir(parents=True,exist_ok=True)
    lines=["#EXTM3U"]
    for x in items:
        attrs=f'tvg-id="{esc(x.get("id"))}" tvg-name="{esc(x["name"])}" tvg-logo="{esc(x.get("logo"))}" group-title="{esc(x.get("group",x.get("language","Other")))}"'
        lines += [f'#EXTINF:-1 {attrs},{esc(x["name"])}',x["url"].strip()]
    (OUT/name).write_text("\n".join(lines)+"\n",encoding="utf-8")

tv=load("channels.json","channels")
radio=load("radios.json","radios")
write("all-tv.m3u",tv)
write("all-radio.m3u",radio)
for lang in sorted({x.get("language") for x in tv+radio if x.get("language")}):
    write(f"{slug(lang)}.m3u",[x for x in tv+radio if x.get("language")==lang])
print(f"Generated playlists: {len(tv)} TV, {len(radio)} radio.")
