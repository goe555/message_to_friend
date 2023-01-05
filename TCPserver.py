import socket

def mainRun():
  host = "127.0.0.1"
  port = 5000
  s = socket.socket()
  s.bind((host,port))
  s.listen(1)
  print("Waiting connection from Client: ")
  client,addr = s.accept()
  print("Connect from :"+str(addr))

  while True:
    data = client.recv(1024).decode("utf-8")
    if not data :
      break
    print("Massage from client :"+data)
    data = str(data.upper())
    client.send(data.encode("utf-8"))
  client.close()

mainRun()
