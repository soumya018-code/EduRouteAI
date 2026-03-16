
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
@app.route("/")
def home():
    return "Server is working"


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
    query_db("""
    INSERT INTO colleges(name,state,city,fees,cutoff,entrance_exam,capacity)
    VALUES(?,?,?,?,?,?,?)
    """, (d["name"], d["state"], d["city"], d["fees"], d["cutoff"], d["entrance_exam"], d["capacity"]))

    return jsonify({"status":"college added"})
    cur.execute(query, (f"%{course}%", fees))

    rows = cur.fetchall()
    conn.close()

@app.route("/search_colleges")
def search_colleges():

    course = request.args.get("course", "").lower()
    fees = int(request.args.get("fees", 99999999))
    state = request.args.get("state", "").lower()

    conn = sqlite3.connect("colleges.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    query = """
    SELECT 
        colleges.name,
        colleges.city,
        colleges.state,
        courses.course_name AS courses,
        college_courses.fees,
        college_courses.capacity,
        colleges.entrance_exam AS exam
    FROM colleges
    JOIN college_courses
        ON colleges.id = college_courses.college_id
    JOIN courses
        ON courses.id = college_courses.course_id
    WHERE 1=1
    """

    params = []

    # course filter
    if course:
        query += " AND LOWER(courses.course_name) LIKE ?"
        params.append(f"%{course}%")

    # fee filter
    query += " AND college_courses.fees <= ?"
    params.append(fees)

    # state filter
    if state and state != "any":
        query += " AND LOWER(colleges.state) LIKE ?"
        params.append(f"%{state}%")

    query += " LIMIT 50"

    cur.execute(query, params)

    rows = cur.fetchall()
    conn.close()

    return jsonify([dict(r) for r in rows])
    
@app.route("/chatbot", methods=["POST"])
def chatbot():
    try:
        msg = request.json.get("message", "").lower()

        if "mca" in msg:
            reply = "MCA is a Master's in Computer Applications."
        elif "bca" in msg:
            reply = "BCA is Bachelor of Computer Applications."
        elif "btech" in msg:
            reply = "BTech is a 4-year engineering program."
        elif "kiit" in msg:
            reply = "KIIT Bhubaneswar is a top private university in India."
        elif "phd" in msg:
            reply = "PhD is a doctoral research degree."
        else:
            reply = "Ask about MCA, BCA, BTech, PhD or KIIT."

        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": str(e)})
    
print("REGISTERED ROUTES:")
print(app.url_map)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
