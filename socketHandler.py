import socket

class socketHandler:
    
    def closeSocketConnection(self,socketToClose):
        socketToClose.close()

    def createConnection(self,connectionDetails):
        createdSocket = socket.socket()
        print("created socket")
        createdSocket.connect((connectionDetails))
        return createdSocket