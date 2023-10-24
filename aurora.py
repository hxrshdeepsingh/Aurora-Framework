import click
from utils import clear
from module_server import server
from module_builder import builder

#clear screen
clear.screen()

# colors
red = "\033[31m"
gray = "\033[90m"
blue = "\033[34m"
reset = "\033[0m"
green = "\033[32m"

# banner
print(f"{green}================================================{reset}")
print(f"{green}================================================{reset}")
print(f"{green}================================================{reset}")
print(f"{green}============== AURORA FRAMEWORK ===V.1=========={reset}")
print(f"{green}================================================{reset}")
print(f"{green}================================================{reset}")
print(f"{green}================================================{reset}\n")

# choices
print(f"{blue}[1] Start Listener for payload{reset}")
print(f"{blue}[2] Generate Payload for windows{reset}")

@click.command()
@click.option("--choice", prompt="[+] Choose an option (1/2)", help="Choose option 1 or 2", type=int)
def main(choice):
    match choice:

        case 1:
            clear.screen()
            server.main()
            clear.screen()

        case 2:
            clear.screen()
            builder.main()
            clear.screen()

        case _:
            print(f"{red}Invalid choice! Please try again.{reset}")
            main()

if __name__ == "__main__":
    main()