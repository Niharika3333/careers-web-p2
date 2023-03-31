# print("Hello world")
# print(__name__)

from flask import Flask, render_template, jsonify

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Toronto, Canada',
    'salary': 'CAD 100000$'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Brampton, Canada',
    'salary': 'CAD 150000$'
  },
  {
    'id': 3,
    'title': 'Data Engineer',
    'location': 'Scarbrough, Canada',
    'salary': 'CAD 200000$'
  },
  {
    'id': 4,
    'title': 'Full-Stack Developer',
    'location': 'Remote',
    'salary': 'CAD 170000$'
  }
]


app = Flask(__name__)

@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Niharika')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)