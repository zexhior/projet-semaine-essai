from typing import List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from model.base import Base

class File(Base):
  __tablename__ = "file"
  
  id: Mapped[int] = mapped_column(primary_key=True)
  name: Mapped[str] = mapped_column(String, nullable=False)
  live_services: Mapped[List["LiveService"]] = relationship(
      "LiveService", back_populates="file"
  )