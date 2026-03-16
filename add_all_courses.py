import sqlite3

conn = sqlite3.connect("colleges.db")
cur = conn.cursor()

courses = [
"MCA","BTech","MBA","M.Tech","M.Sc","MA","Ph.D.",
"BCA","B.Com","B.Sc","B.Tech","MBA","Executive MBA",
"BA","BBA","BSc","MSc","MCom","LLM","BA LLB",
"MBBS","MSW","BBA / B.Com","B.Tech / Dual Degree"
]

for c in courses:
    cur.execute("INSERT OR IGNORE INTO courses(course_name) VALUES(?)",(c,))

conn.commit()
conn.close()

print("All courses inserted successfully")