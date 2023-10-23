import os
import click

# absolute path
source_file_path = os.path.abspath("module_builder/source_code.txt")

# colors
red = "\033[31m"
gray = "\033[90m"
blue = "\033[34m"
reset = "\033[0m"
green = "\033[32m"


@click.command()
@click.option("--name", prompt="[+] Set name ", help="set name", type=str)
@click.option("--time", prompt="[+] Set reconnection time", help="set time", type=str)
def main(name, time):

    """
    create a new payload file with the given name and set reconnection time
    """
    payload_name = name + '.py'

    source_file = open(source_file_path, 'r')
    payload_file = open(payload_name, 'w')
    payload_file.write(source_file.read())

    source_file.close()
    payload_file.close()

    with open(payload_name, 'r') as file:
        code = file.read()
        code = code.replace('<TIME>', time)
        file.close()

    with open(payload_name, 'w') as file:
        file.write(code)
        file.close()
    
    print(f"{green}[*] Payload saved as {payload_name}{reset}")
