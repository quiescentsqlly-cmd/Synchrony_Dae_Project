# Setting variables & Importing
import random
coins = 50
wager = 0
games = ["1. carnival wheel", "2. guess the number", "3. roulette", "4. end"]

# defining the title part of the game; lets you go back and choose a different game
def display_title_screen():
    while True:
        print("~~~~~~~~~~~~~~~~~~~~")
        print(" $ *   CASINO  *  $ ")
        print("~~~~~~~~~~~~~~~~~~~~")
        print()
        print("Options:")

        for option in games:
            print(option.title())

        print("-----------------------------------------------------")

        try:
            choice = int(input("Enter your choice (1-4): "))

            if choice == 1:
                print("Loading:", games[0].title())
                display_carnival_wheel()

                if coins <= 0:
                    return

            elif choice == 2:
                print("Loading:", games[1].title())
                display_guess_the_number()

                if coins <= 0:
                    return

            elif choice == 3:
                print("Loading:", games[2].title())
                display_roulette_game()

                if coins <= 0:
                    return

            elif choice == 4:
                print("Goodbye!")
                break

            else:
                print("Error: Please enter a number between 1 and 4.")

        except ValueError:
            print("Please enter a valid integer from 1 to 4.")
    

# ---------------------------------------------------------------------------------------------------------------------------------

# Defining the guessing number game... T'T
def display_guess_the_number():
    global coins
    max_attempts = 10

    while True:
        if coins == 0:
            print("You have no coins left!")
            print(" ")
            print(" ")
            print("GAME OVER! Re-run this code if you wish to play again.")
            return

        # Title
        print("~~~~~~~~~~~~~~~~~~~~")
        print("  GUESS THE NUMBER  ")
        print("~~~~~~~~~~~~~~~~~~~~")
        print()
        print("Welcome to Guess the Number" + ", " + name.title() + "!")
        print()
        print("The rules are simple; I am thinking of a number, and you have to guess it in 10 tries or less.")
        print("If you do, great! Your wager will DOUBLE. If you don't, then you LOSE that money :'(")
        print()
        print("With that in mind... How much do you want to wager?")
        print("You have", coins, "coins.")

        # Betting
        while True:
            try:
                gtnwager = int(input("Enter your wager: "))

                if gtnwager <= 0:
                    print("Please set your wager to a number greater than zero.")

                elif gtnwager <= coins:
                    coins -= gtnwager
                    print("OK! You now have", coins, "coins.")
                    print("If you guess correctly, you get", gtnwager * 2, "coins.")
                    break

                else:
                    print("Please enter a number less than or equal to", coins)

            except ValueError:
                print("Please enter a valid integer.")

        print("--------------------------------------------------------------")

        # Secret number and attempts
        secret_number = random.randint(1, 1000)
        attempts = 0
        won = False

        print("I am thinking of a number between 1 and 1000.")

        while attempts < max_attempts:
            try:
                print("--------------------------------------------")
                guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter guess: "))

                if guess < 1 or guess > 1000:
                    print("Out of bounds! Guess a number between 1 and 1000.")
                    continue

                attempts += 1

                if guess < secret_number:
                    print()
                    print("Too low! Guess higher! ⬆")
                elif guess > secret_number:
                    print()
                    print("Too high! Guess lower! ⬇")
                else:
                    won = True
                    break

            except ValueError:
                print("Invalid input. Please enter a valid number.")

        # Winning or losing
        if won:
            winnings = gtnwager * 2
            coins += winnings
            print("\nCONGRATULATIONS! You guessed the number in", attempts, "tries.")
            print("You earned", winnings, "coins. You now have", coins, "coins.")
        else:
            print("\nOh no! You lost :(")
            print("The number was", secret_number)
            print("You now have", coins, "coins.")

        # Play again
        play_again = input(
            "Do you want to play again? (yes/no): ").strip().lower()

        if play_again in ["yes", "y"]:
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                continue
        else:
            print(f"Thanks for playing! You finished with {coins} coins.")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            display_title_screen()
            break
# ------------------------------------------------------------------------------------------------------------------------------------
# defining the roulette game

def display_roulette_game():
# setting variables; addressing the coins variable as global or else it wont work :/
    global coins
    colors = ["red", "black", "white", "gold", "blue"]
    roulette_results = random.choice(colors)
    won = False
# prints the titlee

    
    while True:
        if coins <= 0:
            print("You have no coins left!")
            print("GAME OVER! Re-run this code if you wish to play again.")
            return
        else:
            print("~~~~~~~~~~~~~~~~~~~~")
            print("  ~   ROULETTE  ~   ")
            print("~~~~~~~~~~~~~~~~~~~~")
            print()
            print("Welcome to Roulette, " + name.title() + "!")
            print()
            print("In this game, a random color out of 5 is chosen by me, and you have to guess it C; Choose a color and wager on your choice")
            print("")
            print("Albeit risky, you have the opportunity to multiply your wager by 3!")
            print()

            print("~ ~ ~ YOU HAVE", coins, "COINS. ~ ~ ~")
            print()
            print("Please guess on color,", name.title() + ". After you select, the computer will reveal the secret color.")
            print()
            print("OPTIONS:")#listing ur color options

            for color in colors:
                print(color.title())

            print()
        while coins > 0: #making sure ur 
            user_guess = input("Your guess: ").strip().lower()

            if user_guess not in colors:
                print("\nPlease guess on one of the colors below:")
                for color in colors:
                    print(color.title())
                continue
            else:
                print("")
                break

        while True:
                    try:
                        r_wager = int(input("How much are you willing to bet? Look up to see how many coins you have: "))

                        if r_wager <= 0:
                            print("Please set your wager to a number greater than zero.")

                        elif r_wager <= coins:
                            coins -= r_wager
                            print()
                            break

                        else:
                            print("Please enter a number less than or equal to", coins)

                    except ValueError:
                        print("Please enter a valid integer.")

        secret_color = random.choice(colors)
        if user_guess == secret_color:
            print("CONGRATS! You guessed correctly :) It was", secret_color)
            won = True
        else:
            print("Aw :( you didn't get it, it was", secret_color)

        if won:
            winnings = r_wager * 3
            coins += winnings
            print("You earned", winnings, "coins. You now have", coins, "coins.")

            play_again = input("Do you want to play again? (yes/no): ").strip().lower()

            if play_again in ["yes", "y"]:
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                continue
            else:
                print(f"Thanks for playing! You finished with {coins} coins.")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                display_title_screen()
                break
        else:
            print("You now have", coins, "coins.")

            play_again = input("Do you want to play again? (yes/no): ").strip().lower()

            if play_again in ["yes", "y"]:
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                continue
            else:
                print(f"Thanks for playing! You finished with {coins} coins.")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                display_title_screen()
                break






 # ------------------------------------------------------------------------------------------------------------------------------------
# defining the wheel of fortune game FINALLY OMG LAST THING IM SOOOO SOOO SOOO EXCITEDD
def display_carnival_wheel():
    global coins

    wheel_prizes = [
        "BANKRUPT", "-2", "-2", "-2", "-3", "-5",
        "NOTHING", "2", "2", "2", "3", "5"
    ]

    while True:
        if coins <= 0:
            print("You have no coins left!")
            print("GAME OVER! Re-run this code if you wish to play again.")
            return

        print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("  ~   CARNIVAL WHEEL  ~   ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print()
        print("Welcome to Wheel of Fortune, " + name.title() + "!")
        print()
        print("In this game, a (metaphorical) wheel is spun to determine prizes.")
        print("The number you land on is multiplied by your wager.")
        print("Be wary! Some numbers will SUBTRACT FROM YOUR WAGER!")
        print()
        print("You currently have", coins, "coins.")
        print()
        print("PRIZES/PENALTIES:")
        print("---------------------------------------")

        for prize in wheel_prizes:
            print(prize)

        print("---------------------------------------")
        print("(BANKRUPT resets your coins to ZERO and ends the game)")
        print("(NOTHING returns your wager without a profit)")
        print()

        # Get a valid wager
        while True:
            try:
                cnwager = int(input("Enter your wager: "))

                if cnwager <= 0:
                    print("You can't bet nothing! Enter a number greater than zero.")

                elif cnwager > coins:
                    print("Please enter a number less than or equal to", coins)

                else:
                    coins -= cnwager
                    print()
                    print("OK! You now have", coins, "coins.")
                    break

            except ValueError:
                print("Please enter a valid integer.")

        # Spin a NEW wheel every round
        wheel_choice = random.choice(wheel_prizes)

        print("-----------------------------------------")
        print("The wheel has spun!")
        print()
        print("It landed on ... *drumroll*")
        print(".")
        print(".")
        print(".")
        print(".")
        print()
        print(wheel_choice + "!")
        print()

        # Handle the result
        if wheel_choice == "BANKRUPT":
            coins = 0
            print("Oh no! You landed on BANKRUPT!")
            print("You now have", coins, "coins.")
            print("GAME OVER! Re-run the program if you wish to play again.")
            print("Thank you for playing!")
            return

        elif wheel_choice == "NOTHING":
            coins += cnwager
            print("Seems you don't earn anything.")
            print("You now have", coins, "coins.")

        else:
            multiplier = int(wheel_choice)
            winnings = cnwager * multiplier
            coins += winnings

            if multiplier > 0:
                print("Your wager earned", winnings, "coins!")
            else:
                print("Oh no! You lost", abs(winnings), "extra coins!")

            print("You now have", coins, "coins.")

        print()

        # Check whether the player can continue

        if coins <= 0:
            print("It seems you're well out of coins :(")
            print()
            print("GAME OVER!")
            print()
            print("Re-run the code if you wish to try again.")
            print("Thanks for playing!")
            break

        # Ask to play another round
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()

        if play_again in ["yes", "y"]:
            print("\n" * 5)
            continue
        else:
            print(f"Thanks for playing! You finished with {coins} coins.")
            print("\n" * 5)
            display_title_screen()
            return
        




    
                    


    
# Title - I DON't KNOW THE NAME YET >:##
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print("~~~~~~~~~~~~~~~~~~~~")
print(" $ *   CASINO  *  $ ")
print("~~~~~~~~~~~~~~~~~~~~")

# Title 2x

print(" ")
print("WELCOME! Hope you enjoy your stay :)")
name = input("Enter your name: ")
print(" ")
print("Hello,", name.title() + "!", "Welcome to my Casino :)")
print(" ")
print("Here, you have a choice of 3 games that you could wager on and earn or lose coins.")
print("Gamble responsibly! You currently have", str(coins), "coins. If you lose them all, you're out of here!")
print(" ")
print("(The wagering mechanics in this game are for fictional entertainment only. I do not condone real-life gambling ^_^)")
print("-------------------------------------------------------------------------------------------------------------------------")
print("With THAT being said... What would you like to do?")

# Prints game options

print("Options: ")
for option in games:
    print(option.title())

# make every coin thingy in a string

# Choosing a game
print(" ")


print("-----------------------------------------------------")

while True: # New While Loop! The boolean value TRUE makes the loop run indefinitely because there is no statement that makes it false! Therefore it breaks when I say it does B)
    try:
        choice = int(input("Enter your choice (1-4): "))
        
        if 1 <= choice <= 3:
            print("Loading:", games[choice - 1].title())
            print(".")
            print(".")
            print(".")
            print(" ")
            print(" ")
            break # COMPLETELY TERMINATES PROGRAM! (not the entire code but... the loop) IF youd want it to just stop an inner function, use return
        elif choice == 4:
            print(" ")
            print("Thanks for playing!!")
            break 
        else:
            print("Error: Please enter a number between 1 and 4.")
            print("Options:")
            for option in games:
                print(option.title())
                
    except ValueError:
        print("Please enter a valid integer from 1 to 4.")

if choice == 1:
    display_carnival_wheel()
elif choice == 2:
    display_guess_the_number()
elif choice == 3:
    display_roulette_game()




# kay is forcing us to add a comment to our code :/
