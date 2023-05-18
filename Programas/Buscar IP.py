import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print()
print("El nombre de tu ordenador es->> " + hostname)
print()
print("Tu dirección IP es->> " + ip)
print()
