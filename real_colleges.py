import sqlite3

conn = sqlite3.connect("colleges.db")
cur = conn.cursor()

def get_course_id(course_name):
    cur.execute("SELECT id FROM courses WHERE course_name=?", (course_name,))
    row = cur.fetchone()
    return row[0] if row else None

colleges = [
    # name, state, city, avg fees per year, cutoff %, exam, capacity, courses
    ("KIIT University", "Odisha", "Bhubaneswar", 180000, 85, "KIITEE", 8000, ["BTech","MCA","MBA","PhD"]),
    ("IIT Delhi", "Delhi", "New Delhi", 220000, 98, "JEE Advanced", 1200, ["BTech","MTech","PhD"]),
    ("NIT Tiruchirappalli", "Tamil Nadu", "Tiruchirappalli", 125000, 95, "JEE Main", 1100, ["BTech","MTech","PhD"]),
    ("VIT Vellore", "Tamil Nadu", "Vellore", 180000, 85, "VITEEE", 5000, ["BTech","MCA","MBA"]),
    ("Anna University", "Tamil Nadu", "Chennai", 75000, 88, "TNEA", 1500, ["BTech","MTech"]),
    ("Delhi University", "Delhi", "Delhi", 30000, 80, "CUET", 20000, ["BSc","BCom","BA","MA"]),
    ("Osmania University", "Telangana", "Hyderabad", 40000, 75, "OUCET", 1800, ["BSc","MSc","PhD"]),
    ("Jadavpur University", "West Bengal", "Kolkata", 50000, 90, "WBJEE", 1000, ["BTech","MTech","PhD"]),
]

for name, state, city, fees, cutoff, exam, capacity, course_list in colleges:

    cur.execute("""
    INSERT INTO colleges(name,state,city,fees,cutoff,entrance_exam,capacity)
    VALUES (?,?,?,?,?,?,?)
    """, (name,state,city,fees,cutoff,exam,capacity))

    college_id = cur.lastrowid

    for course in course_list:
        cid = get_course_id(course)
        if cid:
            cur.execute("INSERT INTO college_courses VALUES (?,?)", (college_id,cid))
        else:
            print("⚠ Course not found in table:", course)

conn.commit()
conn.close()

print("✅ Real colleges with accurate details inserted!")
