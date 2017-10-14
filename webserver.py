"""
webserver.py

File that is the central location of code for your webserver.
"""

from flask import Flask, render_template, request
import os
import requests

# Create application, and point static path (where static resources like images, css, and js files are stored) to the
# "static folder"
app = Flask(__name__,static_url_path="/static")

@app.route('/')
def redirect():
    return render_template("homepage.html") 

@app.route('/index')
def home():
    return render_template("homepage.html") # Render the template located in "templates/index.html"


@app.route('/about')
def about():
    return render_template("aboutus.html")

@app.route('/contact',methods=['GET'])
def contact_display():
    return render_template("contactus.html",notifications=[])


@app.route('/contact',methods=['POST'])
def contact_post():
    message = request.form.get("message")
    name = request.form.get("name")
    subject = request.form.get("subject")
    email = request.form.get("email")
    notifications=[]
    data = {
        'from': email,
        'to': os.environ["INFO253_MAILGUN_TO_EMAIL"],
        'subject': "You just got a new message",
        'text': message
    }
    auth = (os.environ["INFO253_MAILGUN_USER"], os.environ["INFO253_MAILGUN_PASSWORD"])
    r = requests.post(
        'https://api.mailgun.net/v3/{}/messages'.format(os.environ["INFO253_MAILGUN_DOMAIN"]),auth=auth,data=data)
    if r.status_code == requests.codes.ok:
        name = "Hi "+name+", you message has been sent"
    else:
        name ="Email has not been set."
    notifications.append(name)
    return render_template("contactus.html",notifications=notifications)


@app.route('/blog/8-experiments-in-motivation')
def blog1():
    return render_template("blog1.html")

@app.route('/blog/a-mindful-shift-of-focus')
def blog2():
    return render_template("blog2.html")

@app.route('/blog/how-to-develop-an-awesome-sense-of-direction')
def blog3():
    return render_template("blog3.html")

@app.route('/blog/training-to-be-a-good-writer')
def blog4():
    return render_template("blog4.html")

@app.route('/blog/what-productivity-systems-wont-solve')
def blog5():
    return render_template("blog5.html")





"""
@app.route('/')
def quote_of_the_day():
  day_of_week = request.args.get('day_of_week', 'sunday')
  return render_template(
    "index.html",
    day=day_of_week,
    quote=quote_db[day_of_week])

@app.route('/',methods=['POST'])
def return_quoto():
  day_of_week = request.form.get('day_of_week', 'sunday')
  return render_template(
    "index.html",
    day=day_of_week,
    quote=quote_db[day_of_week])
    """