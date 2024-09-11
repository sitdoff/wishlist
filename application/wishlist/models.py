from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..db import db


class ItemModel(db.Model):
    __tablename__ = "item"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column()
    url: Mapped[str] = mapped_column()
    price: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), name="user_id")

    user: Mapped["UserModel"] = relationship(back_populates="items")

    def __repr__(self):
        return f"<ItemModel({self.id=} - {self.name=} - {self.price=})>"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "url": self.url,
            "price": self.price,
            "description": self.description,
            "user_id": self.user_id,
        }
