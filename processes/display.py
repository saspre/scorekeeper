



import sys
from PySide import QtCore,QtDeclarative, QtGui
from processes.baseProcess import BaseProcess


class QtScoreInterface(QtCore.QObject ):
    def __init__(self, socket):
        QtCore.QObject.__init__(self)
        self.socket = socket

    @QtCore.Slot()
    def aScored(self):
        print ("A_scored");

    @QtCore.Slot()
    def bScored(self):
        print ("B_scored");


class MainWindow( QtDeclarative.QDeclarativeView ):
    def __init__( self, parent=None):
        super( MainWindow, self ).__init__( parent )
        self.setWindowTitle( "Test" )
        self.setSource( QtCore.QUrl.fromLocalFile( './interface/main.qml' ) )
        self.setResizeMode( QtDeclarative.QDeclarativeView.SizeRootObjectToView )
       

class DisplayProcess(BaseProcess):

    def __init__(self, name, context=None, app=None, window=None):
        super(DisplayProcess, self).__init__(name,context)
        self.app = app
        self.window = window
        self.qcontext = self.window.rootContext()
        self.qcontext.setContextProperty("qScoreInterface",QtScoreInterface(self.sock))

    def run(self):
        
        super(DisplayProcess,self).run();
    
    def processMessage(self):
        pass # Ignore so far
