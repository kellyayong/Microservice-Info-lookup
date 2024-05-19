#
#   Example program of a Personality client in Python
#   Connects REQ socket to tcp://localhost:5000
#   Sends personality type to server, expects personality info back
#
import zmq
import pymsgbox


# Create context
context = zmq.Context()

#  Socket to talk to server
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5000")


# Set the personality type requesting for info as the request manually
request = 'type1'

# Send request and wait for response
print(f"Searching for personality {request} ...")
socket.send_string(request)

# Get reply and print in CLI
message = socket.recv_string()
print(f"Your Personality type is: {request}\n [ {message} ]")

# Or write response to a text file
with open('personality-result.txt', 'w') as file:
    file.write(message)


# Or display as pop up message box
pymsgbox.alert(message, request)
