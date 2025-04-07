from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Home route to serve the HTML interface
@app.route('/')
def home():
    return render_template('index.html')  # Make sure index.html is in a 'templates' folder

# Add Student
@app.route('/add_student', methods=['POST'])
def add_student():
    name = request.form.get('name')
    address = request.form.get('address')
    # TODO: Add logic to insert student into the database
    print(f"Received student: {name}, {address}")
    return jsonify({"status": "success", "message": "Student added."})

# Add Course
@app.route('/add_course', methods=['POST'])
def add_course():
    name = request.form.get('course_name')
    credits = request.form.get('credits')
    course_id = request.form.get('course_id')
    # TODO: Add logic to insert course into the database
    print(f"Received course: {name}, {credits}, {course_id}")
    return jsonify({"status": "success", "message": "Course added."})

# Add Section
@app.route('/add_section', methods=['POST'])
def add_section():
    semester = request.form.get('semester')
    # TODO: Add logic to insert section into the database
    print(f"Received section: {semester}")
    return jsonify({"status": "success", "message": "Section added."})

# List Students
@app.route('/list_students', methods=['GET'])
def list_students():
    # TODO: Fetch student records from the database
    return jsonify({"students": []})

# List Courses
@app.route('/list_courses', methods=['GET'])
def list_courses():
    # TODO: Fetch course records from the database
    return jsonify({"courses": []})

# List Sections
@app.route('/list_sections', methods=['GET'])
def list_sections():
    # TODO: Fetch section records from the database
    return jsonify({"sections": []})

if __name__ == '__main__':
    app.run(debug=True)
