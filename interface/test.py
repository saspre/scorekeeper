

import sys
from PySide import QtCore,QtDeclarative, QtGui

class QtScoreInterface(QtCore.QObject ):

    signaller_score_a = QtCore.Signal(str)
    signaller_score_b = QtCore.Signal(str)


    def __init__(self):
        QtCore.QObject.__init__(self)
        self.score_a = 0
        self.score_b = 0
  
    @QtCore.Slot()
    def aScored(self):
        print ("A_scored");
        self.score_a += 1
        self.updateScore()
        

    @QtCore.Slot()
    def bScored(self):
        print ("B_scored");
        self.score_b += 1
        self.updateScore()
        

    @QtCore.Slot()
    def startMatch(self):
        print ("Game start stopped");
      
       
    def updateScore(self):
        self.signaller_score_a.emit(str(self.score_a))
        self.signaller_score_b.emit(str(self.score_b))


class MainView( QtDeclarative.QDeclarativeView ):
    def __init__( self, parent=None):
        super( MainView, self ).__init__( parent )
        self.setWindowTitle( "ScoreKeeper" )
        self.setSource( QtCore.QUrl.fromLocalFile( './main.qml' ) )
        self.setResizeMode( QtDeclarative.QDeclarativeView.SizeRootObjectToView )
        

qApplication = QtGui.QApplication( sys.argv )
window = MainView()
window.show();
       
qcontext = window.rootContext() 
interface = QtScoreInterface()
qcontext.setContextProperty("qScoreInterface",interface)
    
interface.signaller_score_a.connect(window.rootObject().updateScoreA)
interface.signaller_score_b.connect(window.rootObject().updateScoreB)

sys.exit( qApplication.exec_() )