#!/usr/bin/python2
#main launcher
from processes.controller import ControllerProcess
from processes.input import KeyInputHandler 
from processes.display import DisplayProcess, MainView
from PySide import QtCore,QtDeclarative, QtGui
import zmq, time, sys
from addresses import *
from models import initSchema,initData



class ScoreKeeper():

    controller = ControllerProcess()
    
    
    def start(self):
        self.controller.start();

        # Start Key Input Listener (Possible Mock RFID reader)
        KeyInputHandler(getInputSocketAddr()).start()
        displayProcess = DisplayProcess(getDisplaySocketAddr())       
        displayProcess.start() 
        
        sys.exit( displayProcess.qApplication.exec_() ) ## Must be run from main thread
        

scorekeeper = ScoreKeeper();
scorekeeper.start();



        
### Example of socket communication to controller process
#context = zmq.Context.instance()
#socket = context.socket(zmq.PUSH)
#socket.connect("inproc://controller")
#socket.send_pyobj("Hello")


