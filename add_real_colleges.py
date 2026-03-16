import sqlite3

conn = sqlite3.connect("colleges.db")
cur = conn.cursor()

def get_course_id(course):
    cur.execute("INSERT OR IGNORE INTO courses(course_name) VALUES(?)", (course,))
    cur.execute("SELECT id FROM courses WHERE course_name=?", (course,))
    return cur.fetchone()[0]

def add_college_with_courses(name, state, city, exam, course_list):

    cur.execute(
        "INSERT INTO colleges(name,state,city,entrance_exam) VALUES(?,?,?,?)",
        (name, state, city, exam)
    )

    college_id = cur.lastrowid
    for item in course_list:
        course = item[0]
        fees = item[1]
        seats = item[2]

        course_id = get_course_id(course)

        cur.execute("""
        INSERT INTO college_courses(college_id, course_id, fees, capacity)
        VALUES(?,?,?,?)
        """, (college_id, course_id, fees, seats))


# 🔥 REAL DATA WITH MULTIPLE COURSES

add_college_with_courses(
    "KIIT University", "Odisha", "Bhubaneswar", "KIITEE",
    [
        ("MCA", 575000, 600),
        ("BTech", 2000000, 5000),
        ("MBA", 1800000, 360),
        ("M.Tech", 880000, 50),
        ("M.Sc", 800000, 20),
        ("MA", 460000, 240),
        ("Ph.D.", 786000, 50),
        ("BCA", 1100000, 300),
        ("B.Com", 1175000, 500),
        ("B.Sc", 850000, 100)
        
    ]
)


        

add_college_with_courses(
    "SOA University", "Odisha", "Bhubaneswar", "SAAT",
    [
        ("MCA", 384000, 360),
        ("BTech", 1200000, 1500),
        ("MBA", 1000000, 300),
        ("M.Tech", 300000, 18),
        ("M.Sc", 20000,20)
    ]
)
add_college_with_courses(
    "SILICON University", "Odisha", "Bhubaneswar", "SUAT",
    [
        ("MCA", 320000, 60),
        ("BTech", 840000, 840),
        ("MBA", 400000, 1047),
        ("M.Tech", 300000, 36),
        ("M.Sc", 300000, 30),
        ("MA", 200000, 50),
        ("Ph.D.", 120000, 50),
        ("BCA", 500000, 60),
        ("B.Com", 350000, 50),
        ("B.Sc", 400000, 60)
        
    ]
)

add_college_with_courses(
    "BIRLA GLOBAL  University", "Odisha", "Bhubaneswar", "BET",
    [
        ("MCA", 315000, 244),
        ("BTech", 1050000, 263),
        ("MBA", 1000000, 180),
        ("M.Tech", 500000, 50),
        ("M.Sc", 250000, 20),
        ("MA", 260000, 40),
        ("Ph.D.", 420000, 30),
        ("BCA", 393000, 40),
        ("B.Com", 465000, 175),
        ("B.Sc", 300000, 263)
        
    ]
)
add_college_with_courses(
    "CENTURION University", "Odisha", "Bhubaneswar", "CUEE",
    [
        ("MCA", 380000,250 ),
        ("BTech", 1400000,1600 ),
        ("MBA", 960000, 60),
        ("M.Tech", 360000, 18),
        ("M.Sc", 320000, 10),
        ("MA", 300000, 40),
        ("Ph.D.", 400000, 15),
        ("BCA", 680000, 100),
        ("B.Com", 175000, 100),
        ("B.Sc", 800000, 200)
        
    ]
)
add_college_with_courses(
    "SRI SRI University", "Odisha", "Cuttack", "SSU CET",
    [
        ("MCA", 575000, 600),
        ("BTech", 2000000, 5000),
        ("MBA", 1800000, 360),
        ("M.Tech", 880000, 50),
        ("M.Sc", 800000, 20),
        ("MA", 460000, 240),
        ("Ph.D.", 786000, 50),
        ("BCA", 1100000, 300),
        ("B.Com", 1175000, 500),
        ("B.Sc", 850000, 100)
        
    ]
)
add_college_with_courses(
    "IIT Bombay", "Maharashtra", "Mumbai", "JEE-Advanced",
    [
        ("B.Tech", 950000, 4000),  
        ("M.Tech", 550000, 1200),
        ("MBA", 400000, 300),
        ("Ph.D.", 250000, 200)
    ]
)
add_college_with_courses(
    "IIT Delhi", "Delhi", "New Delhi", "JEE-Advanced",
    [
        ("B.Tech", 850000, 3500),  
        ("M.Tech", 500000, 1000),
        ("MBA", 380000, 300),
        ("Ph.D.", 230000, 180)
    ]
)
add_college_with_courses(
    "IIT Madras", "Tamil Nadu", "Chennai", "JEE-Advanced",
    [
        ("B.Tech", 858000, 3500),  
        ("M.Tech", 520000, 1100),
        ("MBA", 390000, 280),
        ("Ph.D.", 240000, 200)
    ]
)
add_college_with_courses(
    "IIT Kanpur", "Uttar Pradesh", "Kanpur", "JEE-Advanced",
    [
        ("B.Tech", 1167000, 3500),  
        ("M.Tech", 540000, 1000),
        ("MBA", 380000, 270),
        ("Ph.D.", 240000, 180)
    ]
)
add_college_with_courses(
    "IIT Dharwad", "Karnataka", "Dharwad", "JEE-Advanced",
    [
        ("B.Tech", 890000, 1700),
        ("M.Tech", 230000, 700),
        ("Ph.D.", 50000, 200)
    ]
)
add_college_with_courses(
    "IIT Bhilai", "Chhattisgarh", "Bhilai", "JEE-Advanced",
    [
        ("B.Tech", 860000, 1700),
        ("M.Tech", 230000, 700),
        ("Ph.D.", 50000, 200)
    ]
)
add_college_with_courses(
    "IIT Palakkad", "Kerala", "Palakkad", "JEE-Advanced",
    [
        ("B.Tech", 895000, 1500),
        ("M.Tech", 230000, 600),
        ("Ph.D.", 50000, 200)
    ]
)
add_college_with_courses(
    "IIT Jammu", "Jammu & Kashmir", "Jammu", "JEE-Advanced",
    [
        ("B.Tech", 819000, 1500),
        ("M.Tech", 230000, 700),
        ("Ph.D.", 50000, 250)
    ]
)
add_college_with_courses(
    "IIT Goa", "Goa", "Goa", "JEE-Advanced",
    [
        ("B.Tech", 852000, 1500),
        ("M.Tech", 230000, 700),
        ("Ph.D.", 50000, 250)
    ]
)
add_college_with_courses(
    "IIT Tirupati", "Andhra Pradesh", "Tirupati", "JEE-Advanced",
    [
        ("B.Tech", 881000, 1800),
        ("M.Tech", 230000, 700),
        ("Ph.D.", 50000, 250)
    ]
)
add_college_with_courses(
    "IIT Bhubaneswar", "Odisha", "Bhubaneswar", "JEE-Advanced",
    [
        ("B.Tech", 894000, 2200),
        ("M.Tech", 230000, 800),
        ("Ph.D.", 50000, 250)
    ]
)
add_college_with_courses(
    "IIT Mandi", "Himachal Pradesh", "Mandi", "JEE-Advanced",
    [
        ("B.Tech", 863000, 1800),
        ("M.Tech", 230000, 700),
        ("Ph.D.", 50000, 250)
    ]
)
add_college_with_courses(
    "IIT Jodhpur", "Rajasthan", "Jodhpur", "JEE-Advanced",
    [
        ("B.Tech", 1025000, 1800),
        ("M.Tech", 260000, 700),
        ("Ph.D.", 50000, 250)
    ]
)
add_college_with_courses(
    "IIT Patna", "Bihar", "Patna", "JEE-Advanced",
    [
        ("B.Tech", 985000, 2000),
        ("M.Tech", 240000, 800),
        ("Ph.D.", 50000, 250)
    ]
)
add_college_with_courses(
    "IIT Ropar", "Punjab", "Ropar", "JEE-Advanced",
    [
        ("B.Tech", 936000, 2000),
        ("M.Tech", 240000, 700),
        ("Ph.D.", 50000, 250)
    ]
)
add_college_with_courses(
    "IIT Gandhinagar", "Gujarat", "Gandhinagar", "JEE-Advanced",
    [
        ("B.Tech", 867000, 1800),
        ("M.Tech", 240000, 700),
        ("Ph.D.", 50000, 250)
    ]
)
add_college_with_courses(
    "IIT BHU Varanasi", "Uttar Pradesh", "Varanasi", "JEE-Advanced",
    [
        ("B.Tech", 858000, 3500),
        ("M.Tech", 250000, 1000),
        ("Ph.D.", 50000, 300)
    ]
)
add_college_with_courses(
    "IIT Indore", "Madhya Pradesh", "Indore", "JEE-Advanced",
    [
        ("B.Tech", 991000, 2200),
        ("M.Tech", 240000, 800),
        ("Ph.D.", 50000, 250)
    ]
)
add_college_with_courses(
    "IIT Hyderabad", "Telangana", "Hyderabad", "JEE-Advanced",
    [
        ("B.Tech", 908000, 3000),
        ("M.Tech", 280000, 1000),
        ("Ph.D.", 50000, 300)
    ]
)
add_college_with_courses(
    "IIT Roorkee", "Uttarakhand", "Roorkee", "JEE-Advanced",
    [
        ("B.Tech", 890000, 3200),
        ("M.Tech", 250000, 900),
        ("Ph.D.", 50000, 300)
    ]
)
add_college_with_courses(
    "IIT Guwahati", "Assam", "Guwahati", "JEE-Advanced",
    [
        ("B.Tech", 1199000, 2800),
        ("M.Tech", 260000, 900),
        ("Ph.D.", 50000, 300)
    ]
)
add_college_with_courses(
    "IIT Kharagpur", "West Bengal", "Kharagpur", "JEE-Advanced",
    [
        ("B.Tech", 1042000, 4000),
        ("M.Tech", 250000, 1500),
        ("Ph.D.", 50000, 400)
    ]
)
add_college_with_courses(
    "IIT-ISM Dhanbad", "Jharkhand", "Dhanbad", "JEE-Advanced / GATE / JAM / CAT",
    [
        ("B.Tech", 900000, 3500),                   
        ("M.Tech", 130000, 800),            
        ("MBA", 360000, 60),                
        ("M.Sc / M.Sc Tech", 140000, 300),  
        ("Ph.D.", 100000, 200)              
    ]
) 
add_college_with_courses(
    "National Institute of Technology Tiruchirappalli", "Tamil Nadu", "Tiruchirappalli", "JEE Main",
    [
        ("B.Tech", 500000, 4500),  
        ("M.Tech", 300000, 1200), 
        ("M.Sc", 180000, 300),
        ("MBA", 360000, 300),
        ("Ph.D.", 120000, 200)
    ]
)

add_college_with_courses(
    "National Institute of Technology Rourkela", "Odisha", "Rourkela", "JEE Main",
    [
        ("B.Tech", 620000, 7000),  
        ("M.Tech", 320000, 1200),
        ("M.Sc", 180000, 300),
        ("MBA", 350000, 300),
        ("Ph.D.", 120000, 200)
    ]
)

add_college_with_courses(
    "National Institute of Technology Karnataka Surathkal", "Karnataka", "Mangalore", "JEE Main",
    [
        ("B.Tech", 560000, 6000),  
        ("M.Tech", 310000, 1200),
        ("M.Sc", 180000, 300),
        ("MBA", 360000, 300),
        ("Ph.D.", 120000, 200)
    ]
)

add_college_with_courses(
    "National Institute of Technology Calicut", "Kerala", "Kozhikode", "JEE Main",
    [
        ("B.Tech", 630000, 5000),  
        ("M.Tech", 320000, 1000),
        ("M.Sc", 180000, 300),
        ("MBA", 350000, 300),
        ("Ph.D.", 120000, 200)
    ]
)

add_college_with_courses(
    "National Institute of Technology Warangal", "Telangana", "Warangal", "JEE Main",
    [
        ("B.Tech", 550000, 5800),  
        ("M.Tech", 310000, 1100),
        ("M.Sc", 180000, 300),
        ("MBA", 350000, 300),
        ("Ph.D.", 120000, 200)
    ]
)

add_college_with_courses(
    "National Institute of Technology Delhi", "Delhi", "New Delhi", "JEE Main",
    [
        ("B.Tech", 500000, 5000),  
        ("M.Tech", 300000, 1000),
        ("M.Sc", 180000, 300),
        ("MBA", 370000, 320),
        ("Ph.D.", 120000, 200)
    ]
)

add_college_with_courses(
    "National Institute of Technology Patna", "Bihar", "Patna", "JEE Main",
    [
        ("B.Tech", 612000, 4000),  
        ("M.Tech", 300000, 800),
        ("M.Sc", 180000, 200),
        ("MBA", 350000, 200),
        ("Ph.D.", 120000, 150)
    ]
)

add_college_with_courses(
    "National Institute of Technology Durgapur", "West Bengal", "Durgapur", "JEE Main",
    [
        ("B.Tech", 500000, 4500),  
        ("M.Tech", 300000, 800),
        ("M.Sc", 180000, 200),
        ("MBA", 350000, 200),
        ("Ph.D.", 120000, 150)
    ]
)

add_college_with_courses(
    "National Institute of Technology Goa", "Goa", "Goa", "JEE Main",
    [
        ("B.Tech", 500000, 2000),  
        ("M.Tech", 280000, 500),
        ("M.Sc", 180000, 200),
        ("MBA", 350000, 200),
        ("Ph.D.", 120000, 150)
    ]
)

add_college_with_courses(
    "Dr. B R Ambedkar National Institute of Technology Jalandhar", "Punjab", "Jalandhar", "JEE Main",
    [
        ("B.Tech", 500000, 4500),  
        ("M.Tech", 300000, 800),
        ("M.Sc", 180000, 200),
        ("MBA", 350000, 200),
        ("Ph.D.", 120000, 150)
    ]
)

add_college_with_courses(
    "Motilal Nehru National Institute of Technology Allahabad", "Uttar Pradesh", "Prayagraj", "JEE Main",
    [
        ("B.Tech", 520000, 3800),
        ("M.Tech", 300000, 800),
        ("M.Sc", 180000, 200),
        ("MBA", 350000, 300),
        ("Ph.D.", 120000, 150)
    ]
)

add_college_with_courses(
    "Maulana Azad National Institute of Technology Bhopal", "Madhya Pradesh", "Bhopal", "JEE Main",
    [
        ("B.Tech", 500000, 3000),
        ("M.Tech", 300000, 800),
        ("M.Sc", 180000, 200),
        ("MBA", 350000, 300),
        ("Ph.D.", 120000, 150)
    ]
)

add_college_with_courses(
    "National Institute of Technology Kurukshetra", "Haryana", "Kurukshetra", "JEE Main",
    [
        ("B.Tech", 500000, 3000),
        ("M.Tech", 300000, 800),
        ("M.Sc", 180000, 200),
        ("MBA", 350000, 300),
        ("Ph.D.", 120000, 150)
    ]
)

add_college_with_courses(
    "National Institute of Technology Silchar", "Assam", "Silchar", "JEE Main",
    [
        ("B.Tech", 480000, 2500),
        ("M.Tech", 280000, 800),
        ("M.Sc", 180000, 200),
        ("MBA", 350000, 200),
        ("Ph.D.", 120000, 150)
    ]
)

add_college_with_courses(
    "National Institute of Technology Meghalaya", "Meghalaya", "Shillong", "JEE Main",
    [
        ("B.Tech", 500000, 2500),
        ("M.Tech", 280000, 800),
        ("M.Sc", 180000, 200),
        ("MBA", 350000, 200),
        ("Ph.D.", 120000, 150)
    ]
)

add_college_with_courses(
    "National Institute of Technology Nagaland", "Nagaland", "Dimapur", "JEE Main",
    [
        ("B.Tech", 500000, 2000),
        ("M.Tech", 280000, 800),
        ("M.Sc", 180000, 200),
        ("MBA", 350000, 200),
        ("Ph.D.", 120000, 150)
    ]
)

add_college_with_courses(
    "National Institute of Technology Manipur", "Manipur", "Imphal", "JEE Main",
    [
        ("B.Tech", 500000, 2000),
        ("M.Tech", 280000, 800),
        ("M.Sc", 180000, 200),
        ("MBA", 350000, 200),
        ("Ph.D.", 120000, 150)
    ]
)

add_college_with_courses(
    "National Institute of Technology Mizoram", "Mizoram", "Aizawl", "JEE Main",
    [
        ("B.Tech", 500000, 2000),
        ("M.Tech", 280000, 800),
        ("M.Sc", 180000, 200),
        ("MBA", 350000, 200),
        ("Ph.D.", 120000, 150)
    ]
)

add_college_with_courses(
    "National Institute of Technology Uttarakhand", "Uttarakhand", "Srinagar (Garhwal)", "JEE Main",
    [
        ("B.Tech", 500000, 2500),
        ("M.Tech", 280000, 800),
        ("M.Sc", 180000, 200),
        ("MBA", 350000, 200),
        ("Ph.D.", 120000, 150)
    ]
)

add_college_with_courses(
    "National Institute of Technology Puducherry", "Puducherry", "Karaikal", "JEE Main",
    [
        ("B.Tech", 500000, 2000),
        ("M.Tech", 280000, 800),
        ("M.Sc", 180000, 200),
        ("MBA", 350000, 200),
        ("Ph.D.", 120000, 150)
    ]
)

add_college_with_courses(
    "National Institute of Technology Jamshedpur", "Jharkhand", "Jamshedpur", "JEE Main",
    [
        ("B.Tech", 500000, 3500),
        ("M.Tech", 300000, 800),
        ("M.Sc", 180000, 200),
        ("MBA", 350000, 200),
        ("Ph.D.", 120000, 150)
    ]
)
add_college_with_courses(
    "National Institute of Technology Agartala", "Tripura", "Agartala", "JEE Main",
    [
        ("B.Tech", 500000, 3000),
        ("M.Tech", 290000, 600),
        ("M.Sc", 180000, 150),
        ("MBA", 350000, 200),
        ("Ph.D.", 120000, 100)
    ]
)

add_college_with_courses(
    "National Institute of Technology Arunachal Pradesh", "Arunachal Pradesh", "Yupia", "JEE Main",
    [
        ("B.Tech", 500000, 1500),
        ("M.Tech", 280000, 400),
        ("M.Sc", 180000, 150),
        ("MBA", 350000, 150),
        ("Ph.D.", 120000, 100)
    ]
)

add_college_with_courses(
    "National Institute of Technology Sikkim", "Sikkim", "South Sikkim", "JEE Main",
    [
        ("B.Tech", 500000, 1500),
        ("M.Tech", 280000, 400),
        ("M.Sc", 180000, 150),
        ("MBA", 350000, 150),
        ("Ph.D.", 120000, 100)
    ]
)

add_college_with_courses(
    "National Institute of Technology Srinagar", "Jammu & Kashmir", "Srinagar", "JEE Main",
    [
        ("B.Tech", 500000, 1500),
        ("M.Tech", 280000, 500),
        ("M.Sc", 180000, 150),
        ("MBA", 350000, 200),
        ("Ph.D.", 120000, 100)
    ]
)

add_college_with_courses(
    "National Institute of Technology Raipur", "Chhattisgarh", "Raipur", "JEE Main",
    [
        ("B.Tech", 560000, 3500),
        ("M.Tech", 300000, 800),
        ("M.Sc", 180000, 200),
        ("MBA", 350000, 200),
        ("Ph.D.", 120000, 150)
    ]
)

add_college_with_courses(
    "Malaviya National Institute of Technology Jaipur", "Rajasthan", "Jaipur", "JEE Main",
    [
        ("B.Tech", 550000, 3500),
        ("M.Tech", 300000, 800),
        ("M.Sc", 180000, 200),
        ("MBA", 350000, 250),
        ("Ph.D.", 120000, 150)
    ]
)

add_college_with_courses(
    "Visvesvaraya National Institute of Technology Nagpur", "Maharashtra", "Nagpur", "JEE Main",
    [
        ("B.Tech", 500000, 3500),
        ("M.Tech", 300000, 800),
        ("M.Sc", 180000, 200),
        ("MBA", 350000, 250),
        ("Ph.D.", 120000, 150)
    ]
)

add_college_with_courses(
    "National Institute of Technology Andhra Pradesh", "Andhra Pradesh", "Tadepalligudem", "JEE Main",
    [
        ("B.Tech", 500000, 2500),
        ("M.Tech", 290000, 600),
        ("M.Sc", 180000, 150),
        ("MBA", 350000, 200),
        ("Ph.D.", 120000, 100)
    ]
)


add_college_with_courses(
    "Institute of Chemical Technology (ICT Mumbai)", "Maharashtra", "Mumbai", "JEE Main / Entrance",
    [
        ("B.Tech", 330000, 1600),          
        ("M.Tech", 220000, 600),
        ("Ph.D.", 80000, 150)
    ]
)

add_college_with_courses(
    "Veermata Jijabai Technological Institute (VJTI)", "Maharashtra", "Mumbai", "MHT CET / JEE Main",
    [
        ("B.Tech", 300000, 2400),          
        ("M.Tech", 200000, 500),
        ("Ph.D.", 80000, 120)
    ]
)

add_college_with_courses(
    "Sardar Patel Institute of Technology (SPIT)", "Maharashtra", "Mumbai", "MHT CET / JEE Main",
    [
        ("B.Tech", 350000, 2400),          
        ("M.Tech", 220000, 500),
        ("Ph.D.", 80000, 120)
    ]
)

add_college_with_courses(
    "Dwarkadas J. Sanghvi College of Engineering (DJSCE)", "Maharashtra", "Mumbai", "MHT CET / JEE Main",
    [
        ("B.Tech", 500000, 2200),          
        ("M.Tech", 240000, 500),
        ("Ph.D.", 80000, 100)
    ]
)

add_college_with_courses(
    "SVKM’s Narsee Monjee Institute of Management Studies (NMIMS)", "Maharashtra", "Mumbai", "NMAT / NPAT",
    [
        ("BBA", 800000, 1000),
        ("B.Tech", 1000000, 900),
        ("MBA", 800000, 500),
        ("Ph.D.", 200000, 100)
    ]
)

add_college_with_courses(
    "S.P. Jain Institute of Management & Research (SPJIMR)", "Maharashtra", "Mumbai", "CAT / SPJAT",
    [
        ("MBA", 1150000, 300),
        ("Executive MBA", 800000, 120),
        ("Ph.D.", 280000, 50)
    ]
)

add_college_with_courses(
    "Jamnalal Bajaj Institute of Management Studies (JBIMS)", "Maharashtra", "Mumbai", "CAT / MAH MBA CET",
    [
        ("MBA", 350000, 300),
        ("Ph.D.", 100000, 50)
    ]
)

add_college_with_courses(
    "Tata Institute of Social Sciences (TISS Mumbai)", "Maharashtra", "Mumbai", "TISSNET",
    [
        ("MA (Social Sciences)", 150000, 500),
        ("MSW", 150000, 300),
        ("Ph.D.", 100000, 80)
    ]
)

add_college_with_courses(
    "St. Xavier’s College, Mumbai", "Maharashtra", "Mumbai", "Merit / Entrance",
    [
        ("BA", 100000, 1500),
        ("BSc", 120000, 1000),
        ("B.Com", 100000, 1200),
        ("MA / MSc", 80000, 300)
    ]
)

add_college_with_courses(
    "University of Mumbai (MU)", "Maharashtra", "Mumbai", "Merit / Entrance",
    [
        ("BA", 50000, 50000),
        ("BSc", 60000, 40000),
        ("BCom", 50000, 60000),
        ("MCom / MSc", 50000, 30000),
        ("Ph.D.", 80000, 20000)
    ]
)
add_college_with_courses(
    "Jawaharlal Nehru University (JNU)", "Delhi", "New Delhi", "JNU Entrance",
    [
        ("BA/BS", 50000, 1500),
        ("MA/MSc/MTech", 80000, 800),
        ("Ph.D.", 120000, 300)
    ]
)
add_college_with_courses(
    "University of Delhi (DU)", "Delhi", "New Delhi", "CUET / Merit",
    [
        ("BA / BSc / BCom", 60000, 10000),
        ("MA / MSc / MCom", 80000, 5000),
        ("MBA", 300000, 1000),
        ("Ph.D.", 100000, 500)
    ]
)
add_college_with_courses(
    "Netaji Subhas University of Technology (NSUT)", "Delhi", "New Delhi", "JEE Main",
    [
        ("B.Tech", 840000, 2800),
        ("M.Tech", 300000, 800),
        ("MBA", 350000, 250),
        ("Ph.D.", 120000, 120)
    ]
)
add_college_with_courses(
    "Anna University", "Tamil Nadu", "Chennai", "TNEA / Entrance",
    [
        ("B.Tech (CEG Campus)", 500000, 4500),   
        ("M.Tech", 250000, 1000),
        ("MBA", 350000, 300),
        ("Ph.D.", 100000, 150)
    ]
)
add_college_with_courses(
    "SRM Institute of Science and Technology", "Tamil Nadu", "Kattankulathur (Chennai)", "SRMJEEE / Entrance",
    [
        ("B.Tech", 1100000, 6000),     
        ("M.Tech", 380000, 1000),
        ("MBA", 650000, 500),
        ("Ph.D.", 150000, 200)
    ]
)
add_college_with_courses(
    "Madras Christian College (MCC)", "Tamil Nadu", "Chennai", "Merit / Entrance",
    [
        ("BA", 90000, 1300),
        ("BSc", 95000, 1100),
        ("BCom", 90000, 1200),
        ("MA / MSc", 100000, 300)
    ]
)

add_college_with_courses(
    "VIT Chennai", "Tamil Nadu", "Chennai", "VITEEE / Entrance",
    [
        ("B.Tech", 1100000, 5000),
        ("M.Tech", 350000, 1000),
        ("MBA", 650000, 400),
        ("Ph.D.", 150000, 200)
    ]
)

add_college_with_courses(
    "VIT-AP University (VIT Andhra Pradesh)", "Andhra Pradesh", "Amaravati", "VITEEE / VITMEE / VITREE",
    [
        ("B.Tech", 1000000, 4000),    
        ("BBA / B.Com", 320000, 1000),
        ("M.Tech", 320000, 700),
        ("MBA", 600000, 500),
        ("Ph.D.", 150000, 150)
    ]
)
add_college_with_courses(
    "VIT Bhopal University (VIT Bhopal)", "Madhya Pradesh", "Bhopal", "VITEEE / VITMEE / VITREE",
    [
        ("B.Tech", 1000000, 4500),   
        ("B.Sc", 340000, 1200),
        ("BBA / B.Com", 320000, 1000),
        ("M.Tech", 320000, 700),
        ("MBA", 600000, 500),
        ("Ph.D.", 150000, 150)
    ]
)
add_college_with_courses(
    "Symbiosis International (Deemed) University, Pune", "Maharashtra", "Pune", "Various Entrance (SET / SNAP / CUET)",
    [
        ("B.Tech", 600000, 3800),
        ("BA/BBA/BSc", 450000, 3000),
        ("MBA", 800000, 500),
        ("Ph.D.", 180000, 200)
    ]
)
add_college_with_courses(
    "Dr. D. Y. Patil Vidyapeeth (Deemed University)", "Maharashtra", "Pune", "University / Entrance",
    [
        ("MBBS", 15300000, 250),      
        ("B.Tech", 800000, 3500),
        ("MBA", 700000, 400),
        ("Ph.D.", 150000, 100)
    ]
)
add_college_with_courses(
    "Indian Institute of Science (IISc Bangalore)", "Karnataka", "Bangalore", "JEE/NEET/Merit/Entrance",
    [
        ("BSc", 80000, 300),
        ("B.Tech", 120000, 500),
        ("M.Tech", 200000, 200),
        ("M.Sc", 120000, 300),
        ("Ph.D.", 100000, 100)
    ]
)

add_college_with_courses(
    "Indian Institute of Management Bangalore (IIM Bangalore)", "Karnataka", "Bangalore", "CAT / GMAT",
    [
        ("MBA", 2200000, 350),
        ("Executive MBA", 1800000, 120),
        ("Ph.D. Management", 400000, 40)
    ]
)

add_college_with_courses(
    "National Law School of India University (NLSIU Bangalore)", "Karnataka", "Bangalore", "CLAT / Entrance",
    [
        ("BA LLB", 700000, 300),
        ("LLM", 500000, 100),
        ("Ph.D. Law", 200000, 50)
    ]
)

add_college_with_courses(
    "PES University", "Karnataka", "Bangalore", "PESSAT / JEE Main / COMEDK",
    [
        ("B.Tech", 1500000, 4000),   
        ("M.Tech", 400000, 800),
        ("MBA", 900000, 300),
        ("Ph.D.", 150000, 100)
    ]
)

add_college_with_courses(
    "R.V. College of Engineering (RVCE)", "Karnataka", "Bangalore", "KCET / COMEDK / JEE Main",
    [
        ("B.Tech", 1200000, 4500),
        ("M.Tech", 380000, 800),
        ("Ph.D.", 150000, 150)
    ]
)

add_college_with_courses(
    "BMS College of Engineering (BMSCE)", "Karnataka", "Bangalore", "KCET / COMEDK",
    [
        ("B.Tech", 1000000, 4000),
        ("M.Tech", 360000, 800),
        ("Ph.D.", 150000, 150)
    ]
)

add_college_with_courses(
    "Christ University Bangalore", "Karnataka", "Bangalore", "CUET / Entrance / Merit",
    [
        ("BA / BSc / BCom", 450000, 3000),
        ("BBA / BCA", 500000, 3500),
        ("MBA", 900000, 500),
        ("Ph.D.", 180000, 200)
    ]
)

add_college_with_courses(
    "Jain (Deemed-to-be) University", "Karnataka", "Bangalore", "Entrance / Merit",
    [
        ("B.Tech", 900000, 3500),
        ("BBA / BCom", 450000, 2500),
        ("MBA", 800000, 400),
        ("Ph.D.", 150000, 200)
    ]
)

add_college_with_courses(
    "International Institute of Information Technology Bangalore (IIITB)", "Karnataka", "Bangalore", "JEE Main / Entrance",
    [
        ("B.Tech / Dual Degree", 1500000, 1500),
        ("M.Tech", 450000, 400),
        ("Ph.D.", 180000, 80)
    ]
)

add_college_with_courses(
    "Bangalore University", "Karnataka", "Bangalore", "Merit / Entrance",
    [
        ("BA / BSc / BCom", 90000, 1500),
        ("MBA", 300000, 500),
        ("MSc / MA", 120000, 400),
        ("Ph.D.", 100000, 300)
    ]
)

add_college_with_courses(
    "MS Ramaiah Institute of Technology (MSRIT)", "Karnataka", "Bangalore", "KCET / COMEDK",
    [
        ("B.Tech", 1300000, 4000),
        ("M.Tech", 380000, 800),
        ("Ph.D.", 150000, 150)
    ]
)

add_college_with_courses(
    "Dayananda Sagar College of Engineering (DSCE)", "Karnataka", "Bangalore", "KCET / COMEDK",
    [
        ("B.Tech", 1100000, 3500),
        ("M.Tech", 350000, 800),
        ("Ph.D.", 150000, 150)
    ]
)

add_college_with_courses(
    "Alliance University", "Karnataka", "Bangalore", "Entrance / Merit",
    [
        ("B.Tech", 1500000, 2500),
        ("MBA", 1800000, 300),
        ("BA / BCom / BSc", 700000, 2000),
        ("Ph.D.", 250000, 100)
    ]
)
add_college_with_courses(
    "University of Hyderabad (UoH)", "Telangana", "Hyderabad", "CUET / Entrance",
    [
        ("B.Sc / BA / BCom", 200000, 1000),
        ("M.Sc / MA / MCom", 180000, 600),
        ("MBA", 400000, 300),
        ("Ph.D.", 120000, 200)
    ]
)

add_college_with_courses(
    "Osmania University", "Telangana", "Hyderabad", "CPGET / Merit",
    [
        ("BA / BSc / BCom", 150000, 1500),
        ("MBA", 380000, 500),
        ("M.Sc / MA / MCom", 180000, 700),
        ("Ph.D.", 120000, 200)
    ]
)

add_college_with_courses(
    "Jadavpur University", "West Bengal", "Kolkata", "Entrance / Merit",
    [
        ("B.Tech", 120000, 7000),   
        ("BA / BSc / BCom", 18000, 5000),
        ("M.Tech", 80000, 1200),
        ("MBA", 250000, 500),
        ("Ph.D.", 60000, 300)
    ]
)
add_college_with_courses(
    "Amity University, Kolkata", "West Bengal", "Kolkata", "Entrance / Merit",
    [
        ("B.Tech", 984000, 3200),   
        ("BA / BBA / BSc", 456000, 2500),
        ("MBA", 800000, 500),
        ("Ph.D.", 200000, 200)
    ]
)
add_college_with_courses(
    "Gauhati University", "Assam", "Guwahati", "Merit / Entrance",
    [
        ("BA / BSc / BCom", 30000, 1000),   
        ("MA / MSc / MCom", 60000, 300),
        ("MBA", 300000, 500),
        ("Ph.D.", 80000, 200)
    ]
)
add_college_with_courses(
    "Assam Down Town University (ADTU)", "Assam", "Guwahati", "Entrance / Merit",
    [
        ("B.Tech", 600000, 3500),
        ("MBA", 300000, 400),
        ("BA / BSc / BCom", 350000, 3000),
        ("Ph.D.", 150000, 100)
    ]
)
add_college_with_courses(
    "Royal Global University (RGU)", "Assam", "Guwahati", "Entrance / Merit",
    [
        ("B.Tech", 700000, 3000),
        ("MBA", 300000, 350),
        ("BBA / BSc / BCom", 400000, 2500),
        ("Ph.D.", 150000, 100)
    ]
)

conn.commit()
conn.close()

print("Colleges with multiple courses added!")
