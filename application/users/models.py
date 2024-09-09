from flask_login import UserMixin
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..db import db


class UserModel(db.Model, UserMixin):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column()

    items: Mapped[list["ItemModel"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<UserModel({self.id=} - email={self.email=})>"
