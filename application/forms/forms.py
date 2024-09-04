from decimal import ROUND_UP, Decimal

from flask_wtf import FlaskForm
from wtforms import (DecimalField, StringField, SubmitField, TextAreaField,
                     URLField)
from wtforms.validators import InputRequired


class ItemForm(FlaskForm):
    name = StringField("Name", description="Item name", validators=[InputRequired()])
    url = URLField("Url", validators=[InputRequired()])
    price = DecimalField("Price", places=2, validators=[InputRequired()])
    description = TextAreaField("Description")
    submit = SubmitField("Add")
