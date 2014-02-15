#match.py

#Proccess for management of current match

import processes.sk_threading

class Match (processes.sk_threading.Thread):

	def __init__(self):
		super().__init__("match")

	def sk_run(self):
		print('Match Started, waiting for input:');
		message = self.socket.recv()
		print("Message received: %s" % message)	

