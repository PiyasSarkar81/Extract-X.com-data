import requests
import json
import os
import config  # Ensure config.py contains your BEARER_TOKEN

# Load Bearer Token from config.py
BEARER_TOKEN = config.bearer_token  

def create_headers():
    """Create headers for API request."""
    return {"Authorization": f"Bearer {BEARER_TOKEN}"}

def search_tweets(query, max_results=10):
    """Search recent tweets based on a query."""
    search_url = "https://api.twitter.com/2/tweets/search/recent"
    
    params = {
        "query": query,
        "tweet.fields": "created_at,author_id,text",
        "max_results": max_results
    }
    
    response = requests.get(search_url, headers=create_headers(), params=params)
    
    if response.status_code == 200:
        tweets = response.json()
        return tweets.get("data", [])  # Extract tweets list
    else:
        print(f"Error: {response.status_code}, {response.json()}")
        return []

def save_tweets_to_json(query, tweets):
    """Save extracted tweets to a JSON file in the data/ directory."""
    
    # Ensure the "data" directory exists
    if not os.path.exists("data"):
        os.makedirs("data")

    # Create a safe filename based on the query
    query_filename = query.replace(" ", "_")  # Replace spaces with underscores
    filename = f"data/stream_{query_filename}.json"

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(tweets, f, indent=4, ensure_ascii=False)
    
    print(f"✅ Tweets saved to {filename}")

if __name__ == "__main__":
    keyword = "Apple"  # Change this to your desired keyword
    tweets = search_tweets(keyword, max_results=10)

    if tweets:
        save_tweets_to_json(keyword, tweets)
    else:
        print("❌ No tweets found!")
