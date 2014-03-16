
from activities.activity import Activity


class ConfirmResultActivity (Activity):

    def onCreate(self, data=None):
        self.setLayout("confirm")
        self.match = data

    def processDisplayMessage(self,message):
        if message["header"] == "button_clicked":          
            if message["data"] == "confirm":
                self.saveMatch()
            elif message["data"] == "cancel":
                self.switchActivity("MatchActivity", self.match)
        
        else:
            print("We " + __file__ +" received something (message), but we are unsure what it is")
      
    def saveMatch(self):
        self.session.commit()
        self.switchActivity("CreateMatchActivity", self.match)