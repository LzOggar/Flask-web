from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from app import db

class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(32), unique=True, nullable=False)
	password = db.Column(db.String(), nullable=False)
	email = db.Column(db.String(), nullable=False)

	def __repr__(self):
		return "<User {}>".format(self.username)

	def set_password(self, password):
		self.password = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password, password)