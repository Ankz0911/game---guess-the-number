def restart_program():
    from replit import clear
    should_continue = input("do you want to play again?")
    if should_continue == "y" or "yes":
        clear()
        card_guess()
    else:
        print('thanks for playing')

def card_guess():
    from art import logo
    from random import choice

      
    print(logo)
    print('Welcome to the card guessing game')
    difficulty = input('Select a difficulty: \nEasy , Medium or Hard\n')
    lives = 0
    if difficulty == "easy" : 
        lives = 10
    elif difficulty == "medium" :
        lives = 7 
    else : 
        lives = 5
    numbers = [i for i in range(100)]
    chosen_number = choice(numbers)
    print(f"your remaining lives are: { lives}")
    

    while lives > 0:
        user_guess = int(input("Make a guess:\n"))
        if chosen_number == user_guess :
            print('You win')
            restart_program()
        
        elif chosen_number > user_guess : 
            remainder = chosen_number - user_guess
            if remainder <= 10 :
                print('So close but your guess is slightly lower')
                lives -= 1
                print(f"your remaining lives are: { lives}")

            elif remainder >= 10 and remainder <= 20:
                print('your guess is Slightly low')
                lives -= 1
                print(f"your remaining lives are: { lives}")

            else:
                print('Way Too low')
                lives -= 1
                print(f"your remaining lives are: { lives}")

        else:
            remainder = user_guess - chosen_number
            if remainder <= 10 :
                print("So close but your guess is slightly higher")
                lives -= 1
                print(f"your remaining lives are: { lives}")
            elif remainder >= 10 and remainder <= 20:
                print('Slightly high')
                lives -= 1
                print(f"your remaining lives are: { lives}")
            else:
                print('Too high')
                lives -= 1
                print(f"your remaining lives are: { lives}")

    if lives == 0 : 
        print('you lose')
        restart_program()

card_guess()
