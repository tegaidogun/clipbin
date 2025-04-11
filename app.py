from flask import Flask, render_template, request, redirect, url_for, abort
import sqlite3
import uuid
import os

app = Flask(__name__, instance_relative_config=True)
app.config['DATABASE'] = os.path.join(app.instance_path, 'clipbin.db')

# Ensure instance folder exists
os.makedirs(app.instance_path, exist_ok=True)

def get_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/paste', methods=['POST'])
def create_paste():
    content = request.form['content']
    title = request.form.get('title') or "Untitled"
    paste_id = str(uuid.uuid4())[:8]
    
    db = get_db()
    db.execute('INSERT INTO pastes (id, title, content) VALUES (?, ?, ?)',
               (paste_id, title, content))
    db.commit()
    db.close()

    return redirect(url_for('view_paste', paste_id=paste_id))

@app.route('/paste/<paste_id>')
def view_paste(paste_id):
    db = get_db()
    paste = db.execute('SELECT * FROM pastes WHERE id = ?', (paste_id,)).fetchone()
    db.close()
    if paste is None:
        abort(404)
    return render_template('paste.html', paste=paste)

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)