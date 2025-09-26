# Quick tester to check connectivity to Google News RSS
import feedparser

URLS = [
 "https://news.google.com/rss/search?q=hydrogen+Netherlands+when:12m&hl=en&gl=NL&ceid=NL:en",
 "https://news.google.com/rss/search?q=hidrógeno+España+when:12m&hl=es-419&gl=ES&ceid=ES:es",
 "https://news.google.com/rss/search?q=hidrogénio+Portugal+when:12m&hl=pt-PT&gl=PT&ceid=PT:pt"
]

for u in URLS:
    d = feedparser.parse(u)
    print(u, " -> entries:", len(getattr(d, "entries", [])))
    if getattr(d, "entries", []):
        print("  1st:", d.entries[0].get("title"))
