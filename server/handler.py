import random

def storage(x):
    name = f"{random.randint(1, 10000000)}.txt"
    with open(name, "w") as file:
        file.write(x)
    print("received and saved as", name)