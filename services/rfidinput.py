#lpc.py

from red.services.base import Service

import zmq, json, threading

#class Rfidinput (Service, threading.Thread):
#    """
#    Reads from RFID reader. Currently mocked through keyboard inputs
#    """
#
#    def processMessage(self, message):
#        print(message)
#        if(message['head'] == "get_rfid"):
#            self.getRfid()
#        else:
#            return False
#
#    def getRfid(self):
#        try:
#            rin = input("")
#            print (rin)
#            #TODO: Check for correct input syntax
#            self.send({"head":"player_rfid","data":rin})
#        except zmq.error.ContextTerminated:
#            return
#        except SyntaxError:
#            self.send({"head":"stop"})
