#match.py

#Proccess for management of current match

import threading, zmq
from model.matches import Match


class MatchProcess (threading.Thread):

    def __init__(self, name, context=None):
        super(MatchProcess, self).__init__()
        
        self.is_active = False;
        self.match = Match()
        self.context = context or zmq.Context.instance()
        self.sock = self.context.socket(zmq.PAIR)
        self.sock.bind(name)
       


    def run(self):
        while True:
            try:
                message = self.sock.recv_json()

            except zmq.error.ContextTerminated:
                break;
            if message["header"] == "stop":
                break;
            elif message['header'] == "echo":
                self.sock.send_json({'header':'respond_echo'})
            else:
                self.processMessage(message);




    def is_active(self):
        return self.is_active;


    def processMessage(self,message):
        print('Match is waiting for input:');
        
        
        if message["header"] == "start_match":
            print("Match: received a match, starting match");
            self.start_match();
        elif message["header"] == "a_scored":
            self.team_scored("a");
        elif message["header"] == "b_scored":
            self.team_scored("b");
        elif message["header"] == "end_match":
            self.end_match();
        else:
            print("We received something, but we are unsure what it is")

    def start_match(self):
        if self.is_active:
            print ("Unable to start match, already in progress!")
            return
        self.is_active = True;
        self.match = Match();

    def end_match(self):
        self.is_active = False;
        #Save to

    def team_scored(self, team):
        if not self.is_active:
            print ("No match in progress!")
            return
        print("Some scored it was team: " + team)
        if team == 'a':
            self.match.score_a += 1
        elif team == 'b':
            self.match.score_b += 1
        else:
            print ("Who the hell scored")
        print("Score is now: %s - %s" % (self.match.score_a  ,self.match.score_b))
