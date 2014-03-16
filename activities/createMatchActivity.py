from activities.activity import Activity

class CreateMatchActivity(Activity):
    
    #def __init__(self,controller):
    #    super(CreateMatchActivity,self).__init__(controller = controller)
    #    teamAPlayers = []
    #    teamBPlayers = []
    
    def onCreate(self,data):
        self.setLayout("match_setup")
        teamAPlayers = []
        teamBPlayers = []
        
    def processDisplayMessage(self,message):
        if(message["data"]=="start_match"):
            print("Start Match Button Pressed")
                
    
    def start_match(self,teama,teamb):
        if self.is_active:
            print ("Unable to start match, already in progress!")
            #self.end_match()
            return
        team_a = self.session.query(Team).filter(Team.name == teama).one()
        team_b = self.session.query(Team).filter(Team.name == teamb).one()
        self.is_active = True
        self.match = Match( team_a = team_a, score_a = 0,\
                            team_b = team_b, score_b = 0)
        self.session.add(self.match)
        self.controller.switch_activity("MatchActivity", {"teamA":self.teamA,"teamB":self.teamB})
        print("Match: received a match, starting match between: "+team_a.name+" and "+team_b.name )
        
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
        
    def processRFIDMessage(self,message):
        if(message["header"]=="player_id"):
            self.loadPlayer(message["data"])
            
            
    def loadPlayer(self,playerId):
        #if(self.session.query(Player).filter(Player.id == playerId).count() > 0):
        teamAPlayers.append(playerId)
        self.controller.displaySocket.send_json({"header":"call_func","data":{"func":"updateTeamA","param":playerId}})
        