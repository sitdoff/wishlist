from environs import Env
from flask import Flask, redirect, render_template, url_for
from flask.logging import create_logger
from flask_migrate import Migrate

from .db import db
from .users import users
from .wishlist import wishlist

env = Env()
env.read_env()


def create_app():
    app = Flask(__name__)
    app.config.from_object(env("APP_SETTINGS"))

    app.register_blueprint(wishlist.bp)
    app.register_blueprint(users.bp)

    db.init_app(app)

    migrate = Migrate(app, db)

    return app


app = create_app()

logger = create_logger(app)


@app.route("/")
def main():
    return redirect(url_for("wishlist.main"))
