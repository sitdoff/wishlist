from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from sqlalchemy import desc

from application.forms.forms import ItemForm

from ..db import db
from .models import ItemModel

bp = Blueprint("wishlist", __name__, url_prefix="/wishlist")


@bp.route("/")
@login_required
def main():
    items = (
        db.session.execute(
            db.select(ItemModel)
            .filter_by(user_id=current_user.id)
            .order_by(desc(ItemModel.id))
        )
        .scalars()
        .all()
    )
    return render_template("index.html", items=items)


@bp.route("/add/", methods=["GET", "POST"])
@login_required
def add():
    if request.method == "POST":
        item = ItemModel(
            name=request.form["name"],
            url=request.form["url"],
            price=request.form["price"],
            description=request.form["description"],
            user_id=current_user.id,
        )
        db.session.add(item)
        db.session.commit()
        return redirect(url_for("wishlist.main"))
    return render_template("add.html", form=ItemForm())


@bp.route("remove/<int:id>/", methods=["GET"])
@login_required
def remove(id):
    db.session.execute(db.delete(ItemModel).where(ItemModel.id == id))
    db.session.commit()
    return redirect(url_for("wishlist.main"))
