import sessionManager
import socketHandler
import request
import json

client = socketHandler.socketHandler()
session = sessionManager.sessionManager()
clientSocket = client.createConnection(("127.0.0.1",3030))


def create_request():

    request_structure =  '{ "type":"", "key":"", "value":""}'
    request_block = json.loads(request_structure)

# the result is a Python dictionary:
    request_block["type"] = input("Enter reuest type: ") 
    request_block["key"] = input("Enter Key: ")
    request_block["value"] = None
    if request_block["type"]  == "PUT":
        request_block["value"]  = input("Enter value: ")
    return json.dumps(request_block)


request_to_server = create_request()

session.sendDataToSession(clientSocket, request_to_server)
message = session.recieveDataFromSession(clientSocket)
print(message)