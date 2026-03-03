import psycopg2
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

DB_CONFIG = {
    "host": "localhost",
    "port": 10503,
    "dbname": "dhg503",
    "user": "student",
    "password": "student",
}


@app.get("/", response_class=HTMLResponse)
def root():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute("SELECT id, name, major, year FROM students ORDER BY id;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    table_rows = ""
    for row in rows:
        table_rows += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td>{row[3]}</td></tr>"

    return f"""
    <html>
    <head>
        <title>DHG503 Students</title>
        <style>
            body {{ font-family: sans-serif; max-width: 600px; margin: 40px auto; }}
            h1 {{ color: #333; }}
            table {{ border-collapse: collapse; width: 100%; }}
            th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
            th {{ background-color: #4a7c59; color: white; }}
            tr:nth-child(even) {{ background-color: #f2f2f2; }}
        </style>
    </head>
    <body>
        <h1>DHG503 Students</h1>
        <table>
            <tr><th>ID</th><th>Name</th><th>Major</th><th>Year</th></tr>
            {table_rows}
        </table>
    </body>
    </html>
    """
