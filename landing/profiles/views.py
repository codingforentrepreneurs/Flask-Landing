from flask import render_template
from landing import app

@app.route("/users/<username>/")
def profile_detail(username):
    return "<h1>Hello {username}</h1>".format(username=username)


@app.route("/users/")
def profiles_list():
    return render_template('profiles_list.html')