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
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._asdict())
    return jobs



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
