from environs import Env
from flask import Flask, redirect, render_template, url_for
from flask.logging import create_logger

from application.wishlist import wishlist
from application.wishlist.models import ItemModel, db

env = Env()
env.read_env()


def create_app():
    app = Flask(__name__)
    app.config.from_object(env("APP_SETTINGS"))

    db.init_app(app)
    with app.test_request_context():
        db.create_all()

    return app


app = create_app()
app.register_blueprint(wishlist.bp)

logger = create_logger(app)


@app.route("/")
def main():
    return redirect(url_for("wishlist.main"))
