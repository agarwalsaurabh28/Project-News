import os
import requests
import json

# 1. Grab your secret API key from GitHub's vault
api_key = os.environ.get("NEWS_API_KEY")

# 2. Tell the News API we want English business headlines
url = f"https://newsapi.org/v2/top-headlines?category=business&language=en&apiKey={api_key}"

print("Fetching news data...")
response = requests.get(url)
data = response.json()

# 3. Take just the articles list and save it to a file named 'today_news.json'
if "articles" in data:
    articles = data["articles"]
    with open("today_news.json", "w") as f:
        json.dump(articles, f, indent=4)
    print("Success! Saved today_news.json")
else:
    print("Error fetching news. Check your API key.")