from game_logic import (
    user_dict,
    reverse_dict,
    get_computer_choice,
    decide_result
)

while True:

    computer=get_computer_choice()

    user_choice=input("Enter your choice(Snake/Water/Gun):").lower()

    if user_choice not in user_dict:
        print("Invalid input! Please choose from Snake, Water, or Gun.")
        continue

    computer_choice=reverse_dict[computer]
    user=user_dict[user_choice]

    print(f"You chose {user_choice}\nComputer chose {computer_choice}")

    result=decide_result(user, computer)

    if result=="tie":
        print("It's a tie!")
    elif result=="win":
        print("You win!")
    else:
        print("You lose!")
    
    play_again=input("Do you want to play again? (yes/no):").lower()
    if play_again!="yes":
        print("Thanks for playing!")
        break