import random

game_options = ['R', 'P', 'S']

# Input validation
while True:
    user_option = input("Please pick an option Where R is Rocks, P is Papers, and Sis Scissors: ").upper()

    if user_option.upper() not in game_options:
        user_option = print(
            'Invalid!! Please enter a valid option, R for Rocks, P for Papers or S for Scissors ')
        continue
    else:
        comp_choice = random.choice(game_options)

        if user_option == 'R':
            user_choice = 'Rock'
        elif user_option == 'P':
            user_choice = 'Paper'
        else:
            user_choice= "Scissors"

        if comp_choice == 'R':
            cpu_choice = 'Rock'
        elif comp_choice == 'P':
            cpu_choice = 'Paper'
        else:
            cpu_choice = "Scissors"


        print("Player ("+ user_choice +") : CPU ("+cpu_choice+")" )

        if user_choice == cpu_choice:
            print('Tie!!! Restarting game. ')
            continue
        else:
            break

#CHECK WINNER
if (user_option.upper() == 'R' and comp_choice == 'S') or (user_option.upper() == 'P' and comp_choice =='R'):
    result = 'Paper'

elif (user_option.upper() == 'R' and comp_choice == 'S') or (user_option.upper() == 'S' and comp_choice == 'R'):
    result = 'Rock'

else:
    result = 'Scissors'

if result == user_choice:
    print('User Wins')
elif result == cpu_choice:
    print('Computer wins')

