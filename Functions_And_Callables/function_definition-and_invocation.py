import socket

def resolve(host):
    return socket.gethostbyname(host)

print(resolve('www.pluralsight.com'))