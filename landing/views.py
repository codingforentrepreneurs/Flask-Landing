from landing import app

@app.route("/")
def hello():
    return "<h1>Hello World</h1>"

@app.route("/contact-us/")
def contact_us():
    return "<h1>Contact Us</h1>"

@app.route("/about-us/")
def about_us():
    return "<h1>About Us</h1>"


