from socket import *

serverName = '127.0.0.1'
serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The Server is ready too receive")

while True:
    connctionSocket, addr = serverSocket.accept()
    sentence = connctionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connctionSocket.send(capitalizedSentence.encode())
    connctionSocket.close()