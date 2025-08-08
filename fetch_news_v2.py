import feedparser
import json
from datetime import datetime

# List of working RSS feeds
rss_feeds = [
    "https://techcrunch.com/tag/startups/feed/",
    "https://techcrunch.com/tag/venture-capital/feed/",
    "https://feeds.feedburner.com/venturebeat/SZYF",
    "https://rss.app/feeds/1rTj4yLtvB4BzmIe.xml",  # StrictlyVC feed
]

# How many articles to fetch per feed
max_articles = 10

# Article storage
articles = []

print("Fetching articles...\n")

for feed_url in rss_feeds:
    feed = feedparser.parse(feed_url)
    print(f"Checking feed: {feed_url}")
    
    for entry in feed.entries[:max_articles]:
        article = {
            "title": entry.title,
            "link": entry.link,
            "published": entry.get("published", "N/A"),
            "summary": entry.get("summary", ""),
            "source": feed.feed.get("title", "Unknown Source")
        }
        articles.append(article)

print(f"\nFound {len(articles)} articles:\n")

for article in articles:
    print(f"- {article['title']} ({article['link']})")

# Save to versioned JSON file
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"articles_v2_{timestamp}.json"
with open(filename, "w", encoding='utf-8') as f:
    json.dump(articles, f, indent=2, ensure_ascii=False)

print(f"\nArticles saved to {filename}")
