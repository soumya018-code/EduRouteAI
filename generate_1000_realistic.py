import sqlite3
import random

conn = sqlite3.connect("colleges.db")
cur = conn.cursor()

def get_course_ids():
    cur.execute("SELECT id, course_name FROM courses")
    return cur.fetchall()

course_data = get_course_ids()

states_cities = {
    "Maharashtra": ["Mumbai", "Pune", "Nagpur"],
    "Tamil Nadu": ["Chennai", "Coimbatore", "Madurai"],
    "Karnataka": ["Bangalore", "Mysore"],
    "Delhi": ["New Delhi"],
    "Uttar Pradesh": ["Lucknow", "Noida"],
    "Rajasthan": ["Jaipur", "Udaipur"],
    "West Bengal": ["Kolkata"],
    "Telangana": ["Hyderabad"],
    "Odisha": ["Bhubaneswar"],
    "Gujarat": ["Ahmedabad", "Surat"],
    "Madhya Pradesh": ["Bhopal"],
    "Punjab": ["Chandigarh"]
}

exam_map = {
    "BTech": "JEE Main",
    "MBA": "CAT",
    "MCA": "NIMCET",
    "BCA": "CUET",
    "MTech": "GATE",
    "PhD": "University Entrance",
    "BSc": "CUET",
    "BCom": "CUET",
    "BA": "CUET",
    "MA": "University Entrance",
    "MSc": "University Entrance"
}

for i in range(1, 1001):

    state = random.choice(list(states_cities.keys()))
    city = random.choice(states_cities[state])
    college_name = f"{city} Institute of Technology and Science {i}"

    fees = random.randint(40000, 250000)
    cutoff = random.randint(60, 95)
    capacity = random.randint(300, 3000)

    cur.execute("""
    INSERT INTO colleges(name,state,city,fees,cutoff,entrance_exam,capacity)
    VALUES (?,?,?,?,?,?,?)
    """, (college_name, state, city, fees, cutoff, "Multiple Exams", capacity))

    college_id = cur.lastrowid

    # Assign 2–4 random courses
    selected_courses = random.sample(course_data, random.randint(2, 4))

    for cid, cname in selected_courses:
        cur.execute("INSERT INTO college_courses VALUES (?,?)", (college_id, cid))

conn.commit()
conn.close()

print("✅ 1000 realistic colleges generated successfully!")
