from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Success! Welcome to this web app."

port = int(os.environ.get("PORT", 33507))
app.run(host='0.0.0.0', port=port)