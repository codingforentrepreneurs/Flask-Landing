from flask import render_template
from landing import app

@app.route("/users/<username>/")
def profile_detail(username):
    context = {"user": username}
    return render_template('profiles_detail.html', context=context, username=username, some_list=[12, 312, 12321])


@app.route("/users/")
def profiles_list():
    return render_template('profiles_list.html')