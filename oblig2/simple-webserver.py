# simple-webserver.py
from socket import * #tcp server
import sys

serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 8000

serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print(f"Server is ready on port {serverPort}...")

while True:
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:], 'r')  # f.eks. /index.html → index.html
        outputdata = f.read()
        f.close()

        #sender HTTP 200 ok
        header = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
        connectionSocket.send(header.encode())
        connectionSocket.send(outputdata.encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()

    except IOError:
        # Send HTTP 404 Not Found
        error_msg = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n" \
                    "<html><body><h1>404 Not Found</h1></body></html>"
        connectionSocket.send(error_msg.encode())
        connectionSocket.close()
        serverSocket.close()
        sys.exit()
