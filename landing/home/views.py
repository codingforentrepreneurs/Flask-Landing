import json
from flask import render_template, request
from landing import app


@app.route("/", methods=['GET', 'POST'])
def home():
    # CSRF -> My app doesn't allow your app to send data
    # http methods
    #print(request.data) # json
    #print(request.form) # html form
    if request.method == "POST":
        # print(request.data)
        print()
        data = request.stream.read().decode('utf-8')
        print(data) 
        final_data = json.loads(data)
        print(final_data['hello'])
        # eval() -> potentially harmful

    return render_template('home.html')