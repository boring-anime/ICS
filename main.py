import serverManager
import dbHandler
import sessionManager
import socketHandler
import cache_manager
import request
import json

def main():
    srvr = serverManager.server(3030)
    s = srvr.initializeServer()
    # def startListeningOnServer(serverSocket):
    print("waiting for connection")

    

    clientSocket, clientAddr = s.accept()
    
    request_block =  srvr.session.recieveDataFromSession(clientSocket)

    request_block = json.loads(request_block)
    print(request_block)

    request_data = request.request(request_block["type"], request_block["key"], request_block["value"] )
    
    cacheManager = cache_manager.Cache_manager(request_data)
    Value = cacheManager.request_to_cache()


    srvr.session.sendDataToSession(clientSocket, Value)
    srvr.sock.closeSocketConnection(clientSocket)
    srvr.stopServer
  
if __name__=="__main__":
    main()
