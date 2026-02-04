import sqlite3

def init_db():
    conn = sqlite3.connect("colleges.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        role TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS colleges(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        state TEXT,
        city TEXT,
        fees INTEGER,
        cutoff INTEGER,
        entrance_exam TEXT,
        capacity INTEGER
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS courses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_name TEXT UNIQUE
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS college_courses(
        college_id INTEGER,
        course_id INTEGER,
        FOREIGN KEY(college_id) REFERENCES colleges(id),
        FOREIGN KEY(course_id) REFERENCES courses(id)
    )
    """)


    cur.execute("""
    CREATE TABLE IF NOT EXISTS reviews(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        college_id INTEGER,
        user_id INTEGER,
        rating INTEGER,
        comment TEXT
    )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
