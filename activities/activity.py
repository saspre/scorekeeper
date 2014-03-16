import zmq

class Activity:
    
    def __init__(self, controller):
        self.controller = controller
        
    def setLayout(self,layout):
        self.controller.sockets["display"].send_json({"header":"set_layout","data":layout})
        pass

    def switchActivity(self,activity,data=None):
    	self.controller.switchActivity(activity,data)

    @property
    def session(self):
        return self.controller.getSession()
   
