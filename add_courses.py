import sqlite3

courses = ["BTech", "MBA", "MCA", "BCA", "MTech", "PhD", "BSc", "BCom", "BA", "MA", "MSc"]

conn = sqlite3.connect("colleges.db")
cur = conn.cursor()

for c in courses:
    cur.execute("INSERT OR IGNORE INTO courses(course_name) VALUES(?)", (c,))

conn.commit()
conn.close()

print("✅ Courses inserted successfully")
