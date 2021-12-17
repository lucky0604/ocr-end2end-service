from flask import Flask
from flask_restful import Api
from routes import init_routes
from database import config
from database.exts import db

app = Flask(__name__)
api = Api(app)

app.config.from_object(config)
db.init_app(app)

init_routes(api)
app.run()