#!/usr/bin/env python3
import os, yaml, feedparser, pandas as pd
from dateutil import parser as dateparser
from src.normalizer import normalize_records
from src.geocoder import geocode_records
from src.map_builder import build_map

BASE = os.path.dirname(os.path.abspath(__file__))
CFG = os.path.join(BASE, "config")
OUT = os.path.join(BASE, "output")

def load_yaml(p): 
    with open(p,"r",encoding="utf-8") as f: 
        return yaml.safe_load(f)

def fetch(feeds):
    items = []
    for f in feeds.get("feeds", []):
        d = feedparser.parse(f["url"])
        for e in getattr(d,"entries",[]):
            items.append({
                "title": e.get("title",""),
                "link": e.get("link",""),
                "published": e.get("published", e.get("updated","")),
                "summary": e.get("summary",""),
                "source": f.get("name","")
            })
    return items

def main():
    os.makedirs(OUT, exist_ok=True)
    feeds = load_yaml(os.path.join(CFG,"feeds_rss.yaml"))
    kw = load_yaml(os.path.join(CFG,"keywords.yaml"))
    items = fetch(feeds)
    if not items:
        items = pd.read_csv(os.path.join(CFG,"seed_data.csv")).to_dict(orient="records")
    df = normalize_records(items, kw)
    df = geocode_records(df)
    df.to_csv(os.path.join(OUT,"proyectos.csv"), index=False)
    build_map(df, os.path.join(OUT,"mapa_proyectos.html"))

if __name__ == "__main__":
    main()
