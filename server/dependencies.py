import subprocess

green = "\033[32m"
red = "\033[31m"
gray = "\033[90m"
reset = "\033[0m"

def install():
    required_dependencies = ['socket', 'click']
    for dependency in required_dependencies:
        try:
            __import__(dependency)
        except ImportError:
            print(f'{red}[!]{dependency} is not installed. Installing...{reset}')
            subprocess.check_call(['pip', 'install', dependency], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"{green} [+] All dependencies are installed now{reset}")
    return True