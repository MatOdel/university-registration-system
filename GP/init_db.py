import sqlite3

# Connect to (or create) the database
conn = sqlite3.connect('school.db')
c = conn.cursor()

# Create Students table
c.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        address TEXT NOT NULL
    )
''')

# Create Courses table
c.execute('''
    CREATE TABLE IF NOT EXISTS courses (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        credits INTEGER NOT NULL
    )
''')

# Create Sections table
c.execute('''
    CREATE TABLE IF NOT EXISTS sections (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_id TEXT NOT NULL,
        semester TEXT NOT NULL,
        FOREIGN KEY(course_id) REFERENCES courses(id)
    )
''')

# Save changes and close
conn.commit()
conn.close()

print("Database and tables created successfully.")
