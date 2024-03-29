# Data Transfer Protocol Library

dtplib is a cross platform networking library written in Python.

Source: [https://github.com/WKHAllen/dtplib](https://github.com/WKHAllen/dtplib)

**NOTE:** This project has been archived. Its successor is [dtppy](https://github.com/WKHAllen/dtppy).

## Dependencies

- [compressdir](https://github.com/WKHAllen/compressdir)
- [cryptography](https://github.com/pyca/cryptography)
- [rsa](https://github.com/sybrenstuvel/python-rsa/)

## Installation

```console
$ pip install dtplib
```

## Server

### Creating a server

```py
s = Server(onRecv=None, onConnect=None, onDisconnect=None, blocking=False, eventBlocking=False, recvDir=None, daemon=True, jsonEncode=False, ignoreErrors=False)
```

Create a server object.

`onRecv` is a function that will be called when a packet is received. It takes the following parameters: client socket, data, datatype (0: object, 1: file).
`onConnect` is a function that will be called when a client connects. It takes the following parameters: client socket.
`onDisconnect` is a function that will be called when a client disconnects. It takes the following parameters: client socket.
If `blocking` is True, the start method will block until stopping.
If `eventBlocking` is True, `onRecv`, `onConnect`, and `onDisconnect` will block when called.
`recvDir` is the directory in which files will be put in when received.
If `daemon` is True, all threads spawned will be daemon threads.
If `jsonEncode` is True, packets will be encoded using json instad of pickle.
If `ignoreErrors` is True, all errors will be ignored.

### Starting the server

```py
s.start(host=None, port=None)
```

Start the server. If `host` is not specified, it will default to `socket.gethostname()`. If `port` is not specified, it will default to `0`, which represents an arbitrary unused port.

### Stopping the server

```py
s.stop()
```

Stop the server.

### Check if the server is serving

```py
s.serving()
```

### Get the server's address

```py
s.getAddr()
```

### Get a client's address

```py
s.getClientAddr(conn)
```

Get a client's address, providing the client socket object.

### Get a list of a server's clients

```py
s.getClients()
```

### Remove a client

```py
s.removeClient(conn)
```

Disconnect a client from the server, providing the client socket object.

### Send data to a client

```py
s.send(data, conn=None)
```

Send data to a client. `conn` is the client socket object to send the data to. If `conn` is None, data is sent to all clients.

### Send a file or directory to a client

```py
s.sendFile(path, conn=None)
```

Send a file or directory to a client. `path` is the path to the file or directory. `conn` is the client socket object to send the file or directory to. If `conn` is None, the file or directory is sent to all clients.

## Server alternative

The dtplib server object can be used in a with statement.

```py
with server(host, port, *args, **kwargs) as s:
    pass
```

`host` is the server IP address. `port` is the port number. `args` and `kwargs` will be passed to the Server class constructor.

## Client

### Creating a client

```py
c = Client(onRecv=None, onDisconnected=None, blocking=False, eventBlocking=False, recvDir=None, daemon=True, jsonEncode=False)
```

Create a client object.

`onRecv` is a function that will be called when a packet is received. It takes the following parameters: data, datatype (0: object, 1: file).
`onDisconnected` is a function that will be called when the server disconnects suddenly. It takes no parameters.
If `blocking` is True, the connect method will block until disconnecting.
If `eventBlocking` is True, `onRecv` and `onDisconnected` will block when called.
`recvDir` is the directory in which files will be put in when received.
If `daemon` is True, all threads spawned will be daemon threads.
If `jsonEncode` is True, packets will be encoded using json instad of pickle.

### Connecting to a server

```py
c.connect(host, port)
```

### Disconnecting from the server

```py
c.disconnect()
```

### Check if connected to a server

```py
c.connected()
```

### Get the client's address

```py
c.getAddr()
```

### Get the remote server's address

```py
c.getServerAddr()
```

### Send data to the server

```py
c.send(data)
```

Send data to the server, providing the data to be sent.

### Send a file or directory to the server

```py
c.sendFile(path)
```

Send a file or directory to the server, providing the path to the file or directory to be sent.

## Client alternative

The dtplib client object can be used in a with statement.

```py
with client(host, port, *args, **kwargs) as c:
    pass
```

`host` is the server IP address. `port` is the port number. `args` and `kwargs` will be passed to the Client class constructor.
