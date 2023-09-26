import os
import socket
import platform
import subprocess

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('127.0.0.1', 3333)
sock.connect(addr)

def sysinfo():
    info = f"Processor: {platform.processor()}\n"
    info += f"Architecture: {platform.architecture()}\n"
    info += f"Machine: {platform.machine()}\n"
    info += f"Node: {platform.node()}\n"
    info += f"Platform: {platform.platform()}\n"
    info += f"System: {platform.system()}"
    sock.send(info.encode())

def shutdown():
    os.system('shutdown /s')

def restart():
    os.system('shutdown /r')

def service():
    srv = subprocess.run(["sc", "query"], text=True, capture_output=True)
    sock.send(srv.stdout.encode())

while True:
    response = sock.recv(1024).decode()
    print("Received:", response)

    match response:
        case "system":
            sysinfo()
        case "shutdown":
            shutdown()
        case "restart":
            restart()
        case "service":
            service()
        case _:
            code = "404"
            sock.send(code.encode())
