from sqlalchemy.orm import Mapped, mapped_column

from ..db import db


class UserModel(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column()
    password: Mapped[str] = mapped_column()
