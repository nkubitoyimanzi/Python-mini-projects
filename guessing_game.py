import random
choice = ""
random_number = random.randint(1, 10)
while choice != random_number:
    try:
        choice = int(input("Choose any number: "))
    except ValueError:
        print("No this is not a number")
        continue
    if choice < random_number:
        print("too small")
    elif choice > random_number:
        print("too big")
    else:
        print("Congulations you did it!!!")
