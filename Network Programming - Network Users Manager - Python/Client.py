import socket
import os

BUFFER_SIZE = 4096 # send 4096 bytes each time step
# the ip address or hostname of the server, the receiver
host = "127.0.0.1"
# the port, let's use 5001
port = 5001
# the name of file we want to send, make sure it exists
# get the file size
# create the client socket
s = socket.socket()
userName = input("Enter you user Name: ")
print(f"[+] Connecting to {host}:{port}")
s.connect((host, port))
print("[+] Connected.")

# send the filename and filesize
s.send(f"{userName}".encode())

message = s.recv(BUFFER_SIZE).decode()
if message == "0":
    print ("This user name does not belong to the database")
    s.close()
    
elif message == "1":
    print ("This user name has been blocked")
    s.close()
    
elif message == "2":
    print ("This IP address has been blocked")
    s.close()
    

else:
    print(message)
    choice = ""
    while choice != "3":    
        option = s.recv(BUFFER_SIZE).decode()
        print(option)
        choice = input("->")
        if choice != "1" and choice != "2" and choice != "3":
            print("invalid option number")
        s.send(choice.encode())
    
        #option num: 1
    
        if choice == "1":
            recive = s.recv(BUFFER_SIZE).decode()
            if recive == "0":
                print("you have no files uploaded before")
                break
            print(recive)
            choice2 = input("Enter your File name: ")
            s.send(choice2.encode())
            exist = s.recv(BUFFER_SIZE).decode()
            if exist == "0":
                print("File does not exist")
            else:
                path = s.recv(BUFFER_SIZE).decode()
                FileSize = int(s.recv(BUFFER_SIZE).decode())
                path = "1"+path
                with open(path, "wb") as f:
                    bytes_read = s.recv(FileSize)
                    f.write(bytes_read)
                print("Reciving done")
    
        #option num: 2    
    
        elif choice == "2":  
            path = input("Enter your File name: ")
            if not os.path.exists(path):
                print("File does not Exists")
                s.send("0".encode())
                
            else:
                s.send(path.encode())
                FileSize = os.path.getsize(path)
                s.send(str(FileSize).encode())
                with open(path, "rb") as f:
                    bytes_read = f.read(FileSize)
                    s.sendall(bytes_read)
                print("Sending done")
            
            #option num: 3    
    
        elif choice == "3":
            Why = s.recv(BUFFER_SIZE).decode()
            print(f"********\n\n{Why}\n\n********")
            s.close()
    


