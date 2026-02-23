from sqlalchemy.orm import Mapped, relationship

from src.model.base import Base
from src.model.mixins import (
    ApproCashUmeMixin,
    ApproRzAmountsMixin,
    ApproTdpAmountsMixin,
    CpNameMixin,
    FileIdMixin,
    IdMixin,
    LocationMixin,
    MontantCIMixin,
    MontantCIShopMixin,
    MontantCOMixin,
    NdCpApproMixin,
    NdCpMixin,
    NdRzMixin,
    NdTdpMixin,
    TdpNameMixin,
    WeekStartMixin,
    NameMixin,
    LastNameMixin,
)


class RecapRZ(
    Base,
    IdMixin,
    WeekStartMixin,
    TdpNameMixin,
    NdTdpMixin,
    NdRzMixin,
    NameMixin,
    LastNameMixin,
    LocationMixin,
    NdCpApproMixin,
    ApproCashUmeMixin,
    MontantCIMixin,
    FileIdMixin,
):
    __tablename__ = "recap_rz"

    file: Mapped["File"] = relationship("File", back_populates="recap_rz")


class DetailsApproRz(
    Base,
    IdMixin,
    WeekStartMixin,
    TdpNameMixin,
    NdRzMixin,
    NdCpMixin,
    NameMixin,
    LastNameMixin,
    LocationMixin,
    ApproRzAmountsMixin,
    FileIdMixin,
):
    __tablename__ = "details_appro_rz"

    file: Mapped["File"] = relationship("File", back_populates="details_appro_rz")


class DetailsCP(
    Base,
    IdMixin,
    WeekStartMixin,
    TdpNameMixin,
    NdCpMixin,
    CpNameMixin,
    LocationMixin,
    ApproTdpAmountsMixin,
    ApproRzAmountsMixin,
    MontantCIMixin,
    MontantCOMixin,
    MontantCIShopMixin,
    FileIdMixin,
):
    __tablename__ = "details_cp"

    file: Mapped["File"] = relationship("File", back_populates="details_cp")
