import random

RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

def storage(x):
    n = f"{random.randint(1, 10000000)}.txt"
    with open(n, "w") as file:
        file.write(x)
    print(GREEN,"[*] Received and saved as : ", n,RESET)