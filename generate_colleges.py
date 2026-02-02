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
    "Odisha": ["Bhubaneswar","Sambalpur","Balasore","Rourkela"]
}

courses_list = ["BTech", "MBA", "BSc", "BCom", "BA", "MBBS", "MTech"]
exams = {
    "BTech": "JEE Main",
    "MBA": "CAT",
    "MBBS": "NEET",
    "BSc": "CUET",
    "BCom": "CUET",
    "BA": "CUET",
    "MTech": "GATE"
}

conn = sqlite3.connect("colleges.db")
cur = conn.cursor()

for i in range(1, 1001):  # 🔹 Change to 2000 if you want
    state = random.choice(list(states.keys()))
    city = random.choice(states[state])
    course = random.choice(courses_list)

    name = f"{city} Institute of {course} Studies {i}"
    fees = random.randint(20000, 250000)
    cutoff = random.randint(60, 99)
    exam = exams.get(course, "Entrance Test")
    capacity = random.randint(200, 3000)

    cur.execute("""
    INSERT INTO colleges (name, state, city, courses, fees, cutoff, entrance_exam, capacity)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (name, state, city, course, fees, cutoff, exam, capacity))

conn.commit()
conn.close()

print("✅ 1000 Colleges Inserted Successfully!")
