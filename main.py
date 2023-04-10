# print("Hello world")
# print(__name__)

from flask import Flask, render_template, jsonify
from database import load_jobs_from_db

# JOBS = [
#   {
#     'id': 1,
#     'title': 'Data Analyst',
#     'location': 'Toronto, Canada',
#     'salary': 'CAD 100000$'
#   },
#   {
#     'id': 2,
#     'title': 'Data Scientist',
#     'location': 'Brampton, Canada',
#     'salary': 'CAD 150000$'
#   },
#   {
#     'id': 3,
#     'title': 'Data Engineer',
#     'location': 'Scarbrough, Canada',
#     'salary': 'CAD 200000$'
#   },
#   {
#     'id': 4,
#     'title': 'Full-Stack Developer',
#     'location': 'Remote',
#     'salary': 'CAD 170000$'
#   }
# ]




app = Flask(__name__)

@app.route("/")
def hello_world():
  jobs = load_jobs_from_db()
  return render_template('home.html', jobs=jobs, company_name='Niharika')
  #  ##### jobs=jobs -->  first_jobs=second_jobs --> first_jobs = HTML, second_jobs = return's function load_jobs_from_db() in main.app 

@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)