#!/usr/bin/python2
#main launcher
from processes.match import MatchProcess
from processes.input import KeyInputHandler 
import database

import zmq, time

MATCH_SOCKET_ADDR = "inproc://match"

database.initDatabase()

class ScoreKeeper():

    match = MatchProcess(MATCH_SOCKET_ADDR)
    
    
    def start(self):
        self.match.start();
        KeyInputHandler(MATCH_SOCKET_ADDR).start()



scorekeeper = ScoreKeeper();
scorekeeper.start();



        
### Example of socket communication to match process
#context = zmq.Context.instance()
#socket = context.socket(zmq.PUSH)
#socket.connect("inproc://match")
#socket.send_pyobj("Hello")


