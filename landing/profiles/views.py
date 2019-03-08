from flask import render_template
from landing import app

@app.route("/users/<username>/")
def profiles_detail(username):
    context = {"user": username}
    if username == 'jmitchel3':
        context["right_user_msg"] = "Yeah that's right"
    return render_template('profiles_detail.html', context=context)


@app.route("/users/")
def profiles_list():
    return render_template('profiles_list.html')