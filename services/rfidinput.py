#rfidinput.py

from red.services.base import Service

import zmq, json, threading

class Rfidinput (Service, threading.Thread):

    # Overrides run, so doesn't wait for messages
    def run(self):
        try:
            while True:
                rin = raw_input("")
                #TODO: Check for correct input syntax
                self.send({"head":"player_rfid","data":rin})
        except zmq.error.ContextTerminated:
            return
