import socket

sock = socket.socket()
sock.connect(("127.0.0.1", 10001))
sock.sendall("ping".encode("utf8"))
sock.close()

# Или
# sock = socket.create_connection(("127.0.0.1", 10001))
# sock.sendall("ping".encode("utf8"))
# sock.close()
