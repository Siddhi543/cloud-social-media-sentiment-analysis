# Cloud-Based Social Media Sentiment Analysis

Three Flask applications explore how to score written sentiment with VADER and classify text with a trained machine-learning model. The original project ran on AWS EC2 in 2025. This repository includes the applications, serialized model artifacts, and screenshots from that deployment.

| Component | What it does |
| --- | --- |
| [Twitter/X sentiment viewer](twitter_sentiment_analysis/) | Filters synthetic posts by keyword in demo mode, or requests recent posts through the X API in live mode. VADER scores the text and assigns a positive, neutral, or negative label. |
| [VADER text analyzer](vader_web/) | Scores user-entered text and displays positive, neutral, negative, and scaled compound scores. |
| [ML sentiment classifier](ml_classifier/) | Preprocesses text, transforms it with a saved TF-IDF vectorizer, and predicts a label with the bundled classifier. |

## Run the Twitter/X demo

From the repository root, enter the viewer folder and create a virtual environment with Python 3.10 or later.

```sh
cd twitter_sentiment_analysis
python -m venv .venv
```

Activate it with `.\.venv\Scripts\Activate.ps1` in PowerShell or `source .venv/bin/activate` on macOS or Linux, then run:

```sh
python -m pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5001/tweets?keyword=cricket&mode=demo`. Demo mode uses built-in synthetic posts and requires no API credentials. To run the same demo from the command line:

```sh
python twitter_stream.py cricket --mode demo
```

The Twitter/X viewer code was rebuilt from historical screenshots. Live API functionality remains unverified. To try it with authorized access to the recent-search endpoint, set `X_BEARER_TOKEN` in the process environment before starting Flask and select **Live X API** in the viewer. Keep credentials out of version control. The [.env example](twitter_sentiment_analysis/.env.example) documents the variable name. The app reads the process environment directly.

## Run the text analyzers

- **VADER** — Follow the [VADER setup notes](vader_web/README.md) for the local form at `http://127.0.0.1:5002`.
- **ML classifier** — Enter `ml_classifier/` from the repository root and create a separate virtual environment using the setup above. Only load the bundled pickle files after verifying their source and trusting their contents, because loading a pickle can execute code.

Both ML artifacts record scikit-learn `1.0.2`. Use an environment that supports this version. The requirements file leaves scikit-learn unpinned, so specify the matching version when installing dependencies.

```sh
python -m pip install -r requirements.txt "scikit-learn==1.0.2" "numpy<2"
python -m nltk.downloader stopwords
python app.py
```

Open `http://127.0.0.1:5000`. See the [project notes](docs/PROJECT_NOTES.md) for artifact sources and validation status.

## Screenshots from April 2025

[Twitter/X viewer](screenshots/twitter-web-2025.png) · [Twitter/X terminal output](screenshots/twitter-terminal-2025.png) · [VADER input](screenshots/vader-input-2025.png) · [VADER results](screenshots/vader-output-2025.png) · [Gunicorn terminal](screenshots/gunicorn-terminal-2025.png)

The original applications ran on Ubuntu EC2 instances that have since been retired. See the [AWS deployment history](docs/AWS_DEPLOYMENT_HISTORY.md) for the historical commands and server context.
