import sqlite3

conn = sqlite3.connect("colleges.db")
cur = conn.cursor()

def get_course_id(course_name):
    cur.execute("SELECT id FROM courses WHERE course_name=?", (course_name,))
    row = cur.fetchone()
    return row[0] if row else None

# Insert KIIT college (no courses column here)
cur.execute("""
INSERT INTO colleges(name, state, city, fees, cutoff, entrance_exam, capacity)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", ("KIIT University", "Odisha", "Bhubaneswar", 180000, 85, "KIITEE", 8000))

college_id = cur.lastrowid

# Link KIIT with multiple courses
for course in ["BTech", "MCA", "PhD"]:
    cid = get_course_id(course)
    if cid:
        cur.execute("INSERT INTO college_courses VALUES (?, ?)", (college_id, cid))
    else:
        print("Course not found:", course)

conn.commit()
conn.close()

print("✅ KIIT added successfully with courses!")
