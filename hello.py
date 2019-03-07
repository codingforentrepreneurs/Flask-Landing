from flask import Flask

app = Flask(__name__)

# url
# view

@app.route("/")
def hello():
    return "<h1>Hello World</h1>"

@app.route("/contact-us/")
def contact_us():
    return "<h1>Contact Us</h1>"

@app.route("/about-us/")
def about_us():
    return "<h1>About Us</h1>"


@app.route("/user/<username>/")
def profile(username):

    return "<h1>Hello {username}</h1>".format(username=username)

@app.route("/jobs/<job_id>/")
def jobs(job_id):
    # run job 12
    return "<h1>Hello {username}</h1>".format(username=username)


