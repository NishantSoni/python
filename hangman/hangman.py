import random
from words import words


def get_random_word():
    random_word = random.choice(words)
    return random_word.upper()


def play_hangman(word):
    display_word = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("lets play the Hangman game...")
    print(show_hangman_states(tries))
    print(display_word)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Kindly guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter - ", guess)
            elif guess not in word:
                print(guess, " is not in the actual word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Great job,", guess, "is present in the actual word!")
                guessed_letters.append(guess)
                word_as_list = list(display_word)
                indices = [i for i, letter in enumerate(
                    word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                display_word = "".join(word_as_list)
                if "_" not in display_word:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed this word ", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                display_word = word
        else:
            print("It is not a valid guess.")

        print(show_hangman_states(tries))
        print(display_word)
        print("\n")

    if guessed:
        print("Congratulations, you guessed the actual word, You have won this game!")
    else:
        print("Sorry, you ran out of tries. The word was " +
              word + ". Please try again")


def show_hangman_states(tries):
    stages = [  # final state: head + torso + both arms + both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head + torso + both hands + one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head + torso + both hands
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head + torso + one hand
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head + torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def main():
    random_word = get_random_word()
    play_hangman(random_word)
    while input("Do you want to play again ? (Y/N) ").upper() == "Y":
        random_word = get_random_word()
        play_hangman(random_word)


if __name__ == "__main__":
    main()
