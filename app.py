from flask import Flask

import admin
import api
import front

from extensions import db, migrate
from config import Config

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app, db)

import models

app.register_blueprint(admin.admin_bp, url_prefix='/admin')
app.register_blueprint(api.api_bp, url_prefix='/api')
app.register_blueprint(front.front_bp, url_prefix='/')

if __name__ == '__main__':
    app.run()
