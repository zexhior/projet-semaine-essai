from src.model.base import BaseConnexion
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

class Connexion(BaseConnexion):
    __tablename__ = 'connexions'
    __table_args__ = {"schema": "connexion"}

    id = Column(Integer, primary_key=True)
    source: Mapped[str] = mapped_column(String(255), nullable=False)
    connected_at: Mapped[str] = mapped_column(String(255), nullable=False)