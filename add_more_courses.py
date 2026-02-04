import sqlite3

conn = sqlite3.connect("colleges.db")
cur = conn.cursor()

def get_course_id(course_name):
    cur.execute("SELECT id FROM courses WHERE course_name=?", (course_name,))
    row = cur.fetchone()
    return row[0] if row else None

# Add some new colleges
colleges = [
    ("KIIT University", "Odisha", "Bhubaneswar", 180000, 85, "KIITEE", 8000, ["BTech", "MCA", "PhD"]),
    ("Bangalore Tech University", "Karnataka", "Bangalore", 150000, 80, "KCET", 3000, ["BTech", "MBA"]),
    ("Delhi Computer College", "Delhi", "New Delhi", 90000, 70, "CUET", 1200, ["BCA", "MCA"]),
]

for name, state, city, fees, cutoff, exam, capacity, course_list in colleges:

    # Insert college
    cur.execute("""
    INSERT INTO colleges(name, state, city, fees, cutoff, entrance_exam, capacity)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (name, state, city, fees, cutoff, exam, capacity))

    college_id = cur.lastrowid

    # Link courses
    for course in course_list:
        cid = get_course_id(course)
        if cid:
            cur.execute("INSERT INTO college_courses VALUES (?, ?)", (college_id, cid))
        else:
            print(f"⚠ Course not found in courses table: {course}")

conn.commit()
conn.close()

print("✅ Colleges with multiple courses added successfully!")
