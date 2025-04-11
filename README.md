# Clipbin

A minimal Pastebin clone built with Flask.

## Features
- Create and share text/code pastes
- View pastes by URL
- Syntax highlighting with highlight.js
- HTML escaping for safe rendering
- Expiration support for pastes

## Run locally

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Initialize DB
mkdir -p instance
sqlite3 instance/pastedump.db < database/schema.sql

# Run the app
python app.py
```

## Deployment
Easily deploy to Render, Fly.io, or Replit.

## License
MIT