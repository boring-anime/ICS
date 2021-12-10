import socket

class socketHandler:
    
    def closeSocketConnection(socketToClose):
        socketToClose.close()

    def createConnection(connectionDetails):
        createdSocket = socket.socket()
        print("created socket")
        createdSocket.connect(connectionDetails)
        return createdSocket
