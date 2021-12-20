from database.base_model import EntityBase
from .exts import db
from .base_model import EntityBase
from flask_bcrypt import generate_password_hash, check_password_hash

class User(db.Model, EntityBase):
	__tablename__ = "movie_user"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, unique=True)
	casts = db.Column(db.String)
	generes = db.Column(db.String)

class Account(db.Model, EntityBase):
	__tablename__ = "movie_table"
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String, unique=True)
	password = db.Column(db.String, unique=True)

	def hash_password(self):
		self.password = generate_password_hash(self.password).decode("utf8")

	def check_password(self, password):
		return check_password_hash(self.password, password)