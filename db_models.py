from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column,
    Text,
    Integer,
    Boolean
)


Base = declarative_base()


class Game(Base):
    __tablename__ = "game"
    id = Column(Integer, primary_key=True)
    player_one_name = Column(Text)
    player_one_mark = Column(Text)
    player_two_name = Column(Text)
    player_two_mark = Column(Text)
    board = Column(Text)
    last_player = Column(Text)
    winner = Column(Text)
    done = Column(Boolean)
