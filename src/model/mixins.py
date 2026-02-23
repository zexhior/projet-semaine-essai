from datetime import date

from sqlalchemy import BigInteger, Date, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

class IdMixin:
    id: Mapped[int] = mapped_column(primary_key=True)
    
class NameMixin:
    nom: Mapped[str] = mapped_column(String, nullable=False)
    
class LastNameMixin:
    prenom: Mapped[str] = mapped_column(String, nullable=False)


class WeekStartMixin:
    week_start: Mapped[date] = mapped_column(Date, nullable=False)


class TdpNameMixin:
    nom_tdp: Mapped[str] = mapped_column(String, nullable=False)

class CpNameMixin:
    nom_cp: Mapped[str] = mapped_column(String, nullable=False)
    prenom_cp: Mapped[str] = mapped_column(String, nullable=False)


class LocationMixin:
    region: Mapped[str] = mapped_column(String, nullable=False)
    ville: Mapped[str] = mapped_column(String, nullable=False)


class NdCpMixin:
    nd_cp: Mapped[str] = mapped_column(String, nullable=False)


class NdTdpMixin:
    nd_tdp: Mapped[str] = mapped_column(String, nullable=False)


class NdRzMixin:
    nd_rz: Mapped[str] = mapped_column(String, nullable=False)


class NdCpApproMixin:
    nd_cp_appro: Mapped[str] = mapped_column(String, nullable=False)


class ApproCashUmeMixin:
    appro_cash: Mapped[int] = mapped_column(BigInteger, nullable=False)
    appro_ume: Mapped[int] = mapped_column(BigInteger, nullable=False)


class ApproTdpAmountsMixin:
    appro_ume_tdp: Mapped[int] = mapped_column(BigInteger, nullable=False)
    appro_cash_td: Mapped[int] = mapped_column(BigInteger, nullable=False)


class ApproRzAmountsMixin:
    appro_ume_rz: Mapped[int] = mapped_column(BigInteger, nullable=False)
    appro_cash_rz: Mapped[int] = mapped_column(BigInteger, nullable=False)


class MontantCIMixin:
    montant_ci: Mapped[int] = mapped_column(BigInteger, nullable=False)


class MontantCOMixin:
    montant_co: Mapped[int] = mapped_column(BigInteger, nullable=False)


class MontantCIShopMixin:
    montant_ci_shop: Mapped[int] = mapped_column(BigInteger, nullable=False)


class FileIdMixin:
    file_id: Mapped[int] = mapped_column(ForeignKey("file.id"), nullable=False)
