from flask import Flask

app = Flask(__name__)

@app.route("/")

def create_form():
    print("My name is yoeli siwiti, the king of the jungle")

def home():
    create_form()
    return "Hello from Render Flask app!"
home()