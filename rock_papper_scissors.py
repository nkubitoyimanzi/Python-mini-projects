import random

options = ["r", "p", "s"]
options_emojis = {"r": "✊", "p": "✋", "s": "✌️"}
playing_times = int(input("How many times do you want to play: "))

for times_num in range(playing_times):
    print(f"\nRound {times_num + 1}")
    random_letter = random.choice(options)

    while True:
        user_choice = input("Choose one from [R, P, S]: ").lower()
        if user_choice in options:
            break
        print("Invalid input!")

    print(f"You chose {options_emojis[user_choice]}, computer chose {options_emojis[random_letter]}")

    if user_choice == random_letter:
        print("It's a Tie")
    elif (
        (user_choice == "r" and random_letter == "s") or
        (user_choice == "s" and random_letter == "p") or
        (user_choice == "p" and random_letter == "r")
    ):
        print("Congrats! You win")
    else:
        print("Computer wins")
