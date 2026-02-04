import sqlite3
import random

states = {
    "Maharashtra": ["Mumbai", "Pune", "Nagpur"],
    "Tamil Nadu": ["Chennai", "Coimbatore", "Madurai"],
    "Karnataka": ["Bangalore", "Mysore", "Mangalore"],
    "Delhi": ["New Delhi"],
    "Uttar Pradesh": ["Lucknow", "Noida", "Kanpur"],
    "Rajasthan": ["Jaipur", "Udaipur"],
    "West Bengal": ["Kolkata", "Durgapur"],
    "Telangana": ["Hyderabad", "Warangal"],
    "Odisha": ["Bhubaneswar", "Cuttack"]
}

conn = sqlite3.connect("colleges.db")
cur = conn.cursor()

# Get all course IDs
cur.execute("SELECT id FROM courses")
course_ids = [row[0] for row in cur.fetchall()]

for i in range(1, 10001):
    state = random.choice(list(states.keys()))
    city = random.choice(states[state])
    name = f"{city} Institute of Higher Studies {i}"
    fees = random.randint(20000, 250000)
    cutoff = random.randint(60, 99)
    exam = "National Entrance Exam"
    capacity = random.randint(200, 5000)

    # Insert college
    cur.execute("""
    INSERT INTO colleges(name, state, city, fees, cutoff, entrance_exam, capacity)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (name, state, city, fees, cutoff, exam, capacity))

    college_id = cur.lastrowid

    # Assign 1–3 random courses to this college
    selected_courses = random.sample(course_ids, random.randint(1, 3))
    for cid in selected_courses:
        cur.execute("INSERT INTO college_courses VALUES (?, ?)", (college_id, cid))

conn.commit()
conn.close()

print("✅ 10,000 colleges with courses inserted!")
