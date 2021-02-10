from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, Length

class Login(FlaskForm):
	username = StringField("Username", validators=[InputRequired(), Length(min=4, max=32)], render_kw={"class":"form-control"})
	password = PasswordField("Password", validators=[InputRequired()], render_kw={"class":"form-control"})

class Register(FlaskForm):
	username = StringField("Username", validators=[InputRequired(), Length(min=4, max=32)], render_kw={"class":"form-control"})
	email = EmailField("Email", validators=[InputRequired()], render_kw={"class":"form-control"})
	password = PasswordField("Password", validators=[InputRequired()], render_kw={"class":"form-control"})
	confirm_password = PasswordField("Confirm password", validators=[InputRequired()], render_kw={"class":"form-control"})