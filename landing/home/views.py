from flask import render_template
from landing import app


@app.route("/")
def home():
    return render_template('home.html')