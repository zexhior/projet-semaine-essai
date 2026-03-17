from app.model.base import Base
from datetime import date
from sqlalchemy import BigInteger, Date, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.model.mixins import IdMixin, FileIdMixin

class TransactionRZ(Base):
    __tablename__ = "transaction_rz"
    __table_args__ = {"schema": "public"}

    date: Mapped[date] = mapped_column(Date, nullable=False)
    msisdn_rz: Mapped[str] = mapped_column(String, nullable=False)
    msisdn_livreur: Mapped[str] = mapped_column(String, nullable=False)
    tld_msisdn_rattachement: Mapped[str] = mapped_column(String, nullable=False)
    nombre_transferts_reçus: Mapped[int] = mapped_column(Integer, nullable=False)
    montant_transferts_reçus: Mapped[int] = mapped_column(BigInteger, nullable=False) 
    
    file_id: Mapped[int] = mapped_column(ForeignKey("file.id"), nullable=False)
    file: Mapped["File"] = relationship("File", back_populates="transaction_rz")
    
class TransactionGrossisteVersRZ(Base):
    __tablename__ = "transaction_grossiste_vers_rz"
    __table_args__ = {"schema": "public"}

    date: Mapped[date] = mapped_column(Date, nullable=False)
    msisdn_grossiste: Mapped[str] = mapped_column(String, nullable=False)
    msisdn_rz: Mapped[str] = mapped_column(String, nullable=False)
    nombre_transferts_reçus: Mapped[int] = mapped_column(Integer, nullable=False)
    montant_transferts_reçus: Mapped[int] = mapped_column(BigInteger, nullable=False)
    
    file_id: Mapped[int] = mapped_column(ForeignKey("file.id"), nullable=False)
    file: Mapped["File"] = relationship("File", back_populates="transaction_grossiste_vers_rz")
    
class TransactionPDV(Base):
    __tablename__ = "transaction_pdv"
    __table_args__ = {"schema": "public"}

    date: Mapped[date] = mapped_column(Date, nullable=False)
    msisdn_pdv: Mapped[str] = mapped_column(String, nullable=False)
    date_activation: Mapped[date] = mapped_column(Date, nullable=True)
    last_date: Mapped[date] = mapped_column(Date, nullable=True)
    msisdn_rattachement: Mapped[str] = mapped_column(String, nullable=False)
    nombre_transactions: Mapped[int] = mapped_column(Integer, nullable=False)
    montant_transactions: Mapped[int] = mapped_column(BigInteger, nullable=False)
    
    file_id: Mapped[int] = mapped_column(ForeignKey("file.id"), nullable=False)
    file: Mapped["File"] = relationship("File", back_populates="transaction_pdv")
    
class TransactionLivreur(Base):
    __tablename__ = "transaction_livreur"
    __table_args__ = {"schema": "public"}

    date: Mapped[date] = mapped_column(Date, nullable=False)
    msisdn_livreur: Mapped[str] = mapped_column(String, nullable=False)
    msisdn_pdv: Mapped[str] = mapped_column(String, nullable=True)
    nombre_transferts_reçus: Mapped[int] = mapped_column(Integer, nullable=False)
    montant_transferts_reçus: Mapped[int] = mapped_column(BigInteger, nullable=False)
    
    file_id: Mapped[int] = mapped_column(ForeignKey("file.id"), nullable=False)
    file: Mapped["File"] = relationship("File", back_populates="transaction_livreur")
    
class TransactionGrossisteLivreur(Base):
    __tablename__ = "transaction_grossiste_livreur"
    __table_args__ = {"schema": "public"}

    date: Mapped[date] = mapped_column(Date, nullable=False)
    msisdn_grossiste: Mapped[str] = mapped_column(String, nullable=False)
    msisdn_livreur: Mapped[str] = mapped_column(String, nullable=False)
    nombre_transferts_reçus: Mapped[int] = mapped_column(Integer, nullable=False)
    montant_transferts_reçus: Mapped[int] = mapped_column(BigInteger, nullable=False)
    
    file_id: Mapped[int] = mapped_column(ForeignKey("file.id"), nullable=False)
    file: Mapped["File"] = relationship("File", back_populates="transaction_grossiste_livreur")
    
class SoldeAgents(Base):
    __tablename__ = "solde_agents"
    __table_args__ = {"schema": "public"}

    date: Mapped[date] = mapped_column(Date, nullable=False)
    type_agent: Mapped[str] = mapped_column(String, nullable=False)
    rattachement: Mapped[str] = mapped_column(String, nullable=False)
    agent_msisdn: Mapped[str] = mapped_column(String, nullable=False)
    agent_nom: Mapped[str] = mapped_column(String, nullable=False)
    balance: Mapped[int] = mapped_column(BigInteger, nullable=False)
    
    file_id: Mapped[int] = mapped_column(ForeignKey("file.id"), nullable=False)
    file: Mapped["File"] = relationship("File", back_populates="solde_agents")  