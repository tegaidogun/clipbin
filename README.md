# 📋 PasteDump

A minimal, dark-themed, feature-rich pastebin clone built with **Flask** + **Tailwind CSS**.  
Designed for speed, code clarity, and a smooth UI/UX experience.

---

## ✨ Features

- 🔍 **Search pastes** by ID or title
- ✍️ **Create pastes** with optional titles and expiration
- 📟 **Line numbering** and preserved formatting
- 🌗 Dark-first responsive layout with mobile support
- 🔗 Copy **URL**, **raw view**, **download as `.txt` or `.json`**
- 📅 Auto-expiring pastes (5 mins, 1 hour, 1 day, or never)
- 🧠 Built with Flask + SQLite + Tailwind

---

## 🚀 Quickstart

### 1. Clone the repo

```bash
git clone https://github.com/tegaidogun/pastedump.git
cd pastedump
```

### 2. Create virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Tailwind CSS (via npm)

```bash
npm install
```

### 5. Build Tailwind CSS

```bash
npx tailwindcss -i ./static/styles/input.css -o ./static/styles/output.css --watch
```

For one-time production build:
```bash
npx tailwindcss -i ./static/styles/input.css -o ./static/styles/output.css --minify
```

### 6. Run the Flask app

```bash
flask run
```

## 🛆 Dependencies

- Python 3.9+
- Flask
- SQLite3
- Tailwind CSS (via Node.js)
- Jinja2

---

