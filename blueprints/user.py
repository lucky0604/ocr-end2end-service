from flask import Response, request
from flask.json import jsonify
from flask_restful import Resource
from database.exts import db
from database import models
from flask_jwt_extended import jwt_required, get_jwt_identity
'''
users = Blueprint("users", __name__)

@users.route("/movies")
def get_movies():
	movies = models.User.query.all()
	output = []
	for movie in movies:
		output.append(movie.to_json())
	return jsonify(output), "200"

@users.route("/movies", methods=["POST"])
def add_movie():
	body = request.get_json()
	db.session.add(models.User(name=str(body['name']), casts=str(body['casts']), generes=str(body['generes'])))
	db.session.commit()
	return Response("success", mimetype="application/json", status=200)
'''

class UsersApi(Resource):

	def get(self):
		movies = models.User.query.all()
		output = []
		for movie in movies:
			output.append(movie.to_json())
		return {"data": output}, 200

	@jwt_required()
	def post(self):
		account_id = get_jwt_identity()
		print(account_id)
		body = request.get_json()
		db.session.add(models.User(name=str(body['name']), casts=str(body['casts']), generes=str(body['generes'])))
		db.session.commit()
		return Response("success", mimetype="application/json", status=200)