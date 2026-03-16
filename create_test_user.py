import sqlite3
from flask_bcrypt import Bcrypt
from flask import Flask

app = Flask(__name__)
bcrypt = Bcrypt(app)

conn = sqlite3.connect("colleges.db")
cur = conn.cursor()

password = bcrypt.generate_password_hash("1234").decode()

cur.execute("INSERT INTO users(username,password,role) VALUES(?,?,?)",
            ("admin", password, "admin"))

conn.commit()
conn.close()

print("✅ Test user created")
