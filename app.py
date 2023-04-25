from flask import Flask,render_template,jsonify
from sqlalchemy import create_engine,text
from database import load_jobs_from_db,load_job_from_db

app = Flask(__name__)  # creating a Flask application

# JOBS = [
#     {
#         'id' : 1,
#         'title': 'Data Analyst',
#         'location' : 'Bengaluru, India',
#         'salary' : 1000000,
#     },
#     {
#         'id' : 2,
#         'title': 'Data Scientist',
#         'location': 'Delhi, India',
#         'salary' : 1500000,
#     },
#     {
#         'id' : 3,
#         'title': 'Front End Engineer',
#         'location': 'Remote',
#     },
#     {
#         'id' : 4,
#         'title': 'Back End Engineer',
#         'location': 'London,UK',
#         'salary' : 5000000,
#     },  
# ]
@app.route("/")
def hello_world():
    jobs = load_jobs_from_db()
    return render_template('home.html',jobs = jobs)

@app.route("/api/jobs")
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)

#making another route to use the job id and pass it in the function
@app.route("/job/<id>") 
def show_jobs(id):
    job = load_job_from_db(id)
    if not job:
        return "Error:Not Found",404
    return render_template('jobpage.html',job=job)

if __name__ == "__main__":
    app.run(debug=True)