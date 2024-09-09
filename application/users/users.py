from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_user, logout_user
from sqlalchemy.exc import IntegrityError
from werkzeug.security import check_password_hash, generate_password_hash

from ..db import db
from .forms import LoginForm, RegisterForm
from .models import UserModel

bp = Blueprint("users", __name__, url_prefix="/auth")


@bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = UserModel.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for("wishlist.main"))
        else:
            flash("Wrong email or password. Please try again", "alert alert-danger")
            return redirect(url_for("users.login"))

    return render_template("login.html", form=form)


@bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        try:
            user = UserModel(
                email=form.email.data,
                password=generate_password_hash(form.password1.data),
            )
            db.session.add(user)
            db.session.commit()
            login_user(user)
            flash("Successfully registered. Thanks!", "alert alert-success")
            return redirect(url_for("wishlist.main"))

        except IntegrityError:
            form.email.errors.append("User with that email already exists")

    return render_template("register.html", form=form)


@bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("users.login"))
