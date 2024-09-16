from flask import Blueprint, request
from flask_jwt_extended import (create_access_token, current_user,
                                get_jwt_identity, jwt_required)
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError, SQLAlchemyError, StatementError
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
    email = request.json.get("email")
    password = request.json.get("password")
    user = UserModel.query.filter_by(email=email).first()
    if user and user.check_password(password):
        token = create_access_token(identity=user)
        return {"access_token": token}, 200
    return {"error": "Wrong email or password"}, 401


@bp.route("items/", methods=["GET", "POST"])
@jwt_required()
def all_items():

    if request.method == "POST":
        required_fields = ("name", "url", "price", "description")

        item_data = request.get_json()
        if not item_data:
            return {"error": "Item data is required"}, 400

        missing_fields = [field for field in required_fields if field not in item_data]
        if missing_fields:
            return {
                "error": f"Missing required fields: {', '.join(missing_fields)}"
            }, 400

        empty_fields = [field for field in item_data if not item_data[field]]
        if empty_fields:
            return {"error": f"Empty fields: {', '.join(empty_fields)}"}, 400

        try:
            user = UserModel.query.filter_by(email=get_jwt_identity()).first()
            item = ItemModel(**item_data, user_id=user.id)
            db.session.add(item)
            db.session.commit()
            return {"success": "Item created", "item": item.to_dict()}, 201
        except Exception as e:
            return {"error": str(e)}, 400
    items = UserModel.query.filter_by(email=get_jwt_identity()).first().items
    return [item.to_dict() for item in items]


@bp.route("items/<int:item_id>/", methods=["GET", "PATCH", "DELETE"])
@jwt_required()
def item(item_id):
    item = ItemModel.query.filter_by(id=item_id).first()
    if item is None:
        return {"error": "Item not found"}, 404

    if item and item.user_id != current_user.id:
        return {"error": "You can only edit your own items"}, 403

    if request.method == "PATCH":
        allowed_fields = ("name", "url", "price", "description")
        data = request.get_json()
        try:
            for key, value in data.items():
                if key in allowed_fields:
                    setattr(item, key, value)
            db.session.commit()
            return {"success": "Item updated", "item": item.to_dict()}, 200
        except StatementError as e:
            return {"error": f"Invalid data '{key}': '{value}'"}, 400

    if request.method == "DELETE":
        try:
            db.session.delete(item)
            db.session.commit()
            return {"success": "Item deleted"}, 200
        except SQLAlchemyError as e:
            return {"error": str(e)}, 400

    return item.to_dict()
