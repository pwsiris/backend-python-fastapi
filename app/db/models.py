from sqlalchemy import Column, Date, Integer, MetaData, Numeric, Sequence, String, text
from sqlalchemy.dialects.postgresql import JSONB

# from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import declarative_base

# from sqlalchemy.orm import Mapped
# from sqlalchemy.orm import mapped_column


SCHEMA = "pwsi"
# class Base(DeclarativeBase):
#    pass
TestBase = declarative_base()
Base = declarative_base(metadata=MetaData(schema=SCHEMA))


class Test(TestBase):
    __tablename__ = "test"

    # id: Mapped[int] = mapped_column(primary_key=True)
    id = Column(Integer, primary_key=True)
    # text: Mapped[str]
    text = Column(String)


class Game(Base):
    __tablename__ = "game"

    id = Column(
        Integer,
        Sequence("game_id_seq", schema=SCHEMA, metadata=Base.metadata),
        primary_key=True,
        server_default=text(f"nextval('{SCHEMA}.game_id_seq'::regclass)"),
    )
    name = Column(String, nullable=False)
    link = Column(String)
    status = Column(String, nullable=False)
    order_by = Column(Integer)
    comment = Column(String)
    added_date = Column(Date, nullable=False)
    completed_date = Column(Date)
    score = Column(Numeric(4, 1, asdecimal=False))
    genre = Column(Integer)
    records = Column(JSONB)


class User(Base):
    __tablename__ = "user"

    id = Column(
        Integer,
        Sequence("user_id_seq", schema=SCHEMA, metadata=Base.metadata),
        primary_key=True,
        server_default=text(f"nextval('{SCHEMA}.user_id_seq'::regclass)"),
    )
    name = Column(String, nullable=False)
    stream_status = Column(String)


class GameGenre(Base):
    __tablename__ = "game_genre"

    id = Column(
        Integer,
        Sequence("game_genre_id_seq", schema=SCHEMA, metadata=Base.metadata),
        primary_key=True,
        server_default=text(f"nextval('{SCHEMA}.game_genre_id_seq'::regclass)"),
    )
    name = Column(String, nullable=False)


class Anime(Base):
    __tablename__ = "anime"

    id = Column(
        Integer,
        Sequence("anime_id_seq", schema=SCHEMA, metadata=Base.metadata),
        primary_key=True,
        server_default=text(f"nextval('{SCHEMA}.anime_id_seq'::regclass)"),
    )
    name = Column(String, nullable=False)
    name_ru = Column(String)
    link_mal = Column(String)
    link_shiki = Column(String)
    status = Column(String, nullable=False)
    order_by = Column(Integer)
    comment = Column(String)
    added_date = Column(Date, nullable=False)
    completed_date = Column(Date)
    score = Column(Numeric(4, 1, asdecimal=False))
    type = Column(String)
    episodes = Column(Integer)
    watched = Column(Integer)
    series = Column(String)


class Manga(Base):
    __tablename__ = "manga"

    id = Column(
        Integer,
        Sequence("manga_id_seq", schema=SCHEMA, metadata=Base.metadata),
        primary_key=True,
        server_default=text(f"nextval('{SCHEMA}.manga_id_seq'::regclass)"),
    )
    name = Column(String, nullable=False)
    name_ru = Column(String)
    link = Column(String)
    status = Column(String, nullable=False)
    order_by = Column(Integer)
    comment = Column(String)
    added_date = Column(Date, nullable=False)
    completed_date = Column(Date)
    score = Column(Numeric(4, 1, asdecimal=False))
    type = Column(String)
    chapters = Column(Integer)
    readed = Column(Integer)


class WantToPlay(Base):
    __tablename__ = "want_to_play"

    id = Column(
        Integer,
        Sequence("want_to_play_id_seq", schema=SCHEMA, metadata=Base.metadata),
        primary_key=True,
        server_default=text(f"nextval('{SCHEMA}.want_to_play_id_seq'::regclass)"),
    )

    user_id = Column(Integer)
    game_id = Column(Integer)
