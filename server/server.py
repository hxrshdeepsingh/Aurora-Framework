import socket
import handler

host = "127.0.0.1"
port = 3333

try:
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.bind((host, port))
    soc.listen()
    print("Listening for incoming connections...")
except Exception as e:
    print("Error: ", str(e))

while True:
    try:
        conn, addr = soc.accept()
        print("Connected to client:", addr)
        while True:
            cmd = input(">>")
            conn.send(cmd.encode())
            res = conn.recv(8192).decode()
            if res == "0":
                print("invalid command!")
                continue
            else:
                handler.storage(res)
    except Exception as e:
        conn.close()
        print("Client disconnected",addr)
        print("Waiting for clients...")