from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<html><body><h1>Alô!! Esta é a nossa primeira APP na Azure!</h1></body></html>\n"
