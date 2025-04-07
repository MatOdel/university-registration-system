from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

DB_PATH = 'school.db'

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # So we can return rows as dicts
    return conn

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Add Student
@app.route('/add_student', methods=['POST'])
def add_student():
    name = request.form.get('name')
    address = request.form.get('address')
    conn = get_db_connection()
    conn.execute("INSERT INTO students (name, address) VALUES (?, ?)", (name, address))
    conn.commit()
    conn.close()
    return jsonify({"status": "success", "message": "Student added."})

# Add Course
@app.route('/add_course', methods=['POST'])
def add_course():
    name = request.form.get('course_name')
    credits = request.form.get('credits')
    course_id = request.form.get('course_id')
    conn = get_db_connection()
    conn.execute("INSERT INTO courses (id, name, credits) VALUES (?, ?, ?)", (course_id, name, credits))
    conn.commit()
    conn.close()
    return jsonify({"status": "success", "message": "Course added."})

# Add Section
@app.route('/add_section', methods=['POST'])
def add_section():
    course_id = request.form.get('course_id')
    semester = request.form.get('semester')
    conn = get_db_connection()
    conn.execute("INSERT INTO sections (course_id, semester) VALUES (?, ?)", (course_id, semester))
    conn.commit()
    conn.close()
    return jsonify({"status": "success", "message": "Section added."})

# List Students
@app.route('/list_students', methods=['GET'])
def list_students():
    conn = get_db_connection()
    students = conn.execute("SELECT * FROM students").fetchall()
    conn.close()
    return jsonify([dict(row) for row in students])

# List Courses
@app.route('/list_courses', methods=['GET'])
def list_courses():
    rubric = request.args.get('rubric')  # Optional rubric filtering
    conn = get_db_connection()
    if rubric:
        query = "SELECT * FROM courses WHERE id LIKE ?"
        courses = conn.execute(query, (f"{rubric}%",)).fetchall()
    else:
        courses = conn.execute("SELECT * FROM courses").fetchall()
    conn.close()
    return jsonify([dict(row) for row in courses])

# List Sections
@app.route('/list_sections', methods=['GET'])
def list_sections():
    course_id = request.args.get('course_id')  # Optional filtering
    conn = get_db_connection()
    if course_id:
        query = "SELECT * FROM sections WHERE course_id = ?"
        sections = conn.execute(query, (course_id,)).fetchall()
    else:
        sections = conn.execute("SELECT * FROM sections").fetchall()
    conn.close()
    return jsonify([dict(row) for row in sections])

if __name__ == '__main__':
    app.run(debug=True)
