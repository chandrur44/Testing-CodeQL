import sqlite3
import subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route("/user")
def get_user():
    user_id = request.args.get("id")
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT name, email FROM users WHERE id = " + user_id
    cursor.execute(query)
    return str(cursor.fetchone())


@app.route("/ping")
def ping():
    host = request.args.get("host")
    result = subprocess.check_output("ping -c 1 " + host, shell=True)
    return result


if __name__ == "__main__":
    app.run(debug=True)
