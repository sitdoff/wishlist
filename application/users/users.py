from flask import Blueprint, render_template

bp = Blueprint("users", __name__, url_prefix="/auth")


@bp.route("/login")
def login():
    return "login"


@bp.route("/register")
def register():
    return "register"
