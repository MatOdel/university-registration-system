from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

# Ensure database folder and file exist
DB_PATH = 'database/university.db'
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                address TEXT NOT NULL
            );
        ''')
        conn.commit()

# Homepage
@app.route('/')
def index():
    return render_template('base.html')

# Add Student Page
@app.route('/add-student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO students (name, address) VALUES (?, ?)', (name, address))
            conn.commit()
        return redirect(url_for('index'))
    return render_template('add_student.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
