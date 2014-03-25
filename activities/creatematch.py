from red.activity import Activity
import traceback
from models.model import Match, Player, Team, Base, initSchema

class Creatematch(Activity):
    

    def onCreate(self,data):
        self.playersTeamA = []
        self.playersTeamB = []
        self.setLayout("match_setup")
        if data != None and len(data) > 0:
            for rfid in data:
                self.loadPlayer(rfid)
        self.send("rfidinput",{"head":'get_rfid'})
        

    def receiveDisplayMessage(self, message):

        if message["head"] == "echo":
            return 
        if message["data"] == "start_match":
            try:
                match = self.createMatch()
                self.switchActivity("match", data=match)   
            except Exception:
                self.session.rollback()
                self.logger.critical(traceback.format_exc())
        elif message["data"] == "okay":
            self.setLayout("match_setup")
            self.updateLayout()

            
    def createMatch(self):
        if len(self.playersTeamA) == 0 or len(self.playersTeamB) == 0:
            self.setLayout("error")
            self.invokeLayoutFunction("updateErrorMessage","Atleast two player \n are required")
            raise Exception("You need to add players to both teams you fool!")

        teamA = Team.createOrLoad(self.playersTeamA,self.session)
        teamB = Team.createOrLoad(self.playersTeamB,self.session)

        
        #Create Match
        match = Match(team_a = teamA, team_b = teamB, score_a = 0, score_b = 0)
   
        return match

        
    def receiveRfidinputMessage(self,message):
        if message["head"]=="player_rfid":
            self.loadPlayer(message["data"])
            
            
    def loadPlayer(self,playerRfid):
        player = Player.createOrLoad(playerRfid,self.session)
        if player not in self.playersTeamA and player not in self.playersTeamB:
            if(len(self.playersTeamB) < len(self.playersTeamA)):
                self.playersTeamB.append(player)
            else:
                self.playersTeamA.append(player)
        self.send("rfidinput",{"head":'get_rfid'})
        self.updateLayout()

    def updateLayout(self):
        if len(self.playersTeamA) > 0:
            self.send("display",{"head":"call_func","data":{"func":"updateTeamA","param":reduce(lambda x,y: x+"\n"+y,map(lambda player:player.name,self.playersTeamA))}})
        if len(self.playersTeamB) > 0:
            self.send("display",{"head":"call_func","data":{"func":"updateTeamB","param":reduce(lambda x,y: x+"\n"+y,map(lambda player:player.name,self.playersTeamB))}})
        
        
