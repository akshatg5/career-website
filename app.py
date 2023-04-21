from flask import Flask,render_template,jsonify

app = Flask(__name__)  # creating a Flask application

JOBS = [
    {
        'id' : 1,
        'title': 'Data Analyst',
        'location' : 'Bengaluru, India',
        'salary' : 1000000,
    },
    {
        'id' : 2,
        'title': 'Data Scientist',
        'location': 'Delhi, India',
        'salary' : 1500000,
    },
    {
        'id' : 3,
        'title': 'Front End Engineer',
        'location': 'Remote',
    },
    {
        'id' : 4,
        'title': 'Back End Engineer',
        'location': 'London,UK',
        'salary' : 5000000,
    },  
]

@app.route("/")
def hello_world():
    return render_template('home.html',jobs = JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(debug=True)