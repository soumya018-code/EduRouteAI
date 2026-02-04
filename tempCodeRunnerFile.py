from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from flask_cors import CORS
import sqlite3, jwt, datetime
from functools import wraps
import database

app = Flask(__name__)
CORS(app)
bcrypt = Bcrypt(app)
SECRET_KEY = "secret123"

database.init_db()

def query_db(q, args=(), one=False):
    conn = sqlite3.connect("colleges.db")
    cur = conn.cursor()
    cur.execute(q, args)
    r = cur.fetchone() if one else cur.fetchall()
    conn.commit()
    conn.close()
    return r

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            return jsonify({"error":"Token missing"}),403
        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        except:
            return jsonify({"error":"Invalid token"}),403
        return f(data,*args,**kwargs)
    return decorated

@app.route("/register", methods=["POST"])
def register():
    d = request.json
    pw = bcrypt.generate_password_hash(d["password"]).decode()
    try:
        query_db("INSERT INTO users(username,password,role) VALUES(?,?,?)",
                 (d["username"], pw, "student"))
        return jsonify({"status":"registered"})
    except:
        return jsonify({"status":"user exists"})

@app.route("/login", methods=["POST"])
def login():
    d = request.json
    user = query_db("SELECT id,password,role FROM users WHERE username=?",
                    (d["username"],), True)
    if user and bcrypt.check_password_hash(user[1], d["password"]):
        token = jwt.encode({
            "user_id":user[0],
            "role":user[2],
            "exp":datetime.datetime.utcnow()+datetime.timedelta(hours=5)
        }, SECRET_KEY, algorithm="HS256")
        return jsonify({"status":"success","token":token,"role":user[2]})
    return jsonify({"status":"fail"})

@app.route("/add_college", methods=["POST"])
@token_required
def add_college(user):
    if user["role"]!="admin":
        return jsonify({"error":"Unauthorized"}),403
    d=request.json
    query_db("INSERT INTO colleges(name,state,course,fees,cutoff) VALUES(?,?,?,?,?)",
             (d["name"],d["state"],d["course"],d["fees"],d["cutoff"]))
    return jsonify({"status":"college added"})

@app.route("/search_colleges")
def search():
    try:
        course = request.args.get("course", "")
        max_fees = int(request.args.get("fees", 999999))

        conn = sqlite3.connect("colleges.db")
        cur = conn.cursor()

        cur.execute("""
            SELECT name, city, state, courses, fees, entrance_exam, capacity
            FROM colleges
            WHERE courses LIKE ? AND fees <= ?
        """, (f"%{course}%", max_fees))

        rows = cur.fetchall()
        conn.close()

        result = []
        for r in rows:
            result.append({
                "name": r[0],
                "city": r[1],
                "state": r[2],
                "courses": r[3],
                "fees": r[4],
                "exam": r[5],
                "capacity": r[6]
            })

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)})


@app.route("/chatbot", methods=["POST"])
def chatbot():
    msg = request.json["message"].lower()
    if "engineering" in msg:
        reply = "You can pursue BTech or Diploma Engineering."
    elif "medical" in msg:
        reply = "Options include MBBS, BDS, BSc Nursing."
    else:
        reply = "Ask about careers, colleges, or courses."
    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
