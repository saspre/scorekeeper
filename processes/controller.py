#match.py

#Proccess for management of current match
import threading, zmq
from activities.createMatchActivity import CreateMatchActivity
from models import Match, Session, Player, Team, Base, initSchema
from sqlalchemy.orm import sessionmaker
from addresses import *


class ControllerProcess (threading.Thread):

    def __init__(self, context=None):
        super(ControllerProcess, self).__init__()
        
        self.is_active = False;
        self.match = Match()
        self.context = context or zmq.Context.instance()

        self.session = Session()

        self.inputSocket = self.context.socket(zmq.PAIR)
        self.inputSocket.bind(getInputSocketAddr())
        self.displaySocket = self.context.socket(zmq.PAIR)
        self.displaySocket.bind(getDisplaySocketAddr())
        self.poller = zmq.Poller()
        self.activity = CreateMatchActivity(self)
       

    def run(self):
        while True:
            try:
                poller_socks = dict(self.poller.poll(2))
            except KeyboardInterrupt:
                print("Received Key interrupt. Exiting")
                break

            try:
                message = self.displaySocket.recv_json()
            except zmq.error.ContextTerminated:
                break;

            if message["header"] == "stop":
                self.displaySocket.send_json({"header":"stop"})
                break;
            elif message['header'] == "echo":
                self.inputSocket.send_json({'header':'respond_echo'})
            else:
                self.activity.processDisplayMessage(message);


    def is_active(self):
        return self.is_active;

    def switch_activity(self, activity):
        self.activity = activity
        
    
        
