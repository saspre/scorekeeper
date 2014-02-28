


from processes.baseProcess import BaseProcess

import zmq, json

class KeyInputHandler (BaseProcess):




    def start_game_clicked(self):
        self.sock.send_json({"header":"start_match"})

    def team_a_score_clicked(self):
        self.sock.send_json({"header":'a_scored'})

    def team_b_score_clicked(self):
        self.sock.send_json(({"header":'b_scored'}))

    def end_game_clicked(self):
        self.sock.send_json(({"header":'end_match'}))




    # Overrides run, so doesn't wait for messages
    def run(self):
        try:
            while True:
                rin = raw_input("in:")
                for inp in list(rin):            
                    if(inp == 's'):
                        self.start_game_clicked();
                    if(inp == 'a'):
                        self.team_a_score_clicked();
                    if(inp == 'b'):
                        self.team_b_score_clicked();
                    if(inp == 'e'):
                        self.end_game_clicked();

                    if inp == 'q':
                        #logger.info("Shutting down KeyInputHandler")
                        #self.sock.close();
                        self.sock.send_json({"header":"stop"})
                        return
                    
        except zmq.error.ContextTerminated:
            return
