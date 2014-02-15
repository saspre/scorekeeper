#main launcher
#import model.matches;

from model.matches import Match
match = Match();
print(match.match_pk)




import processes.match
import zmq, time

class ScoreKeeper:

	match = processes.match.Match();

	def start(self):
		self.match.start();



scorekeeper = ScoreKeeper();
scorekeeper.start();


time.sleep(1)
		
#  Socket to talk to server
print("Connecting to ")
context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.connect("tcp://localhost:5555")



socket.send(b"Hello")

socket.send(b"Hello")

socket.send(b"Hello")

socket.close();
context.term();