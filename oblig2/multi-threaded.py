# multithreaded-webserver.py
from socket import *
import threading
import sys


serverPort = 8000  #postnummer serveren skal bruke
    #oppreter tcp socket
serverSocket = socket(AF_INET, SOCK_STREAM)
#begrenser nettverkgrensen og port 
serverSocket.bind(('', serverPort))
serverSocket.listen(5)  # Tillat opptil 5 ventende forbindelser

print(f"[SERVER] Multithreaded Web Server kjører på port {serverPort}...")

# Funksjon som håndterer hver klient i egen tråd
def handle_client(connectionSocket, addr):
    try:
        print(f"[TRÅD] Behandler klient: {addr}")
        #mottar forespørselen fra klienten
        message = connectionSocket.recv(1024).decode()
        # velger filnavn fra Get forespørselen fra index.html filen som jeg lagde
        filename = message.split()[1]
        f = open(filename[1:], 'r')
        outputdata = f.read()
        f.close()

        #sender Http 200 ok
        header = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
        connectionSocket.send(header.encode())
        connectionSocket.send(outputdata.encode())
        connectionSocket.send("\r\n".encode())

    except IOError:
        # Sender 404 not Found hvis file ikke finnes
        error_msg = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n" \
                    "<html><body><h1>404 Not Found</h1></body></html>"
        connectionSocket.send(error_msg.encode())

    finally:
        connectionSocket.close()
        #lukker tilkoblingen 
        print(f"[TRÅD] Ferdig med klient: {addr}")

while True:
    connectionSocket, addr = serverSocket.accept()
    thread = threading.Thread(target=handle_client, args=(connectionSocket, addr))
    thread.start()

serverSocket.close()
sys.exit()
