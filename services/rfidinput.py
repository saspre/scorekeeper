

from red.services.base import Service

import zmq, json, threading

class Rfidinput (Service, threading.Thread):




    def start_game_clicked(self):
        team_a = raw_input("Enter team a name:")
        team_b = raw_input("Enter team b name:")
        self.sock.send_json({"head":"start_match","data":{"team_a":team_a,"team_b":team_b}})

    def team_clicked(self):
        player_a = raw_input("Enter player a name:")
        player_b = raw_input("Enter player b name:")
        team_name = raw_input("Enter team name:")
        self.sock.send_json({"head":"new_team","data":{"player_a":player_a,"player_b":player_b,"team_name":team_name}})

    def player_clicked(self):
        name = raw_input("Enter player name:")
        self.sock.send_json({"head":"new_player","data":{"name":name}})

    def team_a_score_clicked(self):
        self.sock.send_json({"head":'a_scored'})

    def team_b_score_clicked(self):
        self.sock.send_json(({"head":'b_scored'}))

    def end_game_clicked(self):
        self.sock.send_json(({"head":'end_match'}))




    # Overrides run, so doesn't wait for messages
    def run(self):
        try:
            while True:
                rin = raw_input("")
                self.send({"head":"player_rfid","data":rin})
                #print("rfidInput file")
                #TODO: Check for correct input syntax
        except zmq.error.ContextTerminated:
            return
