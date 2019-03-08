from flask_wtf import FlaskForm
from wtforms import StringField, validators

class LandingForm(FlaskForm):
    full_name = StringField('Full name', validators=[
            validators.DataRequired(
                    message='You full name is required'
            )
        ])
    email = StringField('Email', validators=[
            validators.DataRequired(
                    message='You email is required'
            )
        ])

