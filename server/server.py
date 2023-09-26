import socket

x = '127.0.0.1'
y = 3333

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind((x, y))
soc.listen()
print("[*] Handler listening ...")

while True:
    conn, addr = soc.accept()
    print("[*] Connected to client:", addr)

    while True:
        try:
            cmd = input(">> ")
            if cmd == "":
                print("error")
            else:
                conn.send(cmd.encode())
                res = conn.recv(8192).decode()
                print(res)

        except Exception:
            conn.close()
            print("[!] Client disconnected", addr)
            print("[*] Waiting for clients...")
            break
