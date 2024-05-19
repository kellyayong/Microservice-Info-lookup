# Microservice Personality Info Lookup

CS361 Sprint 2 - Personality Info Lookup Microservice uses ZeroMQ for the communication pipe. Microserive will receive personality type as a string, looks up the corresponding personality info in a csv file, and sends the info as a string back to the main program.

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

Once connection is established, example program can set the personality type searching for more info on as the request and send the request to the server:

```
# Set the personality type requesting for info as the request
request = 'type1'

# Send request and wait for response
print(f"Searching for personality {request} ...")
socket.send_string(request)
```

## Receive Data

Use the followng example codes to receive the response back from the microservice server. Example program can then write the personality info result in the CLI, the personality-result.txt file, or show in an alert pop up box.
> [!Note]
> Must use "recv_string()" to receive string response.

Get response with:
```
# Get response from microservice server
message = socket.recv_string()
```
### Print response in CLI
```
print(f"Your Personality type is: {request}\n [ {message} ]")
```

###  Write response in a text file
```
with open('personality-result.txt', 'w') as file:
    file.write(message)
```
### Display info as pop up message box

Install PyMsgBox by typing in the terminal:
```
>>> pip install PyMsgBox
```
Then in example program:
```
import pymsgbox
pymsgbox.alert(message, request, button='OK')
```


## UML Diagram
<img width="799" alt="image" src="https://github.com/kellyayong/Microservice-Info-lookup/assets/73264187/4b0d7ab9-0100-4e2c-9035-4564a35c52d8">

