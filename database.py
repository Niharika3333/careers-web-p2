# import sqlalchemy
# pip install sqlalchemy

from sqlalchemy import create_engine, text
import os

# print(sqlalchemy.__version__)

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
      # "cert": "/home/gord/client-ssl/client-cert.pem",
      # "key": "/home/gord/client-ssl/client-key.pem"
    }
  })


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._asdict())
    return jobs


def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text(f"SELECT * FROM jobs WHERE id={id}"))
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return rows[0]._asdict()


def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    job_id = job_id
    full_name = data['full_name']
    email = data['email']
    linkedin_url = data['linkedin_url']
    education = data['education']
    work_experience = data['work_experience']
    resume_url = data['resume_url']
    
    query = text(
      f"INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES('{job_id}', '{full_name}', '{email}', '{linkedin_url}', '{education}', '{work_experience}', '{resume_url}')")

    conn.execute(query)

       # query = text(
    #   "INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES(:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")

    # conn.execute(query,
    #              job_id=job_id,
    #              full_name=data['full_name'],
    #              email=data['email'],
    #              linkedin_url=data['linkedin_url'],
    #              education=data['education'],
    #              work_experience=data['work_experience'],
    #              resume_url=data['resume_url'])














# # pip install pymysql
# # we have created engine. and connected it with planetscale.
# # Next step would be to get some information out of the engine.

# with engine.connect() as conn:
#   result = conn.execute(text("select * from jobs"))

#   result_dicts = []
#   for row in result.all():
#     result_dicts.append(row._asdict())

#   print(result_dicts)

# # print("result: ", result)
# # print("type(result): ", type(result))

# result_all = result.all()
# # print("result.all(): ", result_all)
# # print("type(result.all()): ", type(result_all))

# first_result = result_all[0]
# # print("first_result: ", first_result)

# print("type(first_result): ", type(first_result))
# # #### output == type(first_result):  <class 'sqlalchemy.engine.row.Row'>

# # #### dict(first_result) and first_result.__dict__ did not worked

# first_result_dict = first_result._asdict()
# print("type(first_result_dict): ", type(first_result_dict))
# # #### output == type(first_result_dict):  <class 'dict'>

# # print("first_result_dict: ", first_result_dict)
