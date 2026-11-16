import random

count = int(input("How many times dou wanna play? \n :"))
current_roll = 0

while current_roll <= count: 
    choice = input(">")
    if choice == 'y':
       x = random.randint(1,6)
       y = random.randint(1,6)
       print(f"({x},{y})")
       current_roll += 1
       print(f"you've played {current_roll} times")
    elif choice == 'n':
        print("Thank you for playing")   
        break 

    else:
        print("Invalid input \n >")






