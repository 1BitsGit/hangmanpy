from colorama import Fore
from random_word import RandomWords

# CREDITS TO https://github.com/vaibhavsingh97/random-word created by vaibhavsingh97 for the random word package!
# Give them all the love for making my life SO EASY If you are getting errors run "pip install random_word" and then
# "pip install yaml" in your terminal

while True:

    in_game = False

    print(f"""
    {Fore.CYAN}┌──────────────────────────────────────────────────────────────────────────────────────┐
                         _
                        | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
                        | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ 
                        | | | | (_| | | | | (_| | | | | | | (_| | | | |
                        |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                                           |___/
    {Fore.CYAN}└──────────────────────────────────────────────────────────────────────────────────────┘
                            {Fore.RESET}Type{Fore.LIGHTRED_EX} "help" {Fore.RESET}in any case for a help menu.
                              {Fore.LIGHTMAGENTA_EX}Made by [name omitted lolol] for [my class]! (v1.0)
    {Fore.RESET}
    """)


    def custom_input(message):
        print(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>>>{Fore.WHITE}] {Fore.RESET}", end="")
        input_return = input(message)
        return input_return


    # vars (6 lives for head body two arms two legs)

    guess = ""
    lives = 6
    hints = 0
    egg = False
    r = RandomWords()
    word = r.get_random_word(hasDictionaryDef="true", maxLength=7, minLength=3).upper()
    menu = len(word) * "_ "
    guessed_letters = []
    completed = False

    # int line 4 usr

    while in_game is False:
        initial_input = custom_input("").lower()
        if initial_input == "help":
            print("""Help menu:
            **note, case doesn't matter.
            start -> starts the game
            settings -> modify your settings
            quit -> leave the game
            leave -> exit the settings menu""")
        elif initial_input == "debug":
            print(word)
        elif initial_input == "rr":
            word = r.get_random_word(hasDictionaryDef="true", maxLength=7, minLength=3).upper()
            print(word)
        elif initial_input == "egg = true":
            egg = True
            # hi !
        elif initial_input == "start":
            print(f"{Fore.LIGHTGREEN_EX}You're in game now! Type a letter to begin.{Fore.RESET}")
            in_game = True
        elif initial_input == "settings":
            print(f"""Settings are as follow:
            You have: {lives} lives.
            You have: {hints} hints.
            type "leave" to exit settings, type hints/lives to change their value""")
            while True:
                setting_input = custom_input("").lower()
                if setting_input == "leave":
                    print("leaving")
                    break
                elif setting_input == "quit:":
                    quit("Thanks for playin!")
                elif setting_input == "settings":
                    print("You're already in settings! Here are your settings though: (type leave to leave)")
                    print(f"""Settings are as follow:
                            You have: {lives} lives.
                            You have: {hints} hints.
                            type "leave" to exit settings, type hints/lives to change their value""")
                elif setting_input == "hints":
                    hints = int(input("How many hints do you want? "))
                elif setting_input == "lives":
                    lives = int(input("How many lives do you want? "))
                else:
                    print("You're still in the settings menu, type leave to leave or type in hints or lives to change those values.")
        elif initial_input == "quit":
            quit("Thanks for playin!")
        else:
            print("Sorry! I don't get what you mean, type help for more help")

    while in_game is True and completed is False:
        guess = custom_input("").upper()
        if guess in guessed_letters:
            print(f"""{Fore.BLUE}Sorry "{guess}", matches one of your guessed letters! 
            ({guessed_letters}){Fore.RESET}""")
            print()
        elif guess not in word:
            lives -= 1
            print(f"{Fore.RED}Sorry, that isn't in the word.{Fore.RESET}")
            guessed_letters.append(guess)
        elif guess in word and len(guess) == 1:
            print(f"{Fore.BLUE}Awesome! You got a letter! {Fore.RESET}")
            guessed_letters.append(guess)
        elif len(guess) == len(word):
            if guess == word:
                print(f"{Fore.LIGHTMAGENTA_EX}You've guessed the word!{Fore.RESET}")
                completed = True
            else:
                print(f"{Fore.RED}Sorry, that's not the correct word.{Fore.RESET}")
                lives -= 1
        elif len(guess) > len(word) or len(guess) > 3:
            print(f"{Fore.BLUE}It seems like you tried to guess the word, but it was too long/short.{Fore.RESET}")
            print()
        if completed is False:
            ig_menu = ""
            for letters in word:
                if letters in guessed_letters:
                    ig_menu += letters
                else:
                    ig_menu += "_ "
            print(f"{ig_menu} (You still have {lives} lives/life left.)")
        if ig_menu == word:
            print(f"{Fore.LIGHTMAGENTA_EX}Congratulations! You've guessed the word, {Fore.WHITE}{word}! "
                  f"{Fore.LIGHTMAGENTA_EX}You had {Fore.WHITE}{lives}{Fore.LIGHTMAGENTA_EX} lives left!{Fore.RESET}")
            print()
            completed = True
            repeat_game = input("Do you want to play again? Y/N ").lower()
            if repeat_game == "y":
                in_game = False
            elif repeat_game == "n":
                quit("Thanks for playing, see ya!")
            else:
                print("I don't know what that input is, type y/n")
        if lives == 0:
            print(f"{Fore.RED}Sorry! You ran out of lives!")
            repeat_game = input("Do you want to play again? Y/N ").lower()
            print()
            if repeat_game == "y":
                in_game = False
                continue
            elif repeat_game == "n":
                quit("Thanks for playing, see ya!")
            else:
                print("I don't know what that input is, type y/n")
