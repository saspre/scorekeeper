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
            teamA = None
            teamB = None

            if len(self.teamARfid) == 0 or len(self.teamBRfid) == 0:
                raise Exception("You need to add players you fool")

            #Add new players to DB and add to team lists
            print self.teamARfid
            for rfid in self.teamARfid:
                if self.session.query(Player).filter(Player.rfid == rfid).count() <= 0:
                    self.session.add(Player(name=rfid,rfid=rfid))
                teamAPlayers.append(self.session.query(Player).filter(Player.rfid == rfid).one())
            
            for rfid in self.teamBRfid:
                if self.session.query(Player).filter(Player.rfid == rfid).count() <= 0:
                    self.session.add(Player(name=rfid,rfid=rfid))
                teamBPlayers.append(self.session.query(Player).filter(Player.rfid == rfid).one())
            
            #Check if teams exist in DB
            teamATeams = []
            teamBTeams = []
            
            for player in teamAPlayers:
                 teamATeams.append(player.teams)
                 
            for player in teamBPlayers:
                 teamBTeams.append(player.teams)
             
            intersectList = reduce(lambda xs,ys: filter(lambda x : x in xs,ys),teamATeams)
            for team in intersectList:
                #team exists, set as local team
                if team.size() == len(teamAPlayers):
                    teamA = team
                    break
                
            intersectList = reduce(lambda xs,ys: filter(lambda x : x in xs,ys),teamBTeams)
            for team in intersectList:
                #team exists, set as local team
                if team.size() == len(teamBPlayers):
                    teamB = team
                    break
            
            #team does not exist, so we add a new team
            if teamA == None:
                teamA = Team(name = "-")
                for player in teamAPlayers:
                    teamA.players.append(player)
                self.session.add(teamA)
            
            if teamB == None:
                teamB = Team(name = "-")
                for player in teamBPlayers:
                    teamB.players.append(player)
                self.session.add(teamB)    
            
            if teamA == None:
                raise Exception("Team A not set.")
            
            if teamB == None:
                raise Exception("Team B not set.")
            
            #Create Match
            match = Match(team_a = teamA, team_b = teamB, score_a = 0, score_b = 0)
   
            print(match)
            return match


    def new_player(self, name):
        self.session.add(Player(name = name))
        self.session.commit()


    def new_team(self, name_a, name_b, team_name):
        team = Team(name = team_name)
        self.session.add(team)
        players = self.session.query(Player).filter(Player.name.in_([name_a,name_b]))
        if players.count() != 2:
            print("Something amiss! Found " + players.count() + " players when expecting 2")
            self.session.rollback()
            return
        for player in players:
            team.players.append(player)
        self.session.commit()
        
    def processRfidMessage(self,message):
        if(message["header"]=="player_rfid"):
            self.loadPlayer(message["data"])
            
            
    def loadPlayer(self,playerRfid):
        #if(self.session.query(Player).filter(Player.id == playerId).count() > 0):
        if(len(self.teamBRfid) < len(self.teamARfid)):
            self.teamBRfid.append(playerRfid)
            self.controller.sockets["display"].send_json({"header":"call_func","data":{"func":"updateTeamB","param":reduce(lambda x,y: x+"\n" +y,self.teamBRfid)}})
        else:
            self.teamARfid.append(playerRfid)
            self.controller.sockets["display"].send_json({"header":"call_func","data":{"func":"updateTeamA","param":reduce(lambda x,y: x+"\n" +y,self.teamARfid)}})
        
        