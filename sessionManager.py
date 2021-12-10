import socket

class sessionManager:

    def sendDataToSession(self,sessionSocket,data):
        sessionSocket.send(bytes(str(data),'utf-8'))

    def recieveDataFromSession(self,sessionSocket):
        data = sessionSocket.recv(1024).decode()
        return data
