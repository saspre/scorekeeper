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
        KeyInputHandler(getInputSocketAddr()).start()
        app = QtGui.QApplication( sys.argv )
        window = MainView()
        DisplayProcess(getDisplaySocketAddr(),app=app, window=window).start()
        window.show()
       
        
        sys.exit( app.exec_() )



scorekeeper = ScoreKeeper();
scorekeeper.start();



        
### Example of socket communication to match process
#context = zmq.Context.instance()
#socket = context.socket(zmq.PUSH)
#socket.connect("inproc://match")
#socket.send_pyobj("Hello")


