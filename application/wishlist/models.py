from sqlalchemy.orm import Mapped, mapped_column

from ..db import db


class ItemModel(db.Model):
    __tablename__ = "item"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column()
    url: Mapped[str] = mapped_column()
    price: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()

    def __repr__(self):
        return f"<ItemModel({self.id=} - {self.name=} - {self.price=})>"
