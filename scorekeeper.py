#!/usr/bin/python2
#main launcher
#import model.matches;

from processes.match import MatchProcess
from processes.input import KeyInputHandler 
from processes.display import DisplayProcess, MainView
from PySide import QtCore,QtDeclarative, QtGui
import zmq, time, sys

from addresses import *

class ScoreKeeper():

    match = MatchProcess()
    
    
    def start(self):
        self.match.start();

        # Start Key Input Listener (Possible Mock RFID reader)
        KeyInputHandler(getInputSocketAddr()).start()
      
        displayProcess = DisplayProcess(getDisplaySocketAddr())       
        displayProcess.start() 
        
        sys.exit( displayProcess.qApplication.exec_() ) ## Must be run from main thread
        

scorekeeper = ScoreKeeper();
scorekeeper.start();



        
### Example of socket communication to match process
#context = zmq.Context.instance()
#socket = context.socket(zmq.PUSH)
#socket.connect("inproc://match")
#socket.send_pyobj("Hello")


