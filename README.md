# Microservice Personality Info Lookup

CS361 Sprint 2 - Personality Info Lookup Microservice uses ZeroMQ for the communication pipe. Receiver will read the personality type written in a text file, sends it to the server that looks up the corresponding info in a csv file and sends it back to the receiver.

## Socket Setup

Use the following code to create a ZeroMQ request socket:

```
import zmq

# Create context
context = zmq.Context()

#  Socket to talk to server
print("Connecting to personality lookup server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5000")
```

## Request Data

Once connection is established, receiver will read the personality-type.txt file for any requested personality type. Program can write the personality type in the personality-type.txt file:

> type1

Then receiver will automatically set the personality type written in the text file as the request:

```
request = personality_type
```

and send the request to the server:

```
socket.send_string(request)
```

Afterward sending the request, receiver clears the personality-type.txt file and waits for the next personality type written.

## Receive Data

Following is an example on how to receive the response back from the server. Note: must use "recv_string()" to receive string response. Microservice receiver will then write the personality info result in the personality-result.txt file.

```
# Get reply
message = socket.recv_string()


# Write response to a text file
with open('personality-result.txt', 'w') as file:
    file.write(message)
```

## UML Diagram
<img width="713" alt="image" src="https://github.com/kellyayong/Microservice-Info-lookup/assets/73264187/f118e725-a97f-4df7-bf2f-4ab4deef5176">



