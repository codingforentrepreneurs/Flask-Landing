from flask_wtf import FlaskForm
from wtforms import StringField, validators, ValidationError

from .models import EmailSignup

class LandingForm(FlaskForm):
    full_name = StringField('Full name', 
        render_kw={"class": "form-control", 
            "placeholder": "Full name"},
        validators=[
            validators.DataRequired(
                    message='You full name is required'
            )
        ])
    email = StringField('Email', 
        render_kw={"class": "form-control", 
            "placeholder": "Your email"},
        validators=[
            validators.DataRequired(
                    message='You email is required'
            ),
            validators.Email()
        ])

    def validate_email(self, field):
        if field.data.endswith(".edu"):
            raise ValidationError('You cannot use a school email address.')
        obj = EmailSignup.query.filter_by(email=field.data).first()
        if obj is not None:
            msg = 'This email has already been added.'
            raise ValidationError(msg)
