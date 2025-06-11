# This program is a basic server that runs using sockets.

# First of all, we need to import our modules.
# We'll use the built-in 'socket' module, which is suitable for creating servers and clients.
import socket

# The socket module allows you to create servers and clients that communicate using TCP or UDP.

# Now we're going to create the main server socket using socket functions.
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.socket() creates a new socket object.
# AF_INET sets the address family to IPv4.
# SOCK_STREAM specifies that we are using TCP (a connection-based protocol).

# Now we have to bind our server to a host and port.
# Here, we use "localhost" as the default host.
server_socket.bind(("localhost", 8080))
# The bind() function assigns an IP address and port to the server.
# "localhost" refers to the local machine, and 8080 is the chosen port number.

# The server now starts listening for incoming client connections.
server_socket.listen(1)
# listen(1) tells the operating system to allow 1 connection to wait in the queue.

# Now we wait for a client to connect.
print("Server is waiting for a connection...")
client_socket, client_address = server_socket.accept()
print(f"Server connected to {client_address}")
# The accept() function blocks execution and waits for a client to connect.
# Once a connection is made, it returns:
# - client_socket: a new socket object used for communication with the client.
# - client_address: a tuple containing the client's IP and port.

# Communication begins: the server receives data from the client.
data = client_socket.recv(1024).decode()
print(f"Received from client: {data}")
# recv(1024) reads up to 1024 bytes of data from the client.
# decode() converts the received bytes into a string.

# Now the server sends a response to the client.
response = "Hello, Client!"
client_socket.send(response.encode())
# encode() converts the string into bytes before sending.
# send() transmits the encoded data to the client.

# After the exchange, we close the connections.
client_socket.close()
server_socket.close()
