from flask_wtf import FlaskForm
from wtforms import StringField


class LandingForm(FlaskForm):
    full_name = StringField('Full name')
    email = StringField('Email')

