
from red.activity import Activity


class Confirmresult (Activity):

    def onCreate(self, data=None):
        self.setLayout("confirm")
        self.match = data

    def receiveDisplayMessage(self,message):
        if message["head"] == "button_clicked":          
            if message["data"] == "confirm":
                self.saveMatch()
            elif message["data"] == "cancel":
                self.switchActivity("match", self.match)
        
        else:
            print("We " + __file__ +" received something (message), but we are unsure what it is")
      
    def saveMatch(self):
        self.session.commit()
        self.switchActivity("creatematch", self.match)