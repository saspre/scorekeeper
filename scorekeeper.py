#!/usr/bin/python2
#main launcher
#import model.matches;

import processes.match
import buttons

import zmq, time



class ScoreKeeper:

	match = processes.match.Match();

	def start(self):
		self.match.start();



scorekeeper = ScoreKeeper();
scorekeeper.start();



		
### Example of socket communication to match process
#context = zmq.Context.instance()
#socket = context.socket(zmq.PUSH)
#socket.connect("inproc://match")
#socket.send_pyobj("Hello")



#### input simulation

while True:
	inp = input()
	if(inp == 's'):
		buttons.start_game_clicked();
	if(inp == 'a'):
		buttons.team_a_score_clicked();
	if(inp == 'b'):
		buttons.team_b_score_clicked();
