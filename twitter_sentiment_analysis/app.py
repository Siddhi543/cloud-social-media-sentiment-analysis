"""Flask viewer for keyword-based Twitter/X sentiment analysis."""
import os
from flask import Flask, render_template, request
from twitter_stream import get_tweets
app = Flask(__name__)

@app.route("/")
@app.route("/tweets")
def tweets():
    keyword = request.args.get("keyword", "cricket").strip()
    mode = request.args.get("mode", "demo")
    results, error = [], None
    try:
        results = get_tweets(keyword, mode)
    except Exception as exc:
        error = str(exc)
    return render_template("tweets.html", keyword=keyword, mode=mode, results=results, error=error)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int(os.getenv("PORT", "5001")), debug=False)
