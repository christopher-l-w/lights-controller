#
#   Lights Controller client in Python
#   Connects REQ socket to tcp server at provided IP address and port 5555
#   Sends "ON" or "OFF" to server
#

import zmq
import sys

context = zmq.Context()

# read IP from CMD line python3 main.py IP
if len(sys.argv) > 1:
    server_ip = sys.argv[1]
else:
    server_ip = "raspberrypi.local"

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.PUSH)
socket.connect("tcp://%s:5555" % server_ip)

while True:
    light_state = input("Enter light state (ON/OFF): ")
    print("Sending request: %s" % light_state)
    socket.send_string(light_state)
