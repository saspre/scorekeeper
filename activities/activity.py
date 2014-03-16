import zmq

class Activity:
    
    def __init__(self, controller):
        self.controller = controller
        
    def setLayout(self,layout):
        self.controller.sockets["display"].send_json({"header":"set_layout","data":layout})
        pass

