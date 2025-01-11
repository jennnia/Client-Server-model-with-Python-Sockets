import socket 
#server.py 
try:

   server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   print("Socket successfully created.")
   
   server.bind(("localhost", 12345))
   print("Server binded to local host on port 12345.")

   server.listen(1)
   print("Server is listening.")   
   while True:
    
      client,address = server.accept()
      print(f"Got connection from:{address}.")
      client.send("Thank you for connecting.".encode())

      print("Received message: ",client.recv(1024).decode())
      
      client.close()
      break
except Exception as e:
  
    print(f"{e} error occurred.")
