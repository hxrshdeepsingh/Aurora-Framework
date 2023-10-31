import click
from module_server import server
from module_builder import builder

# colors
red = "\033[31m"
gray = "\033[90m"
blue = "\033[34m"
reset = "\033[0m"
green = "\033[32m"

# banner
def print_banner():
    print(f"{green}================================================{reset}")
    print(f"{green}============== AURORA FRAMEWORK ===V.1=========={reset}")
    print(f"{green}================================================{reset}\n")

def print_menu():
    print(f"{blue}[1] Start Listener for payload{reset}")
    print(f"{blue}[2] Generate Payload for windows{reset}")
    print(f"{blue}[3] Exit{reset}")

@click.command()
def main():
    while True:
        click.clear()
        print_banner()
        print_menu()

        choice = click.prompt("[+] Choose an option (1/3)", type=int)

        match choice:
            case 1:
                click.clear()
                server.main()
                click.clear()
            case 2:
                click.clear()
                builder.main()
                click.clear()
            case 3:
                click.clear()
                break
                
            case _:
                print(f"{red}Invalid choice! try again.{reset}")

if __name__ == "__main__":
    main()