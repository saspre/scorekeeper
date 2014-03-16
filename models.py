#models.py
# I have collected all models into this file/module because it is easier for SQLAlchemy 
# Feel free to split it up into more files if you can (dare)

from sqlalchemy import create_engine, Column, Integer, String, Sequence, Table, Text, ForeignKey, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from datetime import datetime
import config
import traceback

Base = declarative_base()
engine = create_engine(config.Config.get("database","connectionstring"),echo=False)
Session = sessionmaker(bind=engine)

#################################################################################################################
################################## Table used to connect players and to teams ###################################
#################################################################################################################
player_team = Table('player_team',Base.metadata,
    Column('player_id',Integer,ForeignKey('players.id')),
    Column('team_id',Integer,ForeignKey('teams.id'))
)

#################################################################################################################
class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer,Sequence('player_id_seq'),primary_key=True)
    rfid = Column(String,unique=True)
    name = Column(String)
    created_at = Column(DateTime, default=func.now())

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
    created_at = Column(DateTime, default=func.now())

    def __repr__(self):
        return "<Match(team_a='%s', score_a='%s', team_b='%s', score_b='%s')>" % (self.team_a, self.score_a, self.team_b, self.score_b)

#################################################################################################################
class Team(Base):
    __tablename__ = 'teams'

    id = Column(Integer,Sequence('team_id_seq'),primary_key=True)
    name = Column(String)
    players = relationship('Player',secondary='player_team',backref='teams')
    created_at = Column(DateTime, default=func.now())

    def matches(self):
        return self.matches_a + self.matches_b

    def __repr__(self):
        return "<Team(name='%s')>" % (self.name)

def initSchema():
    Base.metadata.create_all(engine)

def dropSchema():
    Base.metadata.drop_all(engine)

def initData():
    session = Session()

    try:
        p = [ \
                Player(name='Rasmus', rfid='1'),\
                Player(name='Kim', rfid='2'),\
                Player(name='Simon', rfid='3'),\
                Player(name='Alex', rfid='4'),\
                Player(name='Mikael', rfid='5')\
            ]
        session.add_all(p)

        single_teams =  [ \
                            Team(name=p[0].name),\
                            Team(name=p[1].name),\
                            Team(name=p[2].name),\
                            Team(name=p[3].name),\
                            Team(name=p[4].name)\
                        ]
        session.add_all(single_teams)
        single_teams[0].players.append(p[0])
        single_teams[1].players.append(p[1])
        single_teams[2].players.append(p[2])
        single_teams[3].players.append(p[3])
        single_teams[4].players.append(p[4])

        multi_teams =   [   \
                            Team(name=p[0].name+p[1].name),\
                            Team(name=p[0].name+p[2].name),\
                            Team(name=p[0].name+p[3].name),\
                            Team(name=p[1].name+p[2].name),\
                            Team(name=p[1].name+p[3].name),\
                            Team(name=p[2].name+p[3].name) \
                        ]
        session.add_all(multi_teams)
        multi_teams[0].players.append(p[0])
        multi_teams[0].players.append(p[1])
        multi_teams[1].players.append(p[0])
        multi_teams[1].players.append(p[2])
        multi_teams[2].players.append(p[0])
        multi_teams[2].players.append(p[3])
        multi_teams[3].players.append(p[1])
        multi_teams[3].players.append(p[2])
        multi_teams[4].players.append(p[1])
        multi_teams[4].players.append(p[3])
        multi_teams[5].players.append(p[2])
        multi_teams[5].players.append(p[3])

        session.commit()
    except:
        print(traceback.format_exc())
        session.rollback()
        raise Exception("Rolling back initialize data")

"""
I am considering changing matches such that their not only include the final results, but also "events", such as a scoring.
If we do it like that we will get even more statistics available, and we have discussed having automatic notices of 
goals being scored anyways. Please note that this is not something we need immediately, but it might worth implementing later.
"""