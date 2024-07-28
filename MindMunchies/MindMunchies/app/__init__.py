from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_babel import Babel
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
babel = Babel()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    babel.init_app(app)
    migrate.init_app(app, db)

    login_manager.login_view = 'main.login'

    from app.routes import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/')

    return app

from app.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
