#sk_process


import threading, time


import zmq



class Thread (threading.Thread):
	
	def __init__(self, name):
		super().__init__()
	

		self.context = zmq.Context()

		print("Connecting to " + name + " server")
		self.socket = self.context.socket(zmq.PULL)
		self.socket.bind("tcp://*:5555")



	def run(self):
		while True:
			self.sk_run();
		



	def sk_run(self):
		raise Exception("Threads Must implement 'sk_run'");	



class DelayedThread (threading.Thread):
	
	def __init__(self, delay):
		super().__init__()
		self.delay = delay;

		

	

	def run(self):
		while True:
			self.sk_run();
			time.sleep(self.delay);



	def sk_run(self):
		raise Exception("Threads Must implement 'sk_run'");	