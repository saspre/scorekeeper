from red.activity import Activity
import traceback
from models.model import Match, Player, Team, Base, initSchema

class Creatematch(Activity):
    
    def onCreate(self,data):
        self.playersTeamA = []
        self.playersTeamB = []
        self.setLayout("match_setup")
        self.send("rfidinput",{"head":'get_rfid'})
        

    def receiveDisplayMessage(self,message):

        if message ["head"] == "echo":
            return 
        if(message["data"]=="start_match"):
            print("Start Match Button Pressed")
            try:
                match = self.createMatch()
                self.switchActivity("match", data=match)   
            except Exception:
                self.session.rollback()
                print(traceback.format_exc())

            
    def createMatch(self):
            teamAPlayers = []
            teamBPlayers = []

            if len(self.playersTeamA) == 0 or len(self.playersTeamB) == 0:
                raise Exception("You need to add players to both teams you fool")

            teamA = Team.createOrLoad(self.playersTeamA,self.session)
            teamB = Team.createOrLoad(self.playersTeamB,self.session)
            
            #Create Match
            match = Match(team_a = teamA, team_b = teamB, score_a = 0, score_b = 0)
   
            print(match)
            return match

        
    def receiveRfidinputMessage(self,message):
        if message["head"]=="player_rfid":
            self.loadPlayer(message["data"])
            
            
    def loadPlayer(self,playerRfid):
        if(len(self.playersTeamB) < len(self.playersTeamA)):
            self.playersTeamB.append(Player.createOrLoad(playerRfid,self.session))
            self.send("display",{"head":"call_func","data":{"func":"updateTeamB","param":reduce(lambda x,y: x+"\n"+y,map(lambda player:player.name,self.playersTeamB))}})
        else:
            self.playersTeamA.append(Player.createOrLoad(playerRfid,self.session))
            self.send("display",{"head":"call_func","data":{"func":"updateTeamA","param":reduce(lambda x,y: x+"\n"+y,map(lambda player:player.name,self.playersTeamA))}})
        self.send("rfidinput",{"head":'get_rfid'})
        
        
