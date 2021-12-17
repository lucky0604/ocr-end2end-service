from flask import Flask
from blueprints.user import users
from database import config
from database.exts import db

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

app.register_blueprint(users)



app.run()