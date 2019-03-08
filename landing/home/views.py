from flask import render_template, request
from landing import app


@app.route("/", methods=['GET', 'POST'])
def home():
    # http methods
    print(request.data) # json
    print(request.form) # html form
    return render_template('home.html')