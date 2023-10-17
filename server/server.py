import dependencies

dependencies.install()

def check_conditions():
    if dependencies:
        import connection
        print(f"{dependencies.green}[*] Enter IP and PORT number to start listener... (ctrl+c to abort){dependencies.reset}")
        connection.connection()
    else:
        print(f"{dependencies.red}[!] Unknown error occured{dependencies.reset}")

check_conditions()