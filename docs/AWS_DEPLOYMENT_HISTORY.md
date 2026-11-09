# AWS deployment history

In April 2025, the original Flask applications ran on Ubuntu instances in AWS EC2. The [Gunicorn screenshot](../screenshots/gunicorn-terminal-2025.png) shows an application listening on `0.0.0.0:5001`. The [Twitter/X terminal screenshot](../screenshots/twitter-terminal-2025.png) shows work in a separate `tweet_viewer` directory with `twitter_stream.py`, `app.py`, and `templates/tweets.html`.

The historical commands included:

```sh
gunicorn --bind 0.0.0.0:5001 app:app
python3 twitter_stream.py Cricket
```

The instances have since been retired, and the exact server configuration is unavailable. The [local viewer setup](../README.md#run-the-twitterx-demo) documents the current repository commands.

## Deployment guidance

For a new deployment, run Gunicorn under a dedicated non-root service account in a Python virtual environment, behind an HTTPS reverse proxy. Restrict inbound access with an EC2 security group and keep the Gunicorn port private. Supply secrets through environment variables and keep tokens, SSH private keys, and `.env` files out of version control.
