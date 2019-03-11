import json
from flask import render_template, request, redirect
from landing import app

from .forms import LandingForm
from .models import EmailSignup

@app.route("/", methods=['GET', 'POST'])
def home():
    form = LandingForm()
    if form.validate_on_submit():
        # print(form.full_name.data)
        # print(form.email.data)
        data = form.data
        if 'csrf_token' in data:
            del data['csrf_token']
        obj = EmailSignup.query.filter_by(email=form.email.data).first()
        if obj is None:
            obj = EmailSignup(**data) #(full_name=, email=)
            obj.save()
        #form = LandingForm()
        #return render_template('home.html', form=form)
        return redirect("/item/{}".format(obj.id))
        # send email -> via flask and smtp
        # create txt doc
        # create csv doc
        # send webhook -> zapier -> google docs
        # save into database -> sqlite -> mysql / postgresql
    return render_template('home.html', form=form)

'''
create email obj instance via form
saved in database
in database, we have objects with ids in models.py
ids == primary keys
primary keys to lookup in database
use dynamic url routing to lookup object in database
'''

@app.route("/item/<int:id>/", methods=['GET'])
def item_detail(id):
    # instance = EmailSignup.query.get(id)
    instance = EmailSignup.query.filter_by(id=id).first_or_404()
    return render_template('items/detail.html', instance=instance)


@app.route("/item/<int:id>/update/", methods=['GET', 'POST'])
def item_update(id):
    # instance = EmailSignup.query.get(id)
    instance = EmailSignup.query.filter_by(id=id).first_or_404()
    # instance.full_name -> form.full_name
    # instance.email -> form.email
    form = LandingForm(obj=instance)
    if form.validate_on_submit():
        data = form.data
        print(data)
    return render_template('items/form.html', instance=instance, form=form)




@app.route("/item/<int:id>/update/", methods=['GET', 'POST'])
def item_delete(id):
    # instance = EmailSignup.query.get(id)
    instance = EmailSignup.query.filter_by(id=id).first_or_404()
    # form
    return render_template('items/detail.html', instance=instance)








