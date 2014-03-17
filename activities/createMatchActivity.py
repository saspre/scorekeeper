from activities.activity import Activity
import traceback
from models import Match, Session, Player, Team, Base, initSchema

class CreateMatchActivity(Activity):
    
    def onCreate(self,data):
        self.teamARfid = []
        self.teamBRfid = []
        self.setLayout("match_setup")
        

    def processDisplayMessage(self,message):
        if(message["data"]=="start_match"):
            print("Start Match Button Pressed")
            try:
                match = self.createMatch()
                self.switchActivity("MatchActivity", match)   
            except Exception:
                self.session.rollback()
                print(traceback.format_exc())

            
    def createMatch(self):
            teamAPlayers = []
            teamBPlayers = []

            if len(self.teamARfid) == 0 or len(self.teamBRfid) == 0:
                raise Exception("You need to add players you fool")

            #Add new players to DB and add to team lists
            for rfid in self.teamARfid:
                teamAPlayers.append(Player.createOrLoad(rfid,self.session))
            
            for rfid in self.teamBRfid:
                teamBPlayers.append(Player.createOrLoad(rfid,self.session))
            
            teamA = Team.createOrLoad(teamAPlayers,self.session)
            teamB = Team.createOrLoad(teamBPlayers,self.session)
            
            #Create Match
            match = Match(team_a = teamA, team_b = teamB, score_a = 0, score_b = 0)
   
            print(match)
            return match

        
    def processRfidMessage(self,message):
        if(message["header"]=="player_rfid"):
            self.loadPlayer(message["data"])
            
            
    def loadPlayer(self,playerRfid):
        if(len(self.teamBRfid) < len(self.teamARfid)):
            self.teamBRfid.append(playerRfid)
            self.controller.sockets["display"].send_json({"header":"call_func","data":{"func":"updateTeamB","param":"\n".join(self.teamBRfid)}})
        else:
            self.teamARfid.append(playerRfid)
            self.controller.sockets["display"].send_json({"header":"call_func","data":{"func":"updateTeamA","param":"\n".join(self.teamARfid)}})
        
        