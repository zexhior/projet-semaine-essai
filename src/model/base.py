from datetime import datetime
from sqlalchemy import MetaData, func, DateTime
from config.config import PG_SCHEMA
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, server_default=func.now(), onupdate=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, server_default=func.now(), onupdate=func.now()
    )
    
    metadata = MetaData(schema=PG_SCHEMA)