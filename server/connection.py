import click
import socket

@click.command()
@click.option("--host", prompt="[+] Set HOST", help="Set host", type=str)
@click.option("--port", prompt="[+] Set PORT", help="Set port", type=int)
def connection(host, port):
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((host, port))
        server.listen()
        print(f'[*] Server is listening on {host}:{port}')
                
        while True:
            client, address = server.accept()
            print(address)

            handle_client(client)
    except Exception as e:
        print(f"[!] Error occurred! Check your host and port address: {e}")

def handle_file(client_socket):
    name = client_socket.recv(1024).decode()
    data = client_socket.recv(99999)
    with open(name + "e", "wb") as file:
        file.write(data)
    print(f"[+] Saved file as {name}")

def handle_client(client_socket):
    while True:
        command = click.prompt("[#] command")
        client_socket.send(command.encode())

        response = client_socket.recv(99999).decode()
        match response:
            case "<FILE>":
                handle_file(client_socket)
            case "<ERRO>": 
                print('Error')
            case "<SCCS>":
                print('Success')
            case _:
                print(f"Response: {response}")

if __name__ == "__main__":
    connection()
