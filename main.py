# print("Hello world")
# print(__name__)

from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db

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


# @app.route("/job/<id>")
# def show_job(id):
#   job = load_job_from_db(id)
#   return(jsonify(job))


@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)
  if not job:
    return "Not Found", 404
  return render_template('jobpage.html', job=job)

@app.route("/api/job/<id>")
def show_job_json(id):
  job = load_job_from_db(id)
  return jsonify(job)


@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
  data = request.form
  # data = request.args ## when you post data, data is present in request.form
  # store this in db # send an email # display an acknowledgement
  ### return jsonify(data)
  job = load_job_from_db(id)

  add_application_to_db(id, data)

  return render_template('application_submitted.html',
                         application=data,
                         job=job)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
