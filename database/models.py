from database.base_model import EntityBase
from .exts import db
from .base_model import EntityBase

class User(db.Model, EntityBase):
	__tablename__ = "movie_user"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, unique=True)
	casts = db.Column(db.String)
	generes = db.Column(db.String)