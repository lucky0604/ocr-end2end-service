from flask import Flask
from flask_restful import Api
from routes import init_routes
from database import config
from database.exts import db
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_envvar("ENV_FILE_LOCATION")

api = Api(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

app.config.from_object(config)
db.init_app(app)

init_routes(api)
app.run()