from red.activity import Activity
import traceback
from models.model import Match, Player, Team, Base, initSchema

class Serial(Activity):
    
    def onCreate(self, data=None):
        self.setLayout("serial")
        self.send("rfidinput",{"head":'get_rfid'})
        
    def receiveRfidinputMessage(self, message):
        if message["head"]=="player_rfid":
            self.invokeLayoutFunction("updateSerial",message["data"])
            self.send("rfidinput",{"head":'get_rfid'})
            
    def receiveDisplayMessage(self, message):
        if message["head"]=="button_clicked" and message["data"] == "okay":
            self.switchActivity("mainmenu")
            
  
