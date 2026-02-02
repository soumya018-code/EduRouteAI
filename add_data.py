import sqlite3

conn = sqlite3.connect("colleges.db")
cur = conn.cursor()

cur.execute("""
INSERT INTO colleges (name, state, course, fees, cutoff)
VALUES
('ABC Engineering College', 'Delhi', 'BTech', 80000, 75),
('XYZ Institute of Technology', 'Maharashtra', 'BTech', 95000, 82),
('National MBA College', 'Karnataka', 'MBA', 120000, 70),
('Medical Sciences College', 'Tamil Nadu', 'MBBS', 150000, 85)
""")

conn.commit()
conn.close()

print("Colleges added successfully!")
