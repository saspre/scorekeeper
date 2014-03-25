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

    @staticmethod
    def createOrLoad(rfid,session):
        playerList = session.query(Player).filter(Player.rfid == rfid)
        if playerList.count() <= 0:
            session.add(Player(name=rfid,rfid=rfid))
        return session.query(Player).filter(Player.rfid == rfid).one()

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

    def size(self):
        return len(self.players)

    def __repr__(self):
        return "<Team(name='%s', players='%s')>" % (self.name, self.players)

    @staticmethod
    def createOrLoad(players,session):
        teams = []
        resultTeam = None
        for player in players:
            teams.append(player.teams)
             
        intersectList = reduce(lambda xs,ys: filter(lambda x : x in xs,ys),teams)
        for team in intersectList:
            #team exists, set as local team
            if team.size() == len(teams):
                resultTeam = team
                break

        if resultTeam == None:
            resultTeam = Team(name = " & ".join(map(lambda x: x.name,players)))
            for player in players:
                resultTeam.players.append(player)
            session.add(resultTeam)
        
        if resultTeam == None:
            raise Exception("Result team not set.")

        return resultTeam

def initSchema():
    Base.metadata.create_all(engine)

def dropSchema():
    Base.metadata.drop_all(engine)

def initData():
    session = sessionmaker(bind=engine)()

    try:
        p = [ \
                Player(name='Rasmus', rfid='1'),\
                Player(name='Kim', rfid='2'),\
                Player(name='Simon', rfid='3'),\
                Player(name='Alex', rfid='4'),\
                Player(name='Mikael', rfid='5')\
            ]
        session.add_all(p)

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