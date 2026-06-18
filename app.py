from flask import Flask, request
from datetime import datetime
import os

app = Flask(__name__)

LOG_FILE = "ip_logs.txt"

@app.route("/")
def log_ip():
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    time = datetime.now()

    log_entry = f"{time} - {ip}\n"

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_entry)

    # No UI, just silent response
    return "", 204  # 204 = No Content

if __name__ == "__app__":
    app.run()
