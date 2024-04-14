#
#   Lights Controller client in Python
#   Connects REQ socket to tcp server at provided IP address and port 5555
#   Sends "ON" or "OFF" to server
#

import zmq
import sys

context = zmq.Context()

# read IP from CMD line python3 main.py IP
server_ip = sys.argv[1]

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://%s:5555" % server_ip)

while True:
    light_state = input("Enter light state (ON/OFF): ")
    print("Sending request %s …" % light_state)
    socket.send(light_state.encode())
    message = socket.recv()
    print("Received reply [ %s ]" %  (message))
