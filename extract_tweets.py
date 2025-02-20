# make a pyhton environment and make a config.py file and store your BEARER_TOKEN

# run: pip install requests
# run: python extract_tweets.py

# you will see the extracted tweets in your terminal.
# if tweets is not found or you requested more than 
# your rate limit in x.com you will get output like:
# "❌ No tweets found!"

import requests
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

if __name__ == "__main__":
    keyword = "apple"  # Change this to your desired keyword
    tweets = search_tweets(keyword, max_results=10)

    if tweets:
        print("🔹 Extracted Tweets:")
        for tweet in tweets:
            print(f"{tweet['created_at']} - {tweet['text']}")
    else:
        print("❌ No tweets found!")
