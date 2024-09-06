from flask import Blueprint, render_template, request
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash

from ..db import db
from .forms import RegisterForm
from .models import UserModel

bp = Blueprint("users", __name__, url_prefix="/auth")


@bp.route("/login")
def login():
    return "login"


@bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():

        print("Email:", form.email.data)
        print("Password:", form.password1.data)

        try:
            user = UserModel(
                email=form.email.data,
                password=generate_password_hash(form.password1.data),
            )
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            form.email.errors.append("User with that email already exists")

    return render_template("register.html", form=form)
