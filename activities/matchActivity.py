from activities.activity import Activity

class MatchActivity(Activity):
    
    def processDisplayMessage(self,message):
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
        
    def onCreate(self, data):
        self.teamA = data["teamA"]
        self.teamB = data["teamB"]
        