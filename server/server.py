import socket
import handler

try:
    host = input("host :")
    port = int(input("port :"))
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.bind((host, port))
    soc.listen()
    print(handler.GREEN,"Listening...",handler.RESET)
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
        print(handler.RED,"Client disconnected",addr,handler.RESET)
        print("Waiting for clients...")