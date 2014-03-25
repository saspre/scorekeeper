


from red.activity import Activity


class Mainmenu(Activity):
    """ MainMenu """

    def onCreate(self, data=None):
        """ onCreate"""
        self.setLayout("mainmenu")
       
    def receiveDisplayMessage(self, message):
        """ Receives stuff """
        if message["head"] == "button_clicked":          
            if message["data"] == "new_match":
                self.switchActivity("creatematch")
            elif message["data"] == "cancel":
                self.switchActivity("recent")
            elif message["data"] == "get_serial":
                self.switchActivity("serial")
        else:
            self.logger.critical("We " + __file__ +" received something (message), but we are unsure what it is")
