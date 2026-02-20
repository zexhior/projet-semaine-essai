from datetime import date

from sqlalchemy import Date, String, BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from model.base import Base

class LiveService(Base):
    __tablename__ = "live_service"
    
    id: Mapped[int]= mapped_column(primary_key=True)
    week_start: Mapped[date] = mapped_column(Date, nullable=False)
    nom_tdp: Mapped[str] = mapped_column(String, nullable=False)
    nd_cp: Mapped[str] = mapped_column(String, nullable=False)
    nom_cp: Mapped[str] = mapped_column(String, nullable=False)
    prenom_cp: Mapped[str] = mapped_column(String, nullable=False)
    region: Mapped[str] = mapped_column(String, nullable=False)
    ville: Mapped[str] = mapped_column(String, nullable=False)
    appro_ume_tdp: Mapped[int] = mapped_column(BigInteger, nullable=False)
    appro_cash_td: Mapped[int] = mapped_column(BigInteger, nullable=False)
    appro_ume_rz: Mapped[int] = mapped_column(BigInteger, nullable=False)
    appro_cash_rz: Mapped[int] = mapped_column(BigInteger, nullable=False)
    montant_ci: Mapped[int] = mapped_column(BigInteger, nullable=False)
    montant_co: Mapped[int] = mapped_column(BigInteger, nullable=False)
    montant_ci_shop: Mapped[int] = mapped_column(BigInteger, nullable=False)
    
    file_id: Mapped[int] = mapped_column(ForeignKey("file.id"), nullable=False)
    file: Mapped['File'] = relationship('File', back_populates='live_services')