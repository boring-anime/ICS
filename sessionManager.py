import socket

class sessionManager:

    def sendDataToSession(sessionSocket,data):
        sessionSocket.send(bytes(str(data),'utf-8'))

    def recieveDataFromSession(sessionSocket):
        data = sessionSocket.recv(1024).decode()
        return data
