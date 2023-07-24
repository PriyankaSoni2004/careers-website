from sqlalchemy import create_engine, text


db_connection_string="mysql+pymysql://ue3agqwg8r9ly0gcs3x8:pscale_pw_HCObptGUSmJP1EXeyY7O5vLcKeByspVALGaTjCPEauH@aws.connect.psdb.cloud/joviancareers?charset=utf8mb4"


engine = create_engine(db_connection_string ,
  connect_args={
    "ssl" :{
      "ssl_ca":"/etc/ssl/cert.pem"
    }
  })

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs=[]
    for row in result.all():
      jobs.append(dict(row))
    return jobs

