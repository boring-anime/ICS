import socket

class socketHandler:
    
    def closeSocketConnection(socketToClose):
        socketToClose.close()

    def createConnection(connectionHost,connectionPort):
        createdSocket = socket.socket()
        createdSocket.connect((connectionHost,connectionPort))
        return createdSocket