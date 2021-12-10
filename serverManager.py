import socket
import sessionManager
import socketHandler

class server:

    session = sessionManager()
    sock = socketHandler()
    def __init__(self, port=3030, hostname="localhost", maxAllowedConn=3):
        self.port = port
        self.hostname = hostname
        self.maxAllowedConn = maxAllowedConn

    def initializeServer(self):
        serverSocket = socket.socket()
        serverSocket.bind ((self.hostname,self.port))
        serverSocket.listen(self.maxAllowedConn)
        return serverSocket

    def stopServer(self,serverSocket):
        serverSocket.shutdown(0)

srvr = server()
s = srvr.initializeServer()
# def startListeningOnServer(serverSocket):
print("waiting for connection")

clientSocket, clientAddr = serverSocket.accept()
srvr.session.sendDataToSession(clientSocket,"hello")
srvr.sock.closeSocketConnection(clientSocket)





