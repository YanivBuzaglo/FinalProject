import socket
target = input("Insert your target IP: ==> ")
while True:
    try:
        sock = socket.socket()
        port = input("Insert port to scan in the target machine: ==> ")
        if "exit" in port:
            break
        else:
            sock.connect((target, int(port)))
            sock.send("What is your banner?\r\n".encode())
            socket.setdefaulttimeout(4)
            rec = sock.recv(1024).decode()
            print(f"[+] The banner of the service --> {rec} and port: {port}")
            sock.close()
    except:
        continue