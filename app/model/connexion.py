from app.model.base import BaseConnexion
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

class Connexion(BaseConnexion):
    __tablename__ = 'connexions'
    __table_args__ = {"schema": "connexion"}

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    source: Mapped[str] = mapped_column(String(100), default='application')
    status: Mapped[str] = mapped_column(String(20))
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    checked_at: Mapped[DateTime] = mapped_column(DateTime) 