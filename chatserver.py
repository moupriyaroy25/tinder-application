from socket import AF_INET,socket,SOCK_STREAM
from threading import Thread

client={}
addresses={}

HOST=''
PORT=123456
BUFSIZ=1024
ADDR=(HOST,PORT)

server=socket(AF_INET,SOCK_STREAM)
server.bind(ADDR)

def accept_incoming_connections():
    while True:
        client,ip_address=server.accept()
        print("%s is connected"%ip_address)
        client.send('thank for connecting')
        addresses[client]=ip_address
        Thread(target=handle_client,args=(client,)).start()

def handle_client(client):
    name=client.recv(BUFSIZ).decode("utf8")
    welcome='welcome%s!if you want to exit the chat please kindly type{quit}'%name
    client.send(bytes(welcome,"utf8"))
    msg="%s has joined the chat"%name
    broadcast(bytes(msg,"utf8"))
    client[client]=name
    while True:
        msg=client.recv(BUFSIZ)
        if msg!=bytes("{quit}","utf8"):
            broadcast(msg,name+":")
        else:
            client.send(bytes("{quit}","utf8"))
            client.close()
            del client[client]
            broadcast(bytes("%s has left the chat"% name,"utf8"))
            break
def broadcast(msg,prefix=""):
    for sock in client:
        sock.send(bytes(prefix,"utf8")+ msg)

        server.listen(5)
        print("waiting for connection...")
        ACCEPT_THREAD=Thread(target=accept_incoming_connections)
        ACCEPT_THREAD.start()
        ACCEPT_THREAD.join()
        server.close()