import zmq
from processes.controller import ControllerProcess

class Activity:
    
    def __init__(self, controller):
        assert controller is ControllerProcess, "Controller is not the ControllerProcess"
        self.controller = controller
        
    