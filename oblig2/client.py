import socket   #tcp
import argparse 

def main():
    #her blir det satt opp kommando argumenter 
    parser = argparse.ArgumentParser(description='Simple HTTP Client')
    parser.add_argument('-i', '--ip', type=str, required=True, help='Server IP')
    parser.add_argument('-p', '--port', type=int, required=True, help='Port number')
    parser.add_argument('-f', '--file', type=str, required=True, help='Filename to request')
    args = parser.parse_args()

    #oppretter en TCP klientsocket 
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # kobler til serveren 
        client_socket.connect((args.ip, args.port))
        #http forespørsel
        request = f"GET /{args.file} HTTP/1.1\r\nHost: {args.ip}\r\n\r\n"
        # sender forespørsel til serveren
        client_socket.send(request.encode())

        #motar respons fra serven 
        response = b""
        while True:
            data = client_socket.recv(1024)
            if not data:
                break  #stoopper hvis det ikke kommer mer data
            response += data

        #printer ut svarene 
        print("Received from server:\n")
        print(response.decode())

    except Exception as e:
        print("Error:", e) #hvsi det skjer fiel

    finally:
        client_socket.close() #stopper forbindelen til serven 


if __name__ == "__main__":
    main()
