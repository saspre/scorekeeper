#!/usr/bin/python2
#main launche


import time
import logging, logging.config
import sys
from red.config      import config
from PySide           import QtGui
from red.kernel      import Kernel



### Initialize Logger
logging.config.fileConfig('config/logging.conf')
logger = logging.getLogger(__file__)
logger.info("Zebra 14 is booting")

app = QtGui.QApplication(sys.argv)

kernel = Kernel()

##### This is QT load UI ######
services = config.get('Services','Services').split(",")
if "display" in services:
    logger.info("Zebra GUI is initiating")
    from red.mainwindow import MainWindow
    window = MainWindow.instance()
    window.show()
    logger.info('Zebra GUI initiated')

###############################


kernel.start()



###### This fellow must be run in the end ######
if "display" in services:
    sys.exit(app.exec_())


"""

class ScoreKeeper():

    controller = ControllerProcess()
    
    
    def start(self):
        self.qApplication = QtGui.QApplication( sys.argv )
        


      

        # Start Key Input Listener (Possible Mock RFID reader)
        #inputprocess = KeyInputHandler(getInputSocketAddr())
        inputprocess = RfidInput(getInputSocketAddr())
        displayProcess = DisplayProcess(getDisplaySocketAddr())    

        self.controller.start();

        window = MainWindow(displayProcess)
        window.show()

        displayProcess.start() 
        inputprocess.start()
        
        sys.exit( self.qApplication.exec_() ) ## Must be run from main thread
        

scorekeeper = ScoreKeeper();
scorekeeper.start();



        
### Example of socket communication to controller process
#context = zmq.Context.instance()
#socket = context.socket(zmq.PUSH)
#socket.connect("inproc://controller")
#socket.send_pyobj("Hello")


"""