from flask import request, Response
from database.models import Account
from flask_restful import Resource
from database.exts import db
from flask_jwt_extended import create_access_token
import datetime

class SignupApi(Resource):

	def post(self):
		body = request.get_json()
		account = Account(**body)
		account.hash_password()
		db.session.add(account)
		db.session.commit()
		return account.to_json(), 200

class LoginApi(Resource):

	def post(self):
		body = request.get_json()
		account = Account.query.filter_by(email=body["email"]).first()
		authorized = account.check_password(body["password"])
		if not authorized:
			return {"error": "not authorized"}, 401
		expires = datetime.timedelta(days = 7)
		access_token = create_access_token(identity=str(account.id), expires_delta=expires)
		return {"token": access_token}, 200