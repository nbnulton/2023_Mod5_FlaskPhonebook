# makes sure users are giving us the correct information
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class UserLoginForm(FlaskForm):
    # makes sure that for the email that it's a string input, 
    # then makes sure that they give us that data in an email format
    email = StringField('Email', validators = [DataRequired(), Email()])
    # adds the asterisk or dots when password is being typed out
    password = PasswordField('Password', validators = [DataRequired()])
    # inside the forms.html
    submit_button = SubmitField()











