import requests
import feedparser

def fetch_rss(feed_url: str = "https://feeds.npr.org/510289/podcast.xml", limit=5):
    response = requests.get(feed_url)
    response.raise_for_status()  # щоб бачити помилки якщо URL недоступний
    feed = feedparser.parse(response.content)
    episodes = []
    for entry in feed.entries[:limit]:
        episodes.append({
            "title": entry.title,
            "url": entry.link
        })
    return episodes
