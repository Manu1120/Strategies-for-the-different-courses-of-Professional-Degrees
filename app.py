from flask import Flask, jsonify, render_template, request, redirect, url_for, flash

app = Flask(__name__)  # ✅ Corrected __name__
app.secret_key = "your_secret_key"  # Required for flash messages

# Route for the welcome page
@app.route("/")
def home():
    return render_template("welcome.html")

# Route for the login page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        # Dummy authentication logic
        if username == "admin" and password == "password":  # Replace with actual logic
            flash("Login successful!", "success")
            return redirect(url_for("course_level"))
        else:
            flash("Invalid username or password. Please try again.", "error")
            return render_template("login.html")
    return render_template("login.html")

# Route for the Course Level selection page
@app.route("/course_level", methods=["GET", "POST"])
def course_level():
    if request.method == "POST":
        selected_level = request.form.get("Level")
        if selected_level == "Under Graduate":
            return redirect(url_for("undergraduate"))
        elif selected_level == "Post Graduate":
            return redirect(url_for("postgraduate"))
        else:
            flash("Please select a course level.", "error")
    return render_template("course_level.html")

# Route for undergraduate page
@app.route("/index.html")
def undergraduate_page():
    return render_template("index.html")

# Route for postgraduate page
@app.route("/indexpg.html")
def postgraduate_page():
    return render_template("indexpg.html")

# Define your course data
course_data = {
    "Computer Science & Engineering": {
        "image": "https://via.placeholder.com/600x300?text=CSE",
        "introduction": "Computer Science & Engineering focuses on designing, developing, and maintaining software and hardware systems.",
        "coreSubjects": ["Programming Languages", "Data Structures", "Operating Systems", "Computer Networks", "Software Engineering"],
        "careerOpportunities": "Software Developer, Systems Analyst, Network Engineer, AI Specialist, IT Consultant.",
        "averageSalary": "$60,000 - $120,000 per year",
        "analysisPage": "/dashboardCS.html"
    },
   "Computer Science & Engineering (Data Science)": {
        "image": "https://via.placeholder.com/600x300?text=Data+Science",
        "introduction": "This specialization focuses on data analysis, machine learning, and building predictive models.",
        "coreSubjects": ["Machine Learning", "Big Data Analytics", "Database Management", "Data Visualization", "Statistics"],
        "careerOpportnities": "Data Scientist, Data Analyst, Business Analyst, Machine Learning Engineer.",
        "averageSalary": "$70,000 - $140,000 per year",
        "analysisPage": "/dashboardCSDS.html"
      },
     "Computer Science & Design": {
        "image": "https://via.placeholder.com/600x300?text=CS+Design",
        "introduction": "Combining technical computer science skills with design principles to create user-centric systems.",
        "coreSubjects": ["Human-Computer Interaction", "UI/UX Design", "Visual Design", "Web Development", "Multimedia Computing"],
        "careerOpportunities": "UI/UX Designer, Web Developer, Digital Product Designer.",
        "averageSalary": "$55,000 - $100,000 per year",
        "analysisPage":"/dashboardCS&D.html"
      },
      "Computer Science & Business System": {
        "image": "https://via.placeholder.com/600x300?text=CSBS",
        "introduction": "This program blends computer science and business knowledge to develop software systems for enterprises.",
        "coreSubjects": ["Business Analytics", "Enterprise Resource Planning", "Database Systems", "Software Engineering"],
        "careerOpportunities": "Business Analyst, ERP Consultant, IT Manager, Product Manager.",
        "averageSalary": "$65,000 - $110,000 per year",
        "analysisPage": "/dashboardCSBS.html"
      },
      "Information Science": {
        "image": "https://via.placeholder.com/600x300?text=IS",
        "introduction": "Information Science focuses on managing and processing information for effective decision-making.",
        "coreSubjects": ["Information Retrieval", "Database Management", "Data Structures", "Software Design"],
        "careerOpportunities": "Data Analyst, IT Consultant, System Administrator.",
        "averageSalary": "$55,000 - $100,000 per year",
        "analysisPage": "/dashboardIS.html"
      },
      "Artificial Intelligence And Machine Learning": {
        "image": "https://via.placeholder.com/600x300?text=AI+ML",
        "introduction": "Specialization in building systems capable of intelligent behavior and learning.",
        "coreSubjects": ["Deep Learning", "Natural Language Processing", "Robotics", "Mathematical Foundations"],
        "careerOpportunities": "AI Engineer, Data Scientist, Robotics Engineer.",
        "averageSalary": "$75,000 - $150,000 per year",
        "analysisPage": "/dashboardAI.html"
      },
      "Mechanical Engineering": {
        "image": "https://via.placeholder.com/600x300?text=ME",
        "introduction": "Mechanical Engineering deals with the design, manufacturing, and operation of machinery.",
        "coreSubjects": ["Thermodynamics", "Fluid Mechanics", "Machine Design", "CAD/CAM"],
        "careerOpportunities": "Mechanical Engineer, Automotive Engineer, Robotics Engineer.",
        "averageSalary": "$50,000 - $90,000 per year",
        "analysisPage": "/dashboardMech.html"
      },
      "Civil Engineering": {
        "image": "https://via.placeholder.com/600x300?text=CE",
        "introduction": "Civil Engineering involves designing, constructing, and maintaining infrastructure projects.",
        "coreSubjects": ["Structural Analysis", "Construction Materials", "Hydraulics", "Geotechnical Engineering"],
        "careerOpportunities": "Civil Engineer, Structural Engineer, Project Manager.",
        "averageSalary": "$50,000 - $85,000 per year",
        "analysisPage": "/dashboardCivil.html"
      },
      "Textile Technology": {
        "image": "https://via.placeholder.com/600x300?text=Textile",
        "introduction": "Textile Technology focuses on fiber production, fabric design, and the creation of textile-based products.",
        "coreSubjects": ["Polymer Chemistry", "Fiber Technology", "Textile Manufacturing"],
        "careerOpportunities": "Textile Engineer, Quality Control Manager.",
        "averageSalary": "$40,000 - $70,000 per year",
        "analysisPage":"/dashboardTXT.html"
      },
      "Chemical Engineering": {
        "image": "https://via.placeholder.com/600x300?text=Chemical",
        "introduction": "Chemical Engineering deals with the development and operation of chemical processes.",
        "coreSubjects": ["Thermodynamics", "Process Design", "Chemical Kinetics"],
        "careerOpportunities": "Chemical Engineer, Process Engineer.",
        "averageSalary": "$55,000 - $95,000 per year",
        "analysisPage": "/dashboardChem.html"
      },
      "Electrical & Electronic Engineering": {
        "image": "https://via.placeholder.com/600x300?text=EEE",
        "introduction": "Electrical & Electronic Engineering focuses on designing and maintaining electrical systems.",
        "coreSubjects": ["Circuit Design", "Power Systems", "Control Systems"],
        "careerOpportunities": "Electrical Engineer, Power Systems Engineer.",
        "averageSalary": "$55,000 - $100,000 per year",
        "analysisPage": "/dashboardEEE.html"
      },
      "Electronics & Communication Engineering": {
        "image": "https://via.placeholder.com/600x300?text=ECE",
        "introduction": "This branch focuses on electronic devices, circuits, and communication systems.",
        "coreSubjects": ["Digital Signal Processing", "Embedded Systems"],
        "careerOpportunities": "Electronics Engineer.",
        "averageSalary": "$60,000 - $110,000 per year",
        "analysisPage": "/dashboardEC.html"
      },
      "Aerospace Engineering": {
        "image": "https://via.placeholder.com/600x300?text=Aerospace",
        "introduction": "Aerospace Engineering deals with aircraft and spacecraft development.",
        "coreSubjects": ["Aerodynamics", "Propulsion Systems"],
        "careerOpportunities": "Aerospace Engineer.",
        "averageSalary": "$70,000 - $130,000 per year",
        "analysisPage": "/dashboardAero.html"
      }

}

# Route for the details page
@app.route('/details')
def course_details():
    discipline = request.args.get('discipline')

    # Debug line to check discipline
    print(f"Discipline: {discipline}") 

    if discipline and discipline in course_data:
        course = course_data[discipline]
        # Debug line to check course data
        print(f"Course: {course}") 
        return render_template('details.html', course_name=discipline, course=course)
    else:
        return "Course not found!", 404

# Sample data for courses
courses_data = {
    "Master of Computer Applications (MCA)": {
        "image": "https://via.placeholder.com/400?text=MCA",
        "introduction": "MCA is a postgraduate degree that focuses on the latest trends in computer science and software engineering.",
        "coreSubjects": ["Programming in C", "Data Structures", "Software Engineering", "Database Management Systems", "Networking"],
        "careerOpportunities": "As an MCA graduate, you can work as a software developer, system architect, database administrator, or network engineer.",
        "averageSalary": "$60,000 - $90,000 per year",
        "analysisPage": "/dashboardMCA.html"
    },
    "Master of Business Administration (MBA)": {
        "image": "https://via.placeholder.com/400?text=MBA",
        "introduction": "MBA is a professional degree that provides students with knowledge and skills in business management and leadership.",
        "coreSubjects": ["Marketing Management", "Financial Accounting", "Human Resource Management", "Business Analytics", "Operations Management"],
        "careerOpportunities": "MBA graduates often pursue careers as business analysts, operations managers, marketing managers, and entrepreneurs.",
        "averageSalary": "$80,000 - $150,000 per year",
        "analysisPage": "/dashboardMBA.html"
    },
    "Master of Technology (MTech)": {
        "image": "https://via.placeholder.com/400?text=MTech",
        "introduction": "MTech is a specialized postgraduate degree focusing on advanced technology and engineering fields.",
        "coreSubjects": ["Advanced Data Structures", "Machine Learning", "Cloud Computing", "Blockchain", "IoT"],
        "careerOpportunities": "MTech graduates can pursue careers as software engineers, data scientists, system architects, and research and development professionals.",
        "averageSalary": "$70,000 - $120,000 per year",
        "analysisPage": "/dashboardMTECH.html"
    }
}

@app.route('/')
def indexpg():
    return render_template('indexpg.html')  # Assuming your main program selection page is indexpg.html

@app.route('/detailspg')
def details():
    course_name = request.args.get('discipline')
    course = courses_data.get(course_name, None)
    
    if course is None:
        return "Course not found", 404

    return render_template('detailspg.html', course_name=course_name, course=course)

@app.route('/<analysis_page>')
def analysis_page(analysis_page):
    return render_template(analysis_page)


if __name__ == '__main__':
    app.run(debug=True)
  