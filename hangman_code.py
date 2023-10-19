from random_word import RandomWords
import re

# Create an instance of the RandomWords class
r = RandomWords()

# Get a random word
random_word = r.get_random_word()
wrong_guesses = 0
guessed_letters = set()


def draw_hangman(wrong_guesses):
    # Draw hangman based on the number of wrong guesses
    if wrong_guesses == 1:
        print(" " * 5, "O")
    elif wrong_guesses == 2:
        print(" " * 5, "O")
        print(" " * 4, "/", end='')
    elif wrong_guesses == 3:
        print(" " * 5, "O")
        print(" " * 4, "/", end='')
        print("|", end='')
    elif wrong_guesses == 4:
        print(" " * 5, "O")
        print(" " * 4, "/", end='')
        print("|", end='')
        print("\\")
    elif wrong_guesses == 5:
        print(" " * 5, "O")
        print(" " * 4, "/", end='')
        print("|", end='')
        print("\\")
        print(" " * 4, "/", end='')
    elif wrong_guesses == 6:
        print(" " * 5, "O")
        print(" " * 4, "/", end='')
        print("|", end='')
        print("\\")
        print(" " * 4, "/", end='')
        print('', "\\")


def main():
    global random_word, wrong_guesses, guessed_letters
    word_reveal = re.sub("[a-z]", "_", random_word)
    while True:
        # Inputting Guesses
        while True:
            # Keep a new line else drawing won't work.
            print("\n", word_reveal)
            guess = input("Letter: ").strip().lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Only ONE LETTER can be guessed at a time.")
            else:
                break

        if guess in random_word:
            guessed_letters.add(guess)
            # Update word_reveal based on the guessed letters
            new_word_reveal = ''
            for letter in random_word:
                if letter in guessed_letters:
                    new_word_reveal += letter
                else:
                    new_word_reveal += '_'
            word_reveal = new_word_reveal
        else:
            wrong_guesses += 1
            draw_hangman(wrong_guesses)

        if word_reveal == random_word:
            print("Congratulations, you won! The word is:", random_word)
            break

        if wrong_guesses == 6:
            print(f"You have lost hangman. The word was {random_word}.")
            break


main()
