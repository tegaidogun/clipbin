from flask import Flask, render_template, request, redirect, url_for, abort
import sqlite3
import uuid
import os
from datetime import datetime, timedelta

app = Flask(__name__, instance_relative_config=True)
app.config['DATABASE'] = os.path.join(app.instance_path, 'clipbin.db')
SCHEMA_PATH = os.path.join(os.path.dirname(__file__), 'database', 'schema.sql')

# Ensure instance folder exists
os.makedirs(app.instance_path, exist_ok=True)

# Recreate database if needed
if not os.path.exists(app.config['DATABASE']):
    with sqlite3.connect(app.config['DATABASE']) as conn:
        with open(SCHEMA_PATH) as f:
            conn.executescript(f.read())

def get_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    db = get_db()
    pastes = db.execute('''
        SELECT id, title, created_at
        FROM pastes
        WHERE expires_in IS NULL
           OR datetime(created_at, '+' || expires_in || ' minutes') > CURRENT_TIMESTAMP
        ORDER BY created_at DESC
        LIMIT 10
    ''').fetchall()
    db.close()
    return render_template('index.html', pastes=pastes)

@app.route('/paste', methods=['POST'])
def create_paste():
    content = request.form['content']
    title = request.form.get('title') or "Untitled"
    expires_in = request.form.get('expires_in')
    paste_id = str(uuid.uuid4())[:8]

    if expires_in == "":
        expires_in = None
    else:
        try:
            expires_in = int(expires_in)
        except ValueError:
            expires_in = None

    db = get_db()
    db.execute('INSERT INTO pastes (id, title, content, expires_in) VALUES (?, ?, ?, ?)',
               (paste_id, title, content, expires_in))
    db.commit()
    db.close()

    return redirect(url_for('view_paste', paste_id=paste_id))

@app.route('/paste/<paste_id>')
def view_paste(paste_id):
    db = get_db()
    paste = db.execute('SELECT *, datetime(created_at, "+" || expires_in || " minutes") as expires_at FROM pastes WHERE id = ?', (paste_id,)).fetchone()
    db.close()

    if paste is None:
        abort(404)

    # Check expiration
    if paste['expires_in'] and datetime.utcnow() > datetime.strptime(paste['expires_at'], "%Y-%m-%d %H:%M:%S"):
        db = get_db()
        db.execute('DELETE FROM pastes WHERE id = ?', (paste_id,))
        db.commit()
        db.close()
        abort(404)

    return render_template('paste.html', paste=paste)

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)