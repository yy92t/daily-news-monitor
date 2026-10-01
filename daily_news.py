import os
import requests
import json

API_KEY = os.getenv("NEWS_API_KEY")

print("API Key exists:", API_KEY is not None)

url = "https://newsapi.org/v2/top-headlines"

response = requests.get(
    url,
    params={
        "country": "hk",
        "apiKey": API_KEY
    }
)

data = response.json()

print("API Response:")
print(json.dumps(data, indent=2))

if "articles" not in data:
    print("ERROR: 'articles' field not found")
    exit(1)

for article in data["articles"][:10\]:
    print(article.get("title", "No title"))
