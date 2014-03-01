
import sys
from PySide import QtGui

class Window(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.textEdit = QtGui.QTextEdit('Text Edit')
        self.listWidget = QtGui.QListWidget()
        self.listWidget.addItem('List Widget')
        self.label = QtGui.QLabel('Label')

        self.stackedLayout = QtGui.QStackedLayout()
        self.stackedLayout.addWidget(self.textEdit)
        self.stackedLayout.addWidget(self.listWidget)
        self.stackedLayout.addWidget(self.label)

        self.frame = QtGui.QFrame()
        self.frame.setLayout(self.stackedLayout)

        self.button1 = QtGui.QPushButton('Text Edit')
        self.button1.clicked.connect(lambda: self.stackedLayout.setCurrentIndex(0))
        self.button2 = QtGui.QPushButton('List Widget')
        self.button2.clicked.connect(lambda: self.stackedLayout.setCurrentIndex(1))
        self.button3 = QtGui.QPushButton('Label')
        self.button3.clicked.connect(lambda: self.stackedLayout.setCurrentIndex(2))

        buttonLayout = QtGui.QHBoxLayout()
        buttonLayout.addWidget(self.button1)
        buttonLayout.addWidget(self.button2)
        buttonLayout.addWidget(self.button3)

        layout = QtGui.QVBoxLayout(self)
        layout.addLayout(buttonLayout)
        layout.addWidget(self.frame)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    w = Window()
    w.show()

    sys.exit(app.exec_())

"""
# - * - Coding: utf-8 - * -
import sys
from  PySide  import  QtGui ,  QtCore
class  MainWindow ( QtGui . QMainWindow ):

    def __init__(self , Parent = None ):
        super ( MainWindow ,  self ). __init__ ( Parent )
        self . setWindowTitle ( 'StackedWidget' )
        self . resize ( 800 ,  600 )
        # I want to create three widgets to switch
        page1 =  self.Create_widget ( 'Page 1' ,  '#DBD9C0' )
        page2 =  self.Create_widget ( 'Page 2' ,  '#739032' )
        page3 =  self.Create_widget ( 'Page 3' ,  '#340A0A' )
        # Create QStackedWidget, you add a widget to switch
        Stacked =  QtGui . QStackedWidget ()
        Stacked . addWidget ( page1 )
        Stacked . addWidget ( page2 )
        Stacked . addWidget ( page3 )
        # Create a combo box to switching
        combo =  QtGui . QComboBox ()
        combo . addItem ( 'Page 1' )
        combo . addItem ( 'Page 2' )
        combo . addItem ( 'Page 3' )
        # The value of the combo box until it changes, I will change the widget to view the QStackedWidget
        self . connect ( combo ,  QtCore . SIGNAL ( "CurrentIndexChanged (int)" ), Stacked ,  QtCore . SLOT ( "setCurrentIndex (int)" ))
        # Layout for display
        layout =  QtGui . QVBoxLayout ()
        layout . addWidget ( combo )
        layout . addWidget ( Stacked )
        # Main widget
        Main_widget =  QtGui . QWidget ()
        Main_widget . setLayout ( layout )
        self . setCentralWidget ( Main_widget )

    def Create_widget ( self , Label_str , BG_Color ):
      
      
        widget =  QtGui . QWidget ()
        # In order to give a background color to be easy to see it switched to create a palette
        palette =  QtGui . QPalette ()
        palette . setColor ( QtGui . QPalette . Background ,  QtGui . QColor ( BG_Color ))
        # Set the palette widget
        widget . setAutoFillBackground ( True )
        widget . setPalette ( palette )
        # Label also add in passing
        Label =  QtGui . QLabel ( widget )
        Label . setText ( Label_str )
        return widget

if __name__ ==  '__main__' :
    app =  QtGui . QApplication ( sys . argv )
    Main_window =  MainWindow ()
    Main_window . show ()
    sys . exit ( app . exec_())

    """