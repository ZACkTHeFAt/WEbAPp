# from flask import Flask
# import os

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Success! Welcome to this web app."

# port = int(os.environ.get("PORT", 33507))
# app.run(host='0.0.0.0', port=port)

from emailer import send_email
from urllib import parse

class EmailData:
    from_name = ""
    about_name = ""
    to_name = ""
    to_address = ""
    occasion = ""
    location = ""
    favorite_thing = ""
    about_names = ""

    def __init__(self,from_name,about_name,to_name,to_address,occasion,location,favorite_thing,about_names):
        self.from_name = from_name
        self.about_name = about_name
        self.to_name = to_name
        self.to_address = to_address
        self.occasion = occasion
        self.location = location
        self.favorite_thing = favorite_thing
        self.about_names = about_names
        


info1 = EmailData('Blusette','Blusette','Zackary, Archer, Zander, Nick, Len, Abigale, Lucca, and Tara','zacke69420@gmail.com','Washington DC Party','Blusettes House','staying up all night long','we all')
info2 = EmailData('Nick','Nick','Zackary, Archer, Zander, Blusette, Len, Abigale, Lucca, and Tara','zacke69420@gmail.com','Washington DC Party','Nicks House','having a fun time','we all')
info3 = EmailData('Len','Len','Zackary, Archer, Zander, Nick, Nick, Abigale, Lucca, and Tara','zacke69420@gmail.com','Washington DC Party','Lens House','hanging out with each other','we all')
info4 = EmailData('Abigale','Abigale','Zackary, Archer, Zander, Nick, Len, Len, Lucca, and Tara','zacke69420@gmail.com','Washington DC Party', 'Abigales House','playing games with each other','we all')

info_list = [info1,info2,info3,info4]

message_template = """
Hi {to_name},

I would like to invite you to {about_name}'s {occasion}! We will be celebrating at {location} because, as you know, {about_names} like {favorite_thing}. Click the link to register today :) http://127.0.0.1:5000/click/{link}

Best wishes, {from_name}
"""

subject_template = "Hi {to_name}! You're invited..."

for info in info_list:
    the_link = parse.quote(info.to_name)
    message = message_template.format(
                              to_name = info.to_name,
                              about_name = info.about_name,
                              occasion = info.occasion,
                              location = info.location,
                              favorite_thing = info.favorite_thing,
                              from_name = info.from_name,
                              about_names = info.about_names,
                              link = the_link
                              )
    subject = subject_template.format(
                                      to_name = info.to_name
                                      )
    send_email(
               info.to_address,
               message,
               subject
               )
