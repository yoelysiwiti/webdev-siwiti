from flask import Flask

app = Flask(__name__)

print("Siwiti, this is app.py")

@app.route("/")
def home():
    return "Hello from Render Flask app!"