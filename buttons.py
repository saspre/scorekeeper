#buttons.py

"""
Something magically will activate these functions when 
a button is clicked. A state pattern can be implemented if needed. 
"""


import model.matches
import zmq

socket = zmq.Context.instance().socket(zmq.PUSH)
socket.connect("inproc://match")

def start_game_clicked():
	socket.send_pyobj(model.matches.Match())



def team_a_score_clicked():
	socket.send_pyobj('a')

def team_b_score_clicked():
	socket.send_pyobj(('b'))


