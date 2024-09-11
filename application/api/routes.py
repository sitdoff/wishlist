from flask import Blueprint
from sqlalchemy import select

from ..db import db
from ..wishlist.models import ItemModel

bp = Blueprint("api", __name__, url_prefix="/api")
