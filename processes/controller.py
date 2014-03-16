#match.py

#Proccess for management of current match
import threading, zmq
from activities.createMatchActivity import CreateMatchActivity
from activities.matchActivity import MatchActivity
from activities.confirmResultActivity import ConfirmResultActivity

from sqlalchemy.orm import sessionmaker
from addresses import *
from models import Session

class ControllerProcess (threading.Thread):

    def __init__(self, context=None):
        super(ControllerProcess, self).__init__()
        self.session = None
        self.is_active = False;
      
        self.context = context or zmq.Context.instance()

        
        self.sockets = dict()
    
        self.poller = zmq.Poller()

        self.createSocket("rfid", getInputSocketAddr())
        self.createSocket("display", getDisplaySocketAddr())
        
    def createSocket(self, name, address):
        self.sockets[name] = self.context.socket(zmq.PAIR)
        self.sockets[name].bind(address)
        self.poller.register(self.sockets[name], zmq.POLLIN)
       
    def getSession(self):
        if self.session == None:
            self.session = Session() 
        return self.session

    def run(self):
        self.switchActivity("CreateMatchActivity")
        while True:
            try:
                poller_socks = dict(self.poller.poll(2))
            except KeyboardInterrupt:
                print("Received Key interrupt. Exiting")
                break

            for key in self.sockets:
                if self.sockets[key] in poller_socks:
                    try:
                        message = self.sockets[key].recv_json()
                    except zmq.error.ContextTerminated:
                        break;
        
                    if message["header"] == "stop":
                        self.sockets[key].send_json({"header":"stop"})
                        break;
                    elif message['header'] == "echo":
                        self.sockets[key].send_json({'header':'respond_echo'})
                    else:
                        eval("self.activity.process" + key.title() + "Message")(message);


    def switchActivity(self, activity, data = None):
        self.activity = eval(activity)(self)
        self.activity.onCreate(data)
        
    
        
