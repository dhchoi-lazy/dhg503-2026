import psycopg2
from fastapi import FastAPI

app = FastAPI()

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "dhg503",
    "user": "student",
    "password": "student",
}


@app.get("/")
def root():
    return {"message": "Hello DHG503!"}


@app.get("/db")
def check_db():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute("SELECT version();")
    version = cur.fetchone()[0]
    cur.close()
    conn.close()
    return {"postgres_version": version}
