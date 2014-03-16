from activities.activity import Activity
from models import Match, Session, Player, Team, Base, initSchema

class MatchActivity(Activity):
    session = Session()
    match = None
    teamA = None
    teamB = None
    
    def onCreate(self,data=None):
        self.setLayout("match")
        teamAPlayers = []
        teamBPlayers = []
        
        #Add new players to DB and add to team lists
        for rfid in data["teamA"]:
            if self.session.query(Player).filter(Player.rfid=rfid).count() <= 0:
                session.add(Player(name=rfid,rfid=rfid))
            teamAPlayers.append(self.session.query(Player).filter(Player.rfid=rfid).one())
        
        for rfid in data["teamB"]:
            if self.session.query(Player).filter(Player.rfid=rfid).count() <= 0:
                session.add(Player(name=rfid,rfid=rfid))
            teamBPlayers.append(self.session.query(Player).filter(Player.rfid=rfid).one())
        
        #Check if teams exist in DB
        teamATeams = []
        teamBTeams = []
        
        for player in teamAPlayers:
             teamATeams.append(player.teams)
             
         for player in teamBPlayers:
             teamBTeams.append(player.teams)
         
        intersectList = [filer(lambda x: x in teamATeams[0], sublist) for sublist in teamATeams]
        for team in intersectList:
            #team exists, set as local team
            if team.size() == len(teamAPlayers):
                self.teamA = team
                break
            
        intersectList = [filer(lambda x: x in teamBTeams[0], sublist) for sublist in teamBTeams]
        for team in intersectList:
            #team exists, set as local team
            if team.size() == len(teamBPlayers):
                self.teamB = team
                break
        
        #team does not exist, so we add a new team
        if self.teamA == None:
            self.teamA = Team(name = "-")
            for player in teamAPlayers:
                self.teamA.players.append(player)
            session.add(self.teamA)
        
        if self.teamB == None:
            self.teamB = Team(name = "-")
            for player in teamBPlayers:
                self.teamB.players.append(player)
            session.add(self.teamB)    
        
        if self.teamA == None:
            raise Exception("Team A not set.")
        
        if self.teamB == None:
            raise Exception("Team B not set.")
        
        #Create Match
        self.match = Match(team_a = self.teamA, team_b = self.teamB, score_a = 0, score_b = 0)

    def processDisplayMessage(self,message):
        """
        if message["header"] == "start_match":
            self.start_match(message["data"]["team_a"],message["data"]["team_b"]);
        elif message["header"] == "a_scored":
            self.team_scored("a");
        elif message["header"] == "b_scored":
            self.team_scored("b");
        elif message["header"] == "end_match":
            self.end_match();
        elif message["header"] == "new_player":
            self.new_player(message["data"]["name"]);
        elif message["header"] == "new_team":
            if len(message["data"]["team_name"]) == 0:
                self.new_team(message["data"]["player_a"],message["data"]["player_b"],message["data"]["team_name"]);
            else:
                self.new_team(message["data"]["player_a"],message["data"]["player_b"],message["data"]["player_a"]+'+'+message["data"]["player_b"]);
        else:
            print("We (match) received something (message), but we are unsure what it is")
        print('Match is waiting for input:');
        """
        pass


    def end_match(self):
        if not self.is_active:
            print ("Unable to end match, no match in progress!")
            return
        self.is_active = False
        self.session.commit()
        print ("Ending match and saving the results at time: "+self.match.created_at.strftime("%Y-%m-%d %H:%M:%S"))
        self.match = None
        
    def team_scored(self, team):
        if not self.is_active:
            print ("No match in progress!")
            return
        if team == 'a':
            scoring_team = self.match.team_a;
            self.match.score_a = self.match.score_a + 1
        elif team == 'b':
            scoring_team = self.match.team_b;
            self.match.score_b = self.match.score_b + 1
        else:
            print ("Who the hell scored")
        print("Some scored it was team: " + scoring_team.name)
        print("Score is now: %s - %s" % (self.match.score_a  ,self.match.score_b))
        # Broadcast to display
        self.displaySocket.send_json(
            {"header":"score_update", 
            "data":{"a":self.match.score_a,
            "b":self.match.score_b}}
            )
   
        