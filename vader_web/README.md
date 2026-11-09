# VADER text analyzer

This Flask form applies VADER (Valence Aware Dictionary and sEntiment Reasoner), a rule-based sentiment analyzer. The app lowercases the input, removes digits and English stopwords, and displays VADER's positive, neutral, and negative scores.

The interface presents the compound score on a 0–100% scale. The displayed percentage represents rescaled polarity, with a neutral compound score centered at 50%. The historical interface labels it as “positive,” but that percentage is a score rather than a probability.

## Local setup

From the repository root, enter `vader_web/` and create and activate a dedicated virtual environment using the [setup instructions](../README.md#run-the-twitterx-demo). [The dependency manifest](requirements.txt) preserves the original pins, which may require an older Python environment. The app requests the NLTK stopwords corpus at startup.

```sh
cd vader_web
python -m pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5002` and submit text using the form.

## Historical interface

[Input form](../screenshots/vader-input-2025.png) · [Score table](../screenshots/vader-output-2025.png)
