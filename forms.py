from flask_wtf import Form
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import (DataRequired, Regexp, ValidationError, Email,
								Length, EqualTo)

class LoginForm(Form):
	email = StringField('Username:', validators=[DataRequired()], default="mike@dbtests.info")
	password = PasswordField('Password:', validators=[DataRequired()])

class Register(Form):
	username = StringField('Username:', validators=[DataRequired()], default="mike@dbtests.info")
	firstname = StringField('First Name:', validators=[DataRequired()], default="Mike")
	surname = StringField('Surname:', validators=[DataRequired()], default="McMahon")