import sqlite3

def init_db():
    conn = sqlite3.connect("colleges.db")
    cur = conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        role TEXT)""")

    cur.execute("""CREATE TABLE IF NOT EXISTS colleges(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        state TEXT,
        course TEXT,
        fees INTEGER,
        cutoff REAL,
        logo TEXT)""")

    cur.execute("""CREATE TABLE IF NOT EXISTS reviews(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        college_id INTEGER,
        user_id INTEGER,
        rating INTEGER,
        comment TEXT)""")

    cur.execute("SELECT * FROM users WHERE role='admin'")
    if not cur.fetchone():
        cur.execute("INSERT INTO users(username,password,role) VALUES('admin','admin123','admin')")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
