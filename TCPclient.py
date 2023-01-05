import socket

def mainRun():
  host = "127.0.0.1"
  port = 5000
  s = socket.socket()
  s.connect((host,port))
  data = input("Input :")

  while data!="q":
    s.send(data.encode("utf-8"))
    data = s.recv(1024).decode("utf-8")
    print("Data from Server :"+data)
    data = input("Inprt :")
  s.close()

mainRun()
