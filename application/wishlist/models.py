from sqlalchemy.orm import Mapped, mapped_column

from ..db import db


class ItemModel(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column()
    url: Mapped[str] = mapped_column()
    price: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
