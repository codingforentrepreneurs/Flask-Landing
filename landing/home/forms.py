from flask_wtf import FlaskForm
from wtforms import StringField, validators, ValidationError, HiddenField
from sqlalchemy import not_

from .models import EmailSignup

class LandingForm(FlaskForm):
    id = HiddenField('id')
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
        _id = self.data.get('id', -1) # -1 is not a valid id
        if field.data.endswith(".edu"):
            raise ValidationError('You cannot use a school email address.')
        not_query = not_(EmailSignup.id == _id)
        obj = EmailSignup.query.filter_by(email=field.data).filter(not_query).first()
        if obj is not None:
            msg = 'This email has already been added.'
            raise ValidationError(msg)
