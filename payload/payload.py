import socket
import psutil
import platform

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
a = ('127.0.0.1', 3333)
s.connect(a)

def system_info():
    info = f"Processor: {platform.processor()}\n"
    info += f"Architecture: {platform.architecture()}\n"
    info += f"Machine: {platform.machine()}\n"
    info += f"Node: {platform.node()}\n"
    info += f"Platform: {platform.platform()}\n"
    info += f"System: {platform.system()}"
    s.send(info.encode())

def process_info():
    for process in psutil.process_iter(attrs=['pid', 'name']):
        ID = process.info['pid']
        NM = process.info['name']
        data = f"Process ID: {ID}, Process Name: {NM}"
        s.send(data.encode())
        break

while True:
    r = s.recv(1024).decode()
    print("Received:", r)

    if r == 'system':
        system_info()
    elif r == 'process':
        process_info()
    else:
        y = "404"
        s.send(y.encode())
