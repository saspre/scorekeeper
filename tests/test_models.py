#!/usr/bin/python
import unittest
import config
config.initConfig('config/test_conf.conf') # must be called before importing models to ensure memory based db
from models.model import Player, Match, Team, initSchema, dropSchema, Session



class ModelsTest(unittest.TestCase):

    def setUp(self):
        initSchema()
        self.session = Session()

    def tearDown(self):
        self.session.close()
        dropSchema()

    def test_player_createOrLoad_same(self):
        playerA = Player.createOrLoad('1',self.session)
        self.session.commit()
        playerB = Player.createOrLoad('1',self.session)
        self.assertEqual(playerA,playerB)

    def test_player_createOrLoad_different(self):
        playerA = Player.createOrLoad('1',self.session)
        self.session.commit()
        playerB = Player.createOrLoad('2',self.session)
        self.assertNotEqual(playerA,playerB)

    def test_team_createOrLoad_existingPlayer_same(self):
        #setup
        player = Player(rfid='1',name='1')
        self.session.add(player)
        self.session.commit()
        #run
        teamA = Team.createOrLoad([player],self.session)
        self.session.add(teamA)
        self.session.commit()
        teamB = Team.createOrLoad([player],self.session)
        self.assertEqual(teamA,teamB)

    def test_team_createOrLoad_existingPlayers_same(self):
        #setup
        player1 = Player(rfid='1',name='1')
        player2 = Player(rfid='2',name='2')
        self.session.add(player1)
        self.session.add(player2)
        self.session.commit()
        #run
        teamA = Team.createOrLoad([player1,player2],self.session)
        self.session.add(teamA)
        self.session.commit()
        teamB = Team.createOrLoad([player1,player2],self.session)
        self.assertEqual(teamA,teamB)

    def test_team_createOrLoad_existingPlayer_different(self):
        #setup
        player1 = Player(rfid='1',name='1')
        player2 = Player(rfid='2',name='2')
        self.session.add(player1)
        self.session.add(player2)
        self.session.commit()
        #run
        teamA = Team.createOrLoad([player1],self.session)
        self.session.add(teamA)
        self.session.commit()
        teamB = Team.createOrLoad([player2],self.session)
        self.assertNotEqual(teamA,teamB)

    def test_team_createOrLoad_existingPlayers_different(self):
        #setup
        player1 = Player(rfid='1',name='1')
        player2 = Player(rfid='2',name='2')
        player3 = Player(rfid='3',name='3')
        player4 = Player(rfid='4',name='4')
        self.session.add(player1)
        self.session.add(player2)
        self.session.add(player3)
        self.session.add(player4)
        self.session.commit()
        #run
        teamA = Team.createOrLoad([player1,player2],self.session)
        self.session.add(teamA)
        self.session.commit()
        teamB = Team.createOrLoad([player3,player4],self.session)
        self.assertNotEqual(teamA,teamB)

    def test_team_createOrLoad_newPlayer_same(self):
        #setup
        player = Player(rfid='1',name='1')
        #run
        teamA = Team.createOrLoad([player],self.session)
        self.session.add(teamA)
        self.session.commit()
        self.assertEqual(self.session.query(Player).filter(Player.rfid == '1').one(),player)
        teamB = Team.createOrLoad([player],self.session)
        self.assertEqual(teamA,teamB)

    def test_team_createOrLoad_newPlayers_same(self):
        #setup
        player1 = Player(rfid='1',name='1')
        player2 = Player(rfid='2',name='2')
        #run
        teamA = Team.createOrLoad([player1,player2],self.session)
        self.session.add(teamA)
        self.session.commit()
        self.assertEqual(self.session.query(Player).filter(Player.rfid == '1').one(),player1)
        teamB = Team.createOrLoad([player1,player2],self.session)
        self.assertEqual(teamA,teamB)

    def test_team_createOrLoad_newPlayer_different(self):
        #setup
        player1 = Player(rfid='1',name='1')
        player2 = Player(rfid='2',name='2')
        #run
        teamA = Team.createOrLoad([player1],self.session)
        self.session.add(teamA)
        self.session.commit()
        self.assertEqual(self.session.query(Player).filter(Player.rfid == '1').one(),player1)
        teamB = Team.createOrLoad([player2],self.session)
        self.assertNotEqual(teamA,teamB)

    def test_team_createOrLoad_newPlayers_different(self):
        #setup
        player1 = Player(rfid='1',name='1')
        player2 = Player(rfid='2',name='2')
        player3 = Player(rfid='3',name='3')
        player4 = Player(rfid='4',name='4')
        #run
        teamA = Team.createOrLoad([player1,player2],self.session)
        self.session.add(teamA)
        self.session.commit()
        self.assertEqual(self.session.query(Player).filter(Player.rfid == '1').one(),player1)
        teamB = Team.createOrLoad([player3,player4],self.session)
        self.assertNotEqual(teamA,teamB)

if __name__ == '__main__':
    unittest.main()