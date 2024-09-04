from flask import Blueprint, redirect, render_template, request, url_for

from application.forms.forms import ItemForm

from .models import ItemModel, db

bp = Blueprint("wishlist", __name__, url_prefix="/wishlist")


@bp.route("/")
def main():
    items = (
        db.session.execute(db.select(ItemModel).order_by(ItemModel.name))
        .scalars()
        .all()
    )
    print(items)
    return render_template("index.html", items=items)


@bp.route("/add/", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        item = ItemModel(
            name=request.form["name"],
            url=request.form["url"],
            price=request.form["price"],
            description=request.form["description"],
        )
        db.session.add(item)
        db.session.commit()
        return redirect(url_for("wishlist.main"))
    return render_template("add.html", form=ItemForm())


@bp.route("remove/<int:id>/", methods=["GET"])
def remove(id):
    db.session.execute(db.delete(ItemModel).where(ItemModel.id == id))
    db.session.commit()
    return redirect(url_for("wishlist.main"))
