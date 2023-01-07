from sqlalchemy import Column, Integer, String

# from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import declarative_base

# from sqlalchemy.orm import Mapped
# from sqlalchemy.orm import mapped_column


# class Base(DeclarativeBase):
#    pass
Base = declarative_base()

SCHEMA = "pwsi"


class Test(Base):
    __tablename__ = "test"

    # id: Mapped[int] = mapped_column(primary_key=True)
    id = Column(Integer, primary_key=True)
    # text: Mapped[str]
    text = Column(String)
