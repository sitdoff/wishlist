from flask import Blueprint, request
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from werkzeug.security import check_password_hash, generate_password_hash

from ..db import db
from ..users.models import UserModel
from ..wishlist.models import ItemModel

bp = Blueprint("api", __name__, url_prefix="/api")


@bp.route("auth/register/", methods=["POST"])
def register():
    email = request.json.get("email")
    password = request.json.get("password")

    if all((email, password)):
        try:
            user = UserModel(
                email=email,
                password=generate_password_hash(password),
            )
            db.session.add(user)
            db.session.commit()
            return {"success": "User successfully created"}, 201

        except IntegrityError:
            return {"error": "User with that email already exists"}, 409

    return {"error": "Email and password are required"}, 400


@bp.route("auth/login/", methods=["POST"])
def login():
    pass


@bp.route("items/", methods=["GET", "POST"])
def all_items():
    pass


@bp.route("items/<int:item_id>/", methods=["GET", "PATCH", "DELETE"])
def item(item_id):
    pass
