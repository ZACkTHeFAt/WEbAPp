from emailer import send_email
from urllib import parse
from flask import Flask
import os

app = Flask(__name__)

@app.route("/emailzz")
def email():
	to_address = "zacke69420@gmail.com"
	message = "MALWARE BYTES :)"
	subject = "MALWARE"
	send_email(
	to_address,
	message,
	subject
	)
	return "An email has been sent (I think)"

@app.route("/")
def home():
	return "Success! Welcome to this web app."

port = int(os.environ.get("PORT", 33507))
app.run(host='0.0.0.0', port=port)