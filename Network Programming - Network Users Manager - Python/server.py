import sqlite3
import socket
import os

File = 'DataBase.db'
if not os.path.exists(File):
    connection = sqlite3.connect(File) 
    connection.execute('''CREATE TABLE users(userID INTEGER PRIMARY KEY, username TEXT NOT NULL, password TEXT NOT NULL, firstName TEXT NOT NULL, lastName TEXT NOT NULL, status BOOLEAN NOT NULL);''')
    connection.execute('''CREATE TABLE IPs_blacklist(IP_address TEXT PRIMARY KEY);''')
    connection.execute('''CREATE TABLE Files(userID INTEGER,fileName TEXT NOT NULL,PRIMARY KEY (userID, fileName),FOREIGN KEY (userID) REFERENCES users(userID) ON DELETE CASCADE ON UPDATE CASCADE);''')

    connection.execute("INSERT INTO users VALUES (12027708,'Aws','AWSNASSAR1','AWS','NASSAR',0)")
    
    connection.execute("INSERT INTO IPs_blacklist VALUES ('127.0.0.2')")
    connection.execute("INSERT INTO IPs_blacklist VALUES ('127.0.0.3')")
    connection.execute("INSERT INTO IPs_blacklist VALUES ('127.0.0.4')")
    
    connection.execute("INSERT INTO Files VALUES (12027708,'aws.jpg')")
    connection.execute("INSERT INTO Files VALUES (12027708,'key.txt')")
    
    connection.commit()
    connection.close()
    
connection = sqlite3.connect(File)
cursor = connection.cursor()
def adduser():
    userID = input("enter user ID: ")
    username = input("enter username: ")
    password = input("enter password: ")
    firstName = input("enter firstName: ")
    lastName = input("enter lastName: ")
    try:
        cursor.execute("""insert into users (userID, username, password, firstName, lastName , status) values (?,?,?,?,?,?)""",(userID,username,password,firstName,lastName,False))
        #print("the user " + username  + " added successfully")
        connection.commit()
        print(f"user: {username} added successfully")
    except sqlite3.IntegrityError as e:
        print("you entered an existing user(an existing userID)! ,please re-enter a non existing one.")

def removeUser():
    userID = input("enter user ID to be removed: ")
    cursor.execute("""select * from users where userID = ?""" , (userID,))
    find = cursor.fetchone()
    if find != None:
        cursor.execute(""" delete from users where userID = ?""" , (userID,))
        connection.commit()
        print(f"user has ID:{userID} removed successfully ")
    elif find == None:
        print("you'r triying to remove a non existing user(a non existing userID)! ,please re-enter an existing one.")

def updateUser():
    userID = input("enter user ID to be updated: ")
    username = input("enter username: ")
    password = input("enter password: ")
    firstName = input("enter firstName: ")
    lastName = input("enter lastName: ")
    status = input("enter status: ")
    cursor.execute("""select * from users where userID = ?""" , (userID,))
    find = cursor.fetchone()
    if find != None:
        cursor.execute("""update users set username = ?,password = ?,firstName = ?,lastName = ?,status = ? where userID = ?""" , (username,password,firstName,lastName,status,userID))
        connection.commit()
        print("updated successfully")
    elif find == None:
        print("you'r triying to update a non existing user(a non existing userID)! ,please re-enter an existing one.")

def listUsers():
    cursor.execute("""select * from users""")
    rf = cursor.fetchone()
    if  rf == None:
        print("There are no users to be printed")
    else:
        cursor.execute("""select * from users""")
        rs = cursor.fetchall()
        for i in rs:
            print(i)

def blockUser():
    username = input("enter username to be blocked: ")
    cursor.execute(""" select * from users where username = ?""" , (username,))
    find = cursor.fetchone()
    if find != None:
        cursor.execute("""update users set status = True where username = ?""",(username,))
        connection.commit()
        print(f"The user: {username} blocked successfully")
    elif find == None:
        print("the entered username does not exists")

def unblockUser():
    username = input("enter username to be unblocked: ")
    cursor.execute(""" select * from users where username = ?""" , (username,))
    find = cursor.fetchone()
    if find != None:
        cursor.execute("""update users set status = False where username = ?""",(username,))
        connection.commit()
        print(f"The user: {username} unblocked successfully")
    elif find == None:
        print("the entered username does not exists")

def blockIPddress():
    IPaddress = input("enter IPaddress to be blocked: ")
    try:
        cursor.execute("""insert into IPs_blacklist (IP_address) values (?) """ , (IPaddress,))
        connection.commit()
        print(f"This IP: {IPaddress} blocked successfully")
    except sqlite3.IntegrityError as e:
        print("you entered an existing IPaddress! ,please re-enter a non existing one.")

def unblockIPaddress():
    IPaddress = input("enter IPaddress to be unblocked: ")
    cursor.execute("""select * from IPs_blacklist where IP_address = ?""" , (IPaddress,))
    find = cursor.fetchone()
    if find != None:
        cursor.execute("""delete from IPs_blacklist where IP_address = ?""" , (IPaddress,))
        connection.commit()
        print(f"This IP: {IPaddress} unblocked successfully")
    elif find == None:
        print("you'r triying to remove a non existing IPaddress! ,please re-enter an existing one.")

def printBlackList():
    cursor.execute("""select * from IPs_blacklist""")
    rf = cursor.fetchone()
    if rf == None:
        print("There are no IPs to be printed")
    else:
        cursor.execute("""select * from IPs_blacklist""")
        rs = cursor.fetchall()
        for i in rs:
            print(i)

def serverAdministratortasks():
    while True:
        print("_________________________")
        print("1.Add user")
        print("2.Remove user")
        print("3.Update user")
        print("4.List  users")
        print("5.Block user")
        print("6.unblock user")
        print("7.Block IP address")
        print("8.unblock IP address")
        print("9.IPs_blacklist")
        print("10.Exit")
        print("----")
        x = input("-> ")
        if x == "1":
            adduser()
        elif x == "2":
            removeUser()
        elif x == "3":
            updateUser()
        elif x == "4":
            listUsers()
        elif x == "5":
            blockUser()
        elif x == "6":
            unblockUser()
        elif x == "7":
            blockIPddress()
        elif x == "8":
            unblockIPaddress()
        elif x == "9":
            printBlackList()
        elif x == "10":
            break
        
# -------------------------------------------------
       
def dealingwithclients():
    SERVER_HOST = "127.0.0.1"
    SERVER_PORT = 5001
    BUFFER_SIZE = 4096

    s = socket.socket()
    s.bind((SERVER_HOST, SERVER_PORT))
    s.listen(1)
    print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

    client_socket, address = s.accept() 
    userName = client_socket.recv(BUFFER_SIZE).decode()
    IPAddress = address[0]
    
    print(f"[*]Client user-name: {userName},\n[*]Client IP address: {IPAddress}")
    cursor = connection.execute("SELECT username FROM users WHERE username = ?", (userName,))
    rs = cursor.fetchone()
    #edit
    if rs == None:
        print ("This user name does not belong to the database") 
        client_socket.send("0".encode())
        client_socket.close()
        return
        
    cursor1 = connection.execute("SELECT status FROM users WHERE username = ?", (userName,))
    if cursor1.fetchone()[0] == 1: 
        client_socket.send("1".encode())
        print ("This user name has been blocked")
        client_socket.close()
        return
        
    cursor2 = connection.execute("SELECT IP_address FROM IPs_blacklist WHERE IP_address = ?", (IPAddress,))
    if cursor2.fetchone() != None:
        client_socket.send("2".encode())
        print ("This IP address has been blocked")
        client_socket.close()
        return
            
    client_socket.send("Success in login you can upload or download your files".encode())
    option = ""
    while option != "3":
        client_socket.send("\n\n---------------------------\n\nEnter the number of the option:\n1.download a file.\n2.Upload a file.\n3.Exit".encode())
        option = client_socket.recv(BUFFER_SIZE).decode()
        
        print("The Client select option number: ", option)
 
        #option num: 1
        
        if option == "1":
            cursor3 = connection.execute("SELECT userID FROM users WHERE username = ?", (userName,))
            ID = cursor3.fetchone()[0]
            cursor4 = connection.execute("SELECT fileName FROM Files WHERE userID = ?", (ID,))
            rs = cursor4.fetchall()
            if len(rs) == 0:
                client_socket.send("0".encode())

            else:
                FNames=""
                j = 1
                for row in rs:
                    FNames += str(j)+". " + row[0] + "\n"
                    j = j+1
                client_socket.send(FNames.encode())
                path = client_socket.recv(BUFFER_SIZE).decode()
                print(f"the file selected: {path}")
                if not os.path.exists(path):
                    print("File does not Exists") 
                    client_socket.send("0".encode())
                else:
                    client_socket.send("1".encode())
                    client_socket.send(path.encode())
                    FileSize = os.path.getsize(path)
                    client_socket.send(str(FileSize).encode())
                   
                    with open(path, "rb") as f:
                        bytes_read = f.read(FileSize) 
                        client_socket.sendall(bytes_read)
                    print("Sending done")
                    
        #option num: 2
        
        elif option == "2": 
            path = client_socket.recv(BUFFER_SIZE).decode()
            if path == "0":
                print("wrong file name")
            else:
                print(path)

                FileSize = int(client_socket.recv(BUFFER_SIZE).decode())
                print(FileSize)
                path = "1"+path
                with open(path, "wb") as f:
                    bytes_read = client_socket.recv(FileSize)
                    f.write(bytes_read)
                print("Reciving done")            
                cursor7 = connection.execute("SELECT userID FROM users WHERE username = ?", (userName,))
                ID = cursor7.fetchone()[0]
                connection.execute("INSERT INTO Files VALUES (?, ?)", (ID, path))
                print("[*]Updating table done")
                print("--------\n[*]All data in Files table:")
                cursor = connection.execute("SELECT * FROM Files ")
                for row in cursor:
                    print(row)
                connection.commit() 
            
        #option num: 3
        
        elif option == "3":
            OS = "End of " + userName + " connection "
            print(f"\n{OS}\n")
            client_socket.send("end of Connection".encode())
            client_socket.close()
            break


while True:
    print("*******MainMenu******") 
    print("*************************")      
    print("choose an option:-")
    print("1.Server Administrator tasks")
    print("2.dealing with clients")
    print("3.Exit")
    print("----")
    x = input("-> ")
    if x == "1":
        serverAdministratortasks()
    elif x == "2":
        dealingwithclients()
    elif x == "3":
        OS = "Salamat"
        print(f"********\n\n{OS}\n\n********")
        break