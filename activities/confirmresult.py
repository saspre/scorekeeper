
from red.activity import Activity


class Confirmresult (Activity):

    def onCreate(self, data=None):
        """ onCreate"""
        self.setLayout("confirm")
        self.match = data
        #self.invokeLayoutFunction("updateMatchResult",str(self.match.score_a) + " - " + str(self.match.score_b))
        self.updateMatchResult

    def receiveDisplayMessage(self,message):
        if message["head"] == "button_clicked":          
            if message["data"] == "confirm":
                self.saveMatch()
            elif message["data"] == "cancel":
                self.switchActivity("match", data=self.match)
        
        else:
            self.logger.critical("We " + __file__ +" received something (message), but we are unsure what it is")
      
    def saveMatch(self):
        self.session.commit()
        self.switchActivity("creatematch", data=self.match)