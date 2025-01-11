import socket
#client.py 
try:
   client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 
   port = 12345
 
   client.connect(("127.0.0.1",port))

   print("Successfully connected to the server.")
   client.send("Hello, Server!".encode())  
   print("Message received from server: ", client.recv(1024).decode())
  
   client.close();

except Exception as e:
 
   print(f"{e} error occurred.") 
