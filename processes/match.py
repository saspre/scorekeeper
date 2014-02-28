#match.py

#Proccess for management of current match

import processes.sk_threading
import model.matches

class Match (processes.sk_threading.ZmqThread):

	

	def is_active():
		return self.is_active;

	def __init__(self):
		super(Match,self).__init__("match")
		self.is_active = False;
		self.match = model.matches.Match()


	def sk_run(self):
		print('Match is waiting for input:');
		incomming = self.socket.recv_pyobj()
		
		if(isinstance(incomming, model.matches.Match)):
			print("Match: received a match, starting match");
			self.start_match(incomming);
		elif (isinstance(incomming, str)):
			self.team_scored(incomming);
		else:
			print("We received something, but we are unsure what it is")

	def start_match(self, match):
		self.is_active = True;
		self.match = match;

	def team_scored(self,team='a'):
		print("Some scored it was team: " + team)
		if(team == 'a'):
			self.match.score_a += 1
		else:
			self.match.score_b += 1

		print("Score is now: %s - %s" % (self.match.score_a  ,self.match.score_b))
