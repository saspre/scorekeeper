



import sys

from PySide.QtCore import QThread, Signal, Slot, QObject
from PySide import QtCore, QtGui, QtUiTools, QtDeclarative 
from processes.baseProcess import BaseProcess


class MainWindow(QtGui.QMainWindow):
  

    def __init__(self, displayProcess):
        super(MainWindow, self).__init__(None)
        self.context = None
        self.displayProcess = displayProcess
        self.centralWidget = QtGui.QStackedWidget()
        self.setCentralWidget(self.centralWidget)
        

        self.setLayout("main")
        
        #if config.get("GUI","fullscreen") == "true":
        #    self.showFullScreen()
        #else:
        self.resize(480,272)
        self.displayProcess.functionSignal.connect(self.functionCall)
        self.displayProcess.layoutSignal.connect(self.setLayout)
        
     
    def functionCall(self, functionName, param):
        func = eval("self.view.rootObject()." + functionName)
        func(param)

    def setLayout(self, layout):
        
        self.view = QtDeclarative.QDeclarativeView()
        self.view.setSource(QtCore.QUrl.fromLocalFile( './interface/'+ layout +'.qml' ))
        self.view.setResizeMode( QtDeclarative.QDeclarativeView.SizeRootObjectToView )   

        qcontext = self.view.rootContext() 
        qcontext.setContextProperty("context",self.displayProcess)
 
        self.centralWidget.addWidget(self.view)
        self.centralWidget.setCurrentWidget(self.view)


class DisplayProcess(BaseProcess, QThread, QObject):

    layoutSignal = Signal(object)
    functionSignal = Signal(str,str)

    
    def __init__(self, name, context=None):
        super(DisplayProcess, self).__init__(name=name, context=context)
       
        
    def processMessage(self, message):
        if message["header"] == "set_layout":
            self.layoutSignal.emit(message["data"])
            return True
        elif message["header"] == "call_func":
            self.functionSignal.emit(message["data"]["func"],str(message["data"]["param"])) 
            return True
        else:
            return False

    @Slot(str)
    def onClicked(self, btn):
        print btn
        message = {"header":"button_clicked","data":btn}
        self.send(message)
        

