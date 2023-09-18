import socket
import handler

try:
    host = input("host :")
    port = input("port :")
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