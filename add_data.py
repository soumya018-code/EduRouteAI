import sqlite3

conn = sqlite3.connect("colleges.db")
cur = conn.cursor()

colleges = [
    ("IIT Delhi", "Delhi", "New Delhi", "BTech", 220000, 98, "JEE Advanced", 1200),
    ("IIT Bombay", "Maharashtra", "Mumbai", "BTech", 225000, 99, "JEE Advanced", 1300),
    ("NIT Trichy", "Tamil Nadu", "Tiruchirappalli", "BTech", 125000, 95, "JEE Main", 1100),
    ("VIT Vellore", "Tamil Nadu", "Vellore", "BTech", 180000, 85, "VITEEE", 5000),
    ("BITS Pilani", "Rajasthan", "Pilani", "BTech", 240000, 97, "BITSAT", 4500),
    ("Delhi University", "Delhi", "Delhi", "BSc", 30000, 80, "CUET", 20000),
    ("AIIMS Delhi", "Delhi", "New Delhi", "MBBS", 6000, 99, "NEET", 125),
    ("Anna University", "Tamil Nadu", "Chennai", "BTech", 75000, 88, "TNEA", 1500),
    ("Jadavpur University", "West Bengal", "Kolkata", "BTech", 50000, 90, "WBJEE", 1000),
    ("Osmania University", "Telangana", "Hyderabad", "BSc", 40000, 75, "OUCET", 1800)
]

cur.executemany("""
INSERT INTO colleges
(name, state, city, courses, fees, cutoff, entrance_exam, capacity)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", colleges)

conn.commit()
conn.close()

print("✅ Colleges added successfully!")
