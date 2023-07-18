# Importing time, random and words modules
import random
import time
from words import word_list


def get_word():
    """"
    Returns a random word from the word list
    """
    word = random.choice(word_list)
    return word.lower()


def hangman(word):
    """
    The main function of the game. Time module makes
    the game more pleasing to play.
    """

    # Welcoming the user
    name = input("What is your name? ")
    print(f"Hello, {name}. Time to play hangman!")

    # Here we set the secret
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    turns = 8

    # Setting up the game
    time.sleep(1)
    print("There is no special characters or numbers in the secret word.")
    print("Start guessing...")
    print(display_hangman(turns))
    print("Secret word: " + word_completion)
    print("\n")
    time.sleep(0.5)

    # Create a while loop and check if the turns are more than zero
    while not guessed and turns > 0:
        guess = input("Please guess a letter or word: ").lower()
        if len(guess) == 1 and guess.isalpha():

            # If player puts a letter that is already guessed
            if guess in guessed_letters:
                print("You already guessed the letter. \
                      Guessed letters:", formatted_letters_list)
                time.sleep(0.5)
            
            # If the guessed letter is NOT found in the secret word
            elif guess not in word:
                formatted_letters_list = " ".join(guessed_letters)
                print(guess, "is not in the word. \
                      Guessed letters:", formatted_letters_list)
                turns -= 1
                guessed_letters.append(guess)
                time.sleep(0.5)

            # If the guessed letter IS found in the secret word
            else:
                print(f"Good job, {guess} is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, char in enumerate(word) if char == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
                time.sleep(0.5)

        # If the player guesses the whole word
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
                time.sleep(0.5)
            elif guess != word:
                print(guess, "is not the word.")
                turns -= 1
                guessed_words.append(guess)
                time.sleep(0.5)
            else:
                guessed = True
                word_completion = word
        
        # If the player guesses a number, a special character
        # or a word that is wrong length.
        else:
            print("Not a single letter or words length is \
            not the same as the secret word.")
            time.sleep(0.5)
        print(display_hangman(turns))
        print("Secret word: " + word_completion)
        print("\n")

    # If the player wins or loses
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of turns. The word was " + word + ". Maybe next time!")

# Displaying the hangman
def display_hangman(turns):
    """
    The steps in hangman
    """
    stages = {
        0: """
                ___________
               | /        |
               |/        ( )
               |         /|\\
               |         / \\
               |
           """,
        1: """
                ___________
               | /        |
               |/        ( )
               |         /|\\
               |         /
               |
            """,
        2: """
                ___________
               | /        |
               |/        ( )
               |         /|\\
               |
               |
            """,
        3: """
                ___________
               | /        |
               |/        ( )
               |
               |
               |
            """,
        4: """
                ___________
               | /        |
               |/
               |
               |
               |
            """,
        5: """
                ___________
               | /
               |/
               |
               |
               |
            """,
        6: """
               | /
               |/
               |
               |
               |
            """,
        7: """
               |
               |
               |
               |
               |
            """,
        8: "",
    }
    return stages[turns]

