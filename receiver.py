#
#   Personality client in Python
#   Connects REQ socket to tcp://localhost:5554
#   Sends personality type to server, expects personality info back
#

import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to personality lookup server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5000")

while True:
    # Set file path
    file_path = 'personality-type.txt'

    # Open file to see if there is a requested personality type
    with open(file_path, 'r') as file:
        personality_type = file.read()
        if personality_type != '':
            # Set request as the personality type
            request = personality_type

            # Send request and wait for response
            # print(f"Sending request {request} …")
            print(f"Searching for personality {request} …")
            socket.send_string(request)

            # Get reply
            message = socket.recv_string()
            # print(f"Received reply [ {message} ]")
            print(f"Your Personality type is: {request} \n [ {message} ]")

    # Clear file after done with personality type
    with open(file_path, 'w') as file:
        file.write('')
