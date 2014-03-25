from red.activity import Activity
import traceback
from models.model import Match, Player, Team, Base, initSchema

class Creatematch(Activity):
    
    def onCreate(self, data=None):
        self.teamARfid = []
        self.teamBRfid = []
        self.setLayout("match_setup")
        

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
        teamAPlayers = []
        teamBPlayers = []

        if len(self.teamARfid) == 0 or len(self.teamBRfid) == 0:
            self.setLayout("error")
            self.invokeLayoutFunction("updateErrorMessage","Atleast two player \n are required")
            return 
            
        #Add new players to DB and add to team lists
        for rfid in self.teamARfid:
            teamAPlayers.append(Player.createOrLoad(rfid, self.session))
        
        for rfid in self.teamBRfid:
            teamBPlayers.append(Player.createOrLoad(rfid, self.session))
        
        teamA = Team.createOrLoad(teamAPlayers, self.session)
        teamB = Team.createOrLoad(teamBPlayers, self.session)
        
        #Create Match
        match = Match(team_a=teamA, team_b=teamB, score_a=0, score_b=0)
   
        return match

        
    def receiveRfidinputMessage(self,message):
        if message["head"]=="player_rfid":
            self.loadPlayer(message["data"])
            
            
    def loadPlayer(self,playerRfid):
        if(len(self.teamBRfid) < len(self.teamARfid)):
            self.teamBRfid.append(playerRfid)
        else:
            self.teamARfid.append(playerRfid)
        self.updateLayout()

    def updateLayout(self):
        self.send("display", {"head":"call_func","data":{"func":"updateTeamB","param":"\n".join(self.teamBRfid)}})
        self.send("display", {"head":"call_func","data":{"func":"updateTeamA","param":"\n".join(self.teamARfid)}})
        
        
