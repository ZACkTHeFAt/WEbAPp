from emailer import send_email
from urllib import parse
from flask import Flask
import os

app = Flask(__name__)

@app.route("/emailzz")
def email():
	to_address = "zacke69420@gmail.com"
	message = "MALWARE BYTES FTW :)"
	subject = "MALWARE BYTES"
	send_email(
	to_address,
	message,
	subject
	)
	return "An email has been sent (I hope)"

@app.route("/minecraft")
def minecraft():
	to_address = "zacke69420@gmail.com"
	message = "{} IS THE BEST MINECRAFT CHARCATER EVER!!".format(os.environ.get('best_minecraft_character'))
	subject = "{}".format(os.environ.get('best_minecraft_character'))
	send_email(
	to_address,
	message,
	subject
	)
	return "CHECK UR EMAIL TO SEE WHO THE BEST MINECRAFT CHARACTER IS (IT'S {})".format(os.environ.get('best_minecraft_character'))


@app.route("/")
def home():
	print("Someone has visited our website! I hope I am looking at the logs right now...")
	return "Success! Welcome to this web app."

port = int(os.environ.get("PORT", 33507))
app.run(host='0.0.0.0', port=port)