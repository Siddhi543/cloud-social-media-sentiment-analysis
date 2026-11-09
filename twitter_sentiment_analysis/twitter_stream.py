"""Score synthetic examples or recent Twitter/X posts with VADER.
Demo mode uses synthetic examples. Live mode requires authorized X API access.
"""
import argparse
import os
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

DEMO_TWEETS = [
    "Cricket match was thrilling, what a brilliant finish!",
    "Disappointing performance today, very frustrating.",
    "The cricket match starts at 7 PM today.",
    "Fantastic teamwork and a great result!",
    "The update is available now.",
]

def classify(text):
    score = SentimentIntensityAnalyzer().polarity_scores(text)["compound"]
    label = "Positive" if score >= 0.05 else "Negative" if score <= -0.05 else "Neutral"
    return {"text": text, "score": round(score, 4), "sentiment": label}

def get_tweets(keyword, mode="demo", limit=10):
    if not keyword or not keyword.strip():
        raise ValueError("Please enter a keyword")
    if mode == "demo":
        # These are explicitly synthetic sample texts, NOT actual tweets.
        return [classify(t) for t in DEMO_TWEETS if keyword.lower() in t.lower()][:limit]
    if mode != "live":
        raise ValueError("Mode must be demo or live")
    token = os.getenv("X_BEARER_TOKEN")
    if not token:
        raise RuntimeError("X_BEARER_TOKEN is not configured")
    import tweepy
    client = tweepy.Client(bearer_token=token, wait_on_rate_limit=False)
    response = client.search_recent_tweets(query=f"{keyword} -is:retweet", max_results=max(10,min(limit,100)), tweet_fields=["created_at"])
    return [classify(tweet.text) for tweet in (response.data or [])][:limit]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("keyword")
    parser.add_argument("--mode", choices=["demo", "live"], default="demo")
    args = parser.parse_args()
    for item in get_tweets(args.keyword, args.mode):
        print(f"Tweet: {item['text']}\nSentiment Score: {item['score']} -> {item['sentiment']}\n")
