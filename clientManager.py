import sessionManager
import socketHandler

client = socketHandler()
session = sessionManager()
clientSocket = client.createConnection("172.17.0.2",3030)
message = recieveDataFromSession(clientSocket)
print(message)