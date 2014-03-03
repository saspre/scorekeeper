#models.py
# I have collected all models into this file/module because it is easier for SQLAlchemy 
# Feel free to split it up into more files if you can

from sqlalchemy import create_engine, Column, Integer, String, Sequence, Table, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from model.base import Base

engine = create_engine("sqlite:///:memory:",echo=False)
Session = sessionmaker(bind=engine)

player_team = Table('player_team',Base.metadata,
    Column('player_id',Integer,ForeignKey('players.id')),
    Column('team_id',Integer,ForeignKey('teams.id'))
)

#################################################################################################################
class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer,Sequence('player_id_seq'),primary_key=True)
    name = Column(String)

    def __repr__(self):
        return "<Player(name='%s')>" % (self.name)

#################################################################################################################
class Match(Base):
    __tablename__ = 'matches'

    id = Column(Integer,Sequence('match_id_seq'),primary_key=True)
    score_a = Column(Integer,default = int(0), nullable = False)
    score_b = Column(Integer,default = int(0), nullable = False)
    team_a_id = Column(Integer,ForeignKey('teams.id'))
    team_a = relationship('Team', backref=backref('matches_a', order_by=id),foreign_keys=team_a_id)
    team_b_id = Column(Integer,ForeignKey('teams.id'))
    team_b = relationship('Team', backref=backref('matches_b', order_by=id),foreign_keys=team_b_id)

    def __repr__(self):
        return "<Match(team_a='%s', score_a='%s', team_b='%s', score_b='%s')>" % (self.team_a, self.score_a, self.team_b, self.score_b)

#################################################################################################################
class Team(Base):
    __tablename__ = 'teams'

    id = Column(Integer,Sequence('team_id_seq'),primary_key=True)
    name = Column(String)
    players = relationship('Player',secondary='player_team',backref='teams')

    def matches(self):
        return self.matches_a + self.matches_b

    def __repr__(self):
        return "<Team(name='%s')>" % (self.name)

Base.metadata.create_all(engine)
