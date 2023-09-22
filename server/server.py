import socket
import handler

def main():
    x = str(input("[*] Listener IP   :   "))
    y = int(input("[*] Listener PORT :   "))

    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.bind((x, y))
    soc.listen()
    print(handler.GREEN + "[*] Handler listening ..." + handler.RESET)

    while True:
        conn, addr = soc.accept()
        print(handler.GREEN + "[*] Connected to client:", addr + handler.RESET)

        while True:
            try:
                cmd = input(">> ")
                conn.send(cmd.encode())
                res = conn.recv(8192).decode()
                print(res)

            except Exception:
                conn.close()
                print(handler.RED + "[!] Client disconnected {addr}" + handler.RESET)
                print(handler.GREEN + "[*] Waiting for clients..." + handler.RESET)
                break

if __name__ == "__main__":
    main()
