#sk_process


import threading, time


import zmq


class BaseProcess(threading.Thread):

    def __init__(self, name, context=None):
        super(BaseProcess, self).__init__()
        
        self.context = context or zmq.Context.instance();
        self.sock = self.context.socket(zmq.PAIR)
        self.sock.connect(name)
       


    def run(self):
        while True:
            try:
                message = self.sock.recv_json()
            except zmq.error.ContextTerminated:
                break;
            if message['header'] == "stop":
                return;
            elif message['header'] == "echo":
                self.sock.send_json({'header':'respond_echo'})
            else:
                self.processMessage(message);


"""
class ZmqThread (threading.Thread):
    
    def __init__(self, name):
        super().__init__()
    
        # Initialize socket for reading
        self.context = zmq.Context.instance()
        self.socket = self.context.socket(zmq.PULL)
        self.socket.bind("inproc://"+name)



    def run(self):
        while True:
            self.sk_run();
        
    def sk_run(self):
        raise Exception("Threads Must implement 'sk_run'");    



class DelayedThread (threading.Thread):
    
    def __init__(self, delay):
        super().__init__()
        self.delay = delay
    
    def run(self):
        while True:
            self.sk_run();
            time.sleep(self.delay);

    def sk_run(self):
        raise Exception("Threads Must implement 'sk_run'");    

"""