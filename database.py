import os
from sqlalchemy import create_engine, text

DB_CONNECTION = os.environ['DB_CONNECTION_VARIABLE']

engine = create_engine(DB_CONNECTION,
                       connect_args={"ssl": {
                           "ssl_ca": "/etc/ssl/cert.pem"
                       }})

def load_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        all_results = result.all()
        jobs = []
        for job in all_results:
            jobs.append(job._mapping)

        return jobs

