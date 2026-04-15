# Penjelasan Socket Programming: TCP & UDP

## TCP Server & Client

### 1. TCPServer.py - Server dengan TCP

```python
from socket import *

serverName = '127.0.0.1'
serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)  # TCP socket
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The Server is ready too receive")

while True:
    connctionSocket, addr = serverSocket.accept()
    sentence = connctionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connctionSocket.send(capitalizedSentence.encode())
    connctionSocket.close()
```

#### Penjelasan Kode:

| Baris Kode | Fungsi |
|------------|--------|
| `socket(AF_INET, SOCK_STREAM)` | Membuat TCP socket. `AF_INET` = IPv4, `SOCK_STREAM` = TCP |
| `bind(('', serverPort))` | Mengikat socket ke port 12000 di semua interface |
| `listen(1)` | Server siap menerima koneksi (max 1 koneksi dalam antrian) |
| `accept()` | **Blocking call** - menunggu sampai ada client yang terkoneksi |
| `recv(1024)` | Menerima data maksimal 1024 bytes dari client |
| `upper()` | Mengubah kalimat menjadi huruf kapital |
| `send()` | Mengirim data kembali ke client |
| `close()` | Menutup koneksi dengan client (bukan server socket) |

### 2. TCPClient.py - Client dengan TCP

```python
from socket import *

serverName = '127.0.0.1'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)  # TCP socket
clientSocket.connect((serverName, serverPort))

sentence = input("Input lowercase sentence: ")
clientSocket.send(sentence.encode()) 
modifiedSentence = clientSocket.recv(1024)
print("From Server: ", modifiedSentence.decode())

clientSocket.close()
```

#### Penjelasan Kode:

| Baris Kode | Fungsi |
|------------|--------|
| `socket(AF_INET, SOCK_STREAM)` | Membuat TCP socket |
| `connect((serverName, serverPort))` | **3-way handshake** dengan server untuk establish koneksi |
| `encode()` | Mengubah string ke bytes (format untuk dikirim) |
| `send()` | Mengirim data melalui koneksi yang sudah terbentuk |
| `recv(1024)` | Menerima response dari server |
| `decode()` | Mengubah bytes kembali ke string |
| `close()` | Menutup koneksi dengan server |

## UDP Server & Client

### 3. UDPServer.py - Server dengan UDP

```python
from socket import *

serverName = '127.0.0.1'
serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)  # UDP socket
serverSocket.bind(('', serverPort))
print("The server is ready to receive")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
```

#### Penjelasan Kode:

| Baris Kode | Fungsi |
|------------|--------|
| `socket(AF_INET, SOCK_DGRAM)` | Membuat UDP socket. `SOCK_DGRAM` = UDP |
| `bind(('', serverPort))` | Mengikat socket ke port 12000 |
| **TIDAK ADA `listen()` & `accept()`** | UDP connectionless, tidak perlu |
| `recvfrom(2048)` | Menerima data (max 2048 bytes) **DAN alamat pengirim** |
| `sendto(data, address)` | Mengirim data ke alamat client yang spesifik |

### 4. UDPClient.py - Client dengan UDP

```python
from socket import *

serverName = '127.0.0.1'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)  # UDP socket
message = input("Input lowercase sentence: ")

clientSocket.sendto(message.encode(), (serverName,serverPort))
modifiedMessage, serverAdd = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())

clientSocket.close()
```

#### Penjelasan Kode:

| Baris Kode | Fungsi |
|------------|--------|
| `socket(AF_INET, SOCK_DGRAM)` | Membuat UDP socket |
| **TIDAK ADA `connect()`** | Langsung kirim tanpa handshake |
| `sendto(data, (ip, port))` | Mengirim datagram ke server |
| `recvfrom(2048)` | Menerima response dan alamat server |