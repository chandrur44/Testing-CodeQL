import os
import sqlite3
import subprocess
import ipaddress
from flask import Flask, request, abort

app = Flask(__name__)


@app.route("/user")
def get_user():
    user_id = request.args.get("id", type=int)
    if user_id is None:
        abort(400, "id must be an integer")
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, email FROM users WHERE id = ?", (user_id,))
    return str(cursor.fetchone())


@app.route("/ping")
def ping():
    host = request.args.get("host", "")
    try:
        ipaddress.ip_address(host)
    except ValueError:
        abort(400, "host must be a valid IP address")
    result = subprocess.check_output(
        ["ping", "-c", "1", host],
        shell=False,
        timeout=5,
    )
    return result


if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG") == "1")
