import random

RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

def storage(x):
    name = f"{random.randint(1, 10000000)}.txt"
    with open(name, "w") as file:
        file.write(x)
    print("received and saved as", name)