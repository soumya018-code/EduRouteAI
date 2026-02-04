import sqlite3

conn = sqlite3.connect("colleges.db")
cur = conn.cursor()

# Example college: KIIT
cur.execute("""
INSERT INTO colleges(name,state,city,fees,cutoff,entrance_exam,capacity)
VALUES (?,?,?,?,?,?,?)
""", ("KIIT University", "Odisha", "Bhubaneswar", 180000, 85, "KIITEE", 8000))

college_id = cur.lastrowid

# Courses KIIT offers
courses = ["BTech", "MCA", "MTech", "PhD" ,  ]

for course in courses:
    cur.execute("SELECT id FROM courses WHERE course_name=?", (course,))
    cid = cur.fetchone()[0]
    cur.execute("INSERT INTO college_courses(college_id, course_id) VALUES (?,?)",
                (college_id, cid))

conn.commit()
conn.close()

print("✅ College with multiple courses added!")
