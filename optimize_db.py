import sqlite3

conn = sqlite3.connect("colleges.db")
cur = conn.cursor()

cur.execute("CREATE INDEX IF NOT EXISTS idx_courses ON colleges(courses)")
cur.execute("CREATE INDEX IF NOT EXISTS idx_fees ON colleges(fees)")

conn.commit()
conn.close()

print("✅ Database optimized!")
