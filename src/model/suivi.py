from src.model.base import Base
from datetime import date
from sqlalchemy import BigInteger, Date, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.model.mixins import IdMixin, FileIdMixin

class TransactionRZ(Base):
    __tablename__ = "transaction_rz"

    date: Mapped[date] = mapped_column(Date, nullable=True)
    msisdn_rz: Mapped[str] = mapped_column(String, nullable=True)
    msisdn_livreur: Mapped[str] = mapped_column(String, nullable=True)
    tld_msisdn_rattachement: Mapped[str] = mapped_column(String, nullable=True)
    nombre_transferts_reçus: Mapped[int] = mapped_column(Integer, nullable=True)
    montant_transferts_reçus: Mapped[int] = mapped_column(BigInteger, nullable=True) 
    
    file_id: Mapped[int] = mapped_column(ForeignKey("file.id"), nullable=True)
    file: Mapped["File"] = relationship("File", back_populates="transaction_rz")
    
class TransactionGrossisteVersRZ(Base):
    __tablename__ = "transaction_grossiste_vers_rz"


    date: Mapped[date] = mapped_column(Date, nullable=True)
    msisdn_grossiste: Mapped[str] = mapped_column(String, nullable=True)
    msisdn_rz: Mapped[str] = mapped_column(String, nullable=True)
    nombre_transferts_reçus: Mapped[int] = mapped_column(Integer, nullable=True)
    montant_transferts_reçus: Mapped[int] = mapped_column(BigInteger, nullable=True)
    
    file_id: Mapped[int] = mapped_column(ForeignKey("file.id"), nullable=False)
    file: Mapped["File"] = relationship("File", back_populates="transaction_grossiste_vers_rz")
    
class TransactionPDV(Base):
    __tablename__ = "transaction_pdv"

    date: Mapped[date] = mapped_column(Date, nullable=True)
    msisdn_pdv: Mapped[str] = mapped_column(String, nullable=True)
    date_activation: Mapped[date] = mapped_column(Date, nullable=True)
    last_date: Mapped[date] = mapped_column(Date, nullable=True)
    msisdn_rattachement: Mapped[str] = mapped_column(String, nullable=True)
    nombre_transactions: Mapped[int] = mapped_column(Integer, nullable=True)
    montant_transactions: Mapped[int] = mapped_column(BigInteger, nullable=True)
    
    file_id: Mapped[int] = mapped_column(ForeignKey("file.id"), nullable=True)
    file: Mapped["File"] = relationship("File", back_populates="transaction_pdv")
    
class TransactionLivreur(Base):
    __tablename__ = "transaction_livreur"

    date: Mapped[date] = mapped_column(Date, nullable=True)
    msisdn_livreur: Mapped[str] = mapped_column(String, nullable=True)
    msisdn_pdv: Mapped[str] = mapped_column(String, nullable=True)
    nombre_transferts_reçus: Mapped[int] = mapped_column(Integer, nullable=True)
    montant_transferts_reçus: Mapped[int] = mapped_column(BigInteger, nullable=True)
    
    file_id: Mapped[int] = mapped_column(ForeignKey("file.id"), nullable=True)
    file: Mapped["File"] = relationship("File", back_populates="transaction_livreur")
    
class TransactionGrossisteLivreur(Base):
    __tablename__ = "transaction_grossiste_livreur"

    date: Mapped[date] = mapped_column(Date, nullable=True)
    msisdn_grossiste: Mapped[str] = mapped_column(String, nullable=True)
    msisdn_livreur: Mapped[str] = mapped_column(String, nullable=True)
    nombre_transferts_reçus: Mapped[int] = mapped_column(Integer, nullable=True)
    montant_transferts_reçus: Mapped[int] = mapped_column(BigInteger, nullable=True)
    
    file_id: Mapped[int] = mapped_column(ForeignKey("file.id"), nullable=True)
    file: Mapped["File"] = relationship("File", back_populates="transaction_grossiste_livreur")
    
class SoldeAgents(Base):
    __tablename__ = "solde_agents"

    date: Mapped[date] = mapped_column(Date, nullable=True)
    type_agent: Mapped[str] = mapped_column(String, nullable=True)
    rattachement: Mapped[str] = mapped_column(String, nullable=True)
    agent_msisdn: Mapped[str] = mapped_column(String, nullable=True)
    agent_nom: Mapped[str] = mapped_column(String, nullable=True)
    balance: Mapped[int] = mapped_column(BigInteger, nullable=True)
    
    file_id: Mapped[int] = mapped_column(ForeignKey("file.id"), nullable=True)
    file: Mapped["File"] = relationship("File", back_populates="solde_agents")