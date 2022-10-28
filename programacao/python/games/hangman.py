import random
from clear import clear_screen


def play():
    secret_word = load_secret_word()
    guessed_letters = initialize_guessed_letters(secret_word)
    errors = 0
    hanged = False
    guessed = False

    display_round(errors, guessed_letters)

    while not hanged and not guessed:
        guess = ask_for_guess()

        if guess in secret_word:
            mark_correct_guess(guess, guessed_letters, secret_word)
        else:
            errors += 1

        clear_screen()
        display_round(errors, guessed_letters)

        hanged = errors == 6
        guessed = "_" not in guessed_letters

    if guessed:
        display_victory_message(secret_word)
    else:
        display_defeat_message(secret_word)


def display_round(errors, guessed_letters):
    print(
        """****************************
Welcome to the Hangman game!
****************************
"""
    )
    draw_gallows(errors)
    print(" ".join(guessed_letters))


def load_secret_word(filename="words.txt", first_valid_line=0):
    with open(filename, "r") as file:
        words = [line.strip() for line in file]

    secret = random.randrange(first_valid_line, len(words))
    return words[secret].upper()


def initialize_guessed_letters(word):
    return ["_" for _ in range(len(word))]


def ask_for_guess():
    guess = input("Guess a letter: ")
    guess = guess.strip().upper()
    return guess


def mark_correct_guess(guess, guessed_letters, secret_word):
    for index, letter in enumerate(secret_word):
        if guess == letter:
            guessed_letters[index] = letter


def draw_gallows(errors):
    print(
        """  _______
 |/      |"""
    )

    if errors == 0:
        print(
            """ |
 |
 |
 |"""
        )

    if errors == 1:
        print(
            """ |      (_)
 |
 |
 |"""
        )

    if errors == 2:
        print(
            """ |      (_)
 |       |
 |       |
 |"""
        )

    if errors == 3:
        print(
            """ |      (_)
 |      \\|
 |       |
 |"""
        )

    if errors == 4:
        print(
            """ |      (_)
 |      \\|/
 |       |
 |"""
        )

    if errors == 5:
        print(
            """ |      (_)
 |      \\|/
 |       |
 |      /"""
        )

    if errors == 6:
        print(
            """ |      (_)
 |      \\|/
 |       |
 |      / \\"""
        )

    print(
        """ |
_|___
"""
    )


def display_victory_message(secret_word):
    print(
        """       ___________
      '._==_==_=_.'
      .-\\\\:      /-.
     | (|:.     |) |
      '-|:.     |-'
        \\\\::.   /
         '::. .'
           ) (
         _.' '._
        '-------'
Congratulations, you won!"""
    )


def display_defeat_message(secret_word):
    print(
        f"""    _______________
   /               \\
  /                 \\
//                   \\/\\
\\|   XXXX     XXXX   | /
 |   XXXX     XXXX   |/
 |   XXX       XXX   |
 |                   |
 \\__      XXX      __/
   |\\     XXX     /|
   | |           | |
   | I I I I I I I |
   |  I I I I I I  |
   \\_             _/
     \\_         _/
       \\_______/
Gosh, you've been hanged!
The secret word was {secret_word}"""
    )


if __name__ == "__main__":
    play()
