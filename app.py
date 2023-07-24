from sqlalchemy import create_engine, text


db_connection_string="mysql+pymysql://y8f8j8l7r0qym086yy8o:pscale_pw_ewf5HK7FQbclUxfTcalE3GCpb10rSK03CZ3jSOHRNP8@aws.connect.psdb.cloud/joviancareers?charset=utf8mb4"


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


sql