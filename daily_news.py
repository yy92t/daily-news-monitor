import os
import requests
import json

API_KEY = os.getenv("NEWS_API_KEY")

if not API_KEY:
    raise ValueError("NEWS_API_KEY is not set")

response = requests.get(
    "https://newsapi.org/v2/top-headlines",
    params={
        "country": "hk",
        "apiKey": API_KEY
    }
)

data = response.json()

print(json.dumps(data, indent=2))

if "articles" not in data:
    print("API error:", data)
    exit(1)

for article in data["articles"][:10]:
    print(article.get("title", "No title"))
