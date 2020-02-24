import sys
import os
sys.path.insert(0, os.path.split(os.path.split(os.path.abspath(__file__))[0])[0])
from dtplib import Client, Server, client, server
import time

def main():
    serverResult = []
    clientResult = []

    def serverRecv(conn, data, datatype):
        serverResult.append(data)

    def clientRecv(data, datatype):
        clientResult.append(data)

    s = Server(serverRecv, jsonEncode=True)
    s.start()
    print(s.getAddr())
    c = Client(clientRecv, jsonEncode=True)
    c.connect(*s.getAddr())
    c.send("Hello, world!")
    s.send("foo bar")
    time.sleep(0.1)
    c.disconnect()
    s.stop()
    
    assert serverResult == ["Hello, world!"]
    assert clientResult == ["foo bar"]

    serverResult = []
    clientResult = []

    with server(None, None, onRecv=serverRecv, recvDir="serverRecv") as s:
        with client(*s.getAddr(), onRecv=clientRecv, recvDir="clientRecv") as c:
            c.sendFile("files")
            s.sendFile("files/test.txt")
            time.sleep(0.1)
    
    assert serverResult == ["files"]
    assert clientResult == ["test.txt"]

    connect = []
    disconnect = []
    disconnected = []

    def onConnect(conn):
        connect.append(conn)

    def onDisconnect(conn):
        disconnect.append(conn)
    
    def onDisconnected():
        disconnected.append(True)

    s = Server(onConnect=onConnect, onDisconnect=onDisconnect)
    s.start()
    c = Client(onDisconnected=onDisconnected)
    c.connect(*s.getAddr())
    time.sleep(0.1)
    client1 = s.getClients()[0]
    c.disconnect()
    time.sleep(0.1)
    c.connect(*s.getAddr())
    time.sleep(0.1)
    client2 = s.getClients()[0]
    s.stop()
    time.sleep(0.1)

    assert connect == [client1, client2]
    assert disconnect == [client1]
    assert disconnected == [True]

if __name__ == "__main__":
    main()
