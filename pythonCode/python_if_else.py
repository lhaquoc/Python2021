import random


def get_choice(choice):
    if choice == 'R':
        return 'Rock'
    elif choice == 'P':
        return 'Paper'
    elif choice == 'S':
        return 'Scissors'
    else:
        return 'Not a valid choice'


def main():
    print('Welcome to Rock, Paper, Scissors Game')
    print('[R]=Rock, [P]=Paper, [S]=Scissors and [Q]=Quit game')
    game_choices = ['R', 'P', 'S']
    counter = 1
    game_on = True
    while game_on:
        user_choice = input(f'Game #{counter}. Please enter your choice:')
        user_choice = user_choice.upper()

        if user_choice == 'Q':
            print('Thanks for joining! Have a good day')
            game_on = False
        else:
            random_index = random.randint(0, 2)
            computer_choice = game_choices[random_index]
            print(
                f'you selected {get_choice(user_choice)} vs Computer choice is {get_choice(computer_choice)}')
            # winning rules
            if user_choice == 'R' and computer_choice == 'S':
                print('Congrats, you win. Rock beats Scissors')
            elif user_choice == 'P' and computer_choice == 'R':
                print('Congrats, you win. Paper covers Rock')
            elif user_choice == 'S' and computer_choice == 'P':
                print('Congrats, you win. Scissors cuts Paper')
            elif user_choice == 'R' and computer_choice == 'P':
                print('Sorry, computer wins. Paper covers Rock')
            elif user_choice == 'P' and computer_choice == 'S':
                print('Sorry, computer wins. Scissors cuts Paper')
            elif user_choice == 'S' and computer_choice == 'R':
                print('Sorry, computer wins. Rock beats Scissors')
            elif user_choice == computer_choice:
                print(f"It's draw. Both you and computer selected {get_choice(computer_choice)}")
            else:
                print('Invalid input. Please enter [R, P, S, or Q] only')
            counter += 1
        print('-'*40)


if __name__ == '__main__':
    main()
