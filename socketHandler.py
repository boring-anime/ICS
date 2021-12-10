import socket

class socketHandler:
    
    def closeSocketConnection(self,socketToClose):
        socketToClose.close()

    def createConnection(self,connectionHost,connectionPort):
        createdSocket = socket.socket()
        createdSocket.connect((connectionHost,connectionPort))
        return createdSocket
