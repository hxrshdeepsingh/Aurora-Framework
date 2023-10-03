import socket

x = '127.0.0.1'
y = 3333

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((x, y))
sock.listen()
print("[*] Server listening...")

while True:
    conn, addr = sock.accept()
    print("[*] Connected to client: ", addr)
    print("[!] Enter a command or 'exit' to quit.")

    while True:
        try:
            command = input("--> ")
            if command == "exit":
                print("[*] Server is shutting down.")
                conn.close()
                sock.close()
                exit()
            elif not command:
                print("[!] Invalid input!")
            else:
                conn.send(command.encode())
                resp = conn.recv(8192).decode()
                print(resp)

        except Exception:
            conn.close()
            print("[!] Client disconnected", addr)
            print("[*] Waiting for clients...")
            break
