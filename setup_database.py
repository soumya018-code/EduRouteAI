import sqlite3

conn = sqlite3.connect("colleges.db")
cur = conn.cursor()

# Colleges table
cur.execute("""
CREATE TABLE IF NOT EXISTS colleges (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    state TEXT,
    city TEXT,
    entrance_exam TEXT
)
""")

# Courses table
cur.execute("""
CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT UNIQUE
)
""")

# College-Course relation table
cur.execute("""
CREATE TABLE IF NOT EXISTS college_courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    college_id INTEGER,
    course_id INTEGER,
    fees INTEGER,
    capacity INTEGER,
    FOREIGN KEY(college_id) REFERENCES colleges(id),
    FOREIGN KEY(course_id) REFERENCES courses(id)
)
""")

conn.commit()
conn.close()

print("Database created successfully")