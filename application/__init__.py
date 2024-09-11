from environs import Env
from flask import Flask, redirect, render_template, url_for
from flask.logging import create_logger
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_wtf import CSRFProtect

from .db import db
from .users import routes as users_routes
from .users.models import UserModel
from .wishlist import routes as wishlist_routes

env = Env()
env.read_env()


def create_app():
    app = Flask(__name__)
    app.config.from_object(env("APP_SETTINGS"))

    app.register_blueprint(wishlist_routes.bp)
    app.register_blueprint(users_routes.bp)

    db.init_app(app)

    migrate = Migrate(app, db)

    csrf = CSRFProtect(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "users.login"
    login_manager.login_message = None

    @login_manager.user_loader
    def load_user(user_id):
        return UserModel.query.get(user_id)

    return app


app = create_app()

logger = create_logger(app)


@app.route("/")
def main():
    return redirect(url_for("wishlist.main"))
