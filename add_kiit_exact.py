import sqlite3

conn = sqlite3.connect("colleges.db")
cur = conn.cursor()

def get_course_id(course_name):
    cur.execute("SELECT id FROM courses WHERE course_name=?", (course_name,))
    r = cur.fetchone()
    return r[0] if r else None

# replace these values with your preferred authoritative ones
name = "KIIT University"
state = "Odisha"
city = "Bhubaneswar"
fees_total = 620000        # total (tuition + typical hostel/other) — change if you want tuition-only
cutoff = 85                # example
entrance = "KIITEE"
capacity = 420


# insert college
cur.execute("""
INSERT INTO colleges(name,state,city,fees,cutoff,entrance_exam,capacity)
VALUES (?,?,?,?,?,?,?)
""", (name, state, city, fees_total, cutoff, entrance, capacity))
college_id = cur.lastrowid

# ensure courses exist (run add_courses.py first to populate common courses)
for course_name in ["BTech","MCA","MBA","PhD"]:
    cid = get_course_id(course_name)
    if cid:
        cur.execute("INSERT INTO college_courses VALUES (?,?)", (college_id, cid))
    else:
        print("Course not found in courses table:", course_name)

conn.commit()
conn.close()

print("✅ KIIT inserted with exact data (edit script values if you want different numbers)")
