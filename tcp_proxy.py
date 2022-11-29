import sys
import socket
import threading

def server_loop(local_host,local_port,remote_host,remote_port,recieve_first):
    
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    try:
        server.bind((local_host,local_port))
    except:
        print("[+] Failed to listen to the port and host %s:%d"%(local_host,local_port))
        print("Check for other Listening sockets")
        sys.exit(0)

    print("[+]Listening on the host and port %s:%d"%(local_host,local_port))

    server.listen(5)

    while True:
        client_socket, addr = server.accept()

        print("==> Recieved incoming connection from %s:%d"%(addr[0],addr[1]))

        proxy_thread
