



import sys
from PySide import QtCore,QtDeclarative, QtGui
from processes.baseProcess import BaseProcess


class QtScoreInterface(QtCore.QObject ):

    signaller_score_a = QtCore.Signal(str)
    signaller_score_b = QtCore.Signal(str)

    def __init__(self, socket):
        QtCore.QObject.__init__(self)
        self.socket = socket
  
    @QtCore.Slot()
    def aScored(self):
        print ("A_scored");
        self.socket.send_json({"header":"a_scored"})

    @QtCore.Slot()
    def bScored(self):
        print ("B_scored");
        self.socket.send_json({"header":"b_scored"})

    @QtCore.Slot()
    def startMatch(self):
        print ("Game start stopped");
        self.socket.send_json({"header":"start_match"})
       
    def updateScore(self, a, b):
        self.signaller_score_a.emit(str(a))
        self.signaller_score_b.emit(str(b))


class MainView( QtDeclarative.QDeclarativeView ):
    def __init__( self, parent=None):
        super( MainView, self ).__init__( parent )
        self.setWindowTitle( "Test" )
        self.setSource( QtCore.QUrl.fromLocalFile( './interface/main.qml' ) )
        self.setResizeMode( QtDeclarative.QDeclarativeView.SizeRootObjectToView )
       

class DisplayProcess(BaseProcess):

    def __init__(self, name, context=None):
        super(DisplayProcess, self).__init__(name,context)
        #http://pyqt.sourceforge.net/Docs/PyQt4/qml.html
        #http://stackoverflow.com/questions/10506398/pyside-signal-argument-cant-be-retrieved-from-qml

        self.qApplication = QtGui.QApplication( sys.argv )
        self.window = MainView()
        self.window.show();
        
        self.qcontext = self.window.rootContext() #is this needed?
        self.interface = QtScoreInterface(self.sock)
        self.qcontext.setContextProperty("qScoreInterface",self.interface)
     
        self.interface.signaller_score_a.connect(self.window.rootObject().updateScoreA)
        self.interface.signaller_score_b.connect(self.window.rootObject().updateScoreB)


    def run(self): 
        super(DisplayProcess,self).run();


    def processMessage(self, msg):
        if msg["header"] == "score_update":
            self.interface.updateScore(
                a=msg["data"]["a"],
                b=msg["data"]["b"]
                )
