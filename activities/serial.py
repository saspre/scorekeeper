from red.activity import Activity
import traceback
from models.model import Match, Player, Team, Base, initSchema

class Serial(Activity):
    
    def onCreate(self, data=None):
        self.teamARfid = []
        self.teamBRfid = []
        self.setLayout("serial")
        
    def receiveRfidinputMessage(self, message):
        if message["head"]=="player_rfid":
            self.invokeLayoutFunction("updateSerial",message["data"])
            
    def receiveDisplayMessage(self, message):
        if message["head"]=="button_clicked" and message["data"] == "okay":
            self.switchActivity("mainmenu")
            
  
