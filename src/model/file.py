from typing import List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.model.base import Base

class File(Base):
    __tablename__ = "file"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    recap_rz: Mapped[List["RecapRZ"]] = relationship(
        "RecapRZ", back_populates="file"
    )
    details_appro_rz: Mapped[List["DetailsApproRz"]] = relationship(
        "DetailsApproRz", back_populates="file"
    )
    details_cp: Mapped[List["DetailsCP"]] = relationship(
        "DetailsCP", back_populates="file"
    )
    transaction_rz: Mapped[List["TransactionRZ"]] = relationship(
        "TransactionRZ", back_populates="file"
    )
    transaction_grossiste_vers_rz: Mapped[List["TransactionGrossisteVersRZ"]] = relationship(
        "TransactionGrossisteVersRZ", back_populates="file"
    )
    transaction_pdv: Mapped[List["TransactionPDV"]] = relationship(
        "TransactionPDV", back_populates="file"
    )
    transaction_livreur: Mapped[List["TransactionLivreur"]] = relationship(
        "TransactionLivreur", back_populates="file"
    )
    transaction_grossiste_livreur: Mapped[List["TransactionGrossisteLivreur"]] = relationship(
        "TransactionGrossisteLivreur", back_populates="file"
    )
    solde_agents: Mapped[List["SoldeAgents"]] = relationship(
        "SoldeAgents", back_populates="file"
    )