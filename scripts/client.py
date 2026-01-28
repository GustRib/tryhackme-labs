import socket
import time

HOST = "10.64.165.202"
PORT = 5901

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(10)
s.connect((HOST, PORT))

banner = s.recv(1024)
version = banner.split(b"\n")[0] + b"\n"
s.sendall(version)

time.sleep(2)

try:
    data = s.recv(4096)
    if data:
        print(data.decode(errors="ignore"))
except:
    pass

while True:
    msg = input(">> ")
    s.sendall(msg.encode() + b"\n")
    try:
        resp = s.recv(4096)
        print(resp.decode(errors="ignore"))
    except:
        break

s.close()
