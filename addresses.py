#addresses.py




INPUT_SOCKET_ADDR = "inproc://input_sock"
DISPLAY_SOCKET_ADDR = "inproc://displa_sock"


def getInputSocketAddr():
    return INPUT_SOCKET_ADDR


def getDisplaySocketAddr():
    return DISPLAY_SOCKET_ADDR