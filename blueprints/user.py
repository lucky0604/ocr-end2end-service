from flask import Blueprint, Response, request, jsonify
from database.exts import db
from database import models

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