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
            if self.session.query(Player).filter(Player.rfid == rfid).count() <= 0:
                self.session.add(Player(name=rfid,rfid=rfid))
            teamAPlayers.append(self.session.query(Player).filter(Player.rfid == rfid).one())
        
        for rfid in data["teamB"]:
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
                self.teamA = team
                break
            
        intersectList = reduce(lambda xs,ys: filter(lambda x : x in xs,ys),teamBTeams)
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
            self.session.add(self.teamA)
        
        if self.teamB == None:
            self.teamB = Team(name = "-")
            for player in teamBPlayers:
                self.teamB.players.append(player)
            self.session.add(self.teamB)    
        
        if self.teamA == None:
            raise Exception("Team A not set.")
        
        if self.teamB == None:
            raise Exception("Team B not set.")
        
        #Create Match
        self.match = Match(team_a = self.teamA, team_b = self.teamB, score_a = 0, score_b = 0)
        print(self.match)

    def processDisplayMessage(self,message):
        if message["header"] == "button_clicked":          
            if message["data"] == "a_scored":
                self.team_scored("a");
            elif message["data"] == "b_scored":
                self.team_scored("b");
            elif message["data"] == "end_match":
                self.end_match();
            elif message["data"] == "confirm":
                self.save_match()
            elif message["data"] == "cancel":
                self.setLayout("match")
        
        else:
            print("We (match) received something (message), but we are unsure what it is")
      
    

    def end_match(self):
               
        print ("Ending match and saving the results at time: "+self.match.created_at.strftime("%Y-%m-%d %H:%M:%S"))
        self.switchLayout("finished")
        
    def team_scored(self, team):
       
        if team == 'a':
            scoring_team = self.match.team_a;
            self.match.score_a = self.match.score_a + 1
            func = "updateScoreA"
            score = self.match.score_a
        elif team == 'b':
            scoring_team = self.match.team_b;
            self.match.score_b = self.match.score_b + 1
            func = "updateScoreB"
            score = self.match.score_b
        else:
            print ("Who the hell scored")
        
        print("Some scored it was team: " + scoring_team.name)
        print("Score is now: %s - %s" % (self.match.score_a  ,self.match.score_b))
        # Broadcast to display

        message =  {"header":"call_func", 
                    "data":{"func":func,
                            "param":score}}

        self.controller.sockets["display"].send_json(message)
   
        