import zmq

class Activity:
    
    def __init__(self, controller):
        self.controller = controller
        
    def setLayout(self,layout):
        self.controller.displaySocket.send_json({"header":"set_layout","data":layout})