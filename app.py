from flask import Flask

app = Flask(__name__)

print("Siwiti, this is app.py")

@app.route("/")

<<<<<<< HEAD

def home():
    message =  "Hello from Render Flask app, the messages variable declaredSS";
    return message;
=======
def call_message();
    return "Hello from Render Flask app, the messages from call message()";
    
def home():
    call_message();
    return message;

>>>>>>> aa5bfb3f3f4d327ed4493420f44066d6421ecfe9
