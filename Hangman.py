# Simple Hangman Game
import random


word_list = ["python", "laptop", "keyboard", "monitor", "internet"]

word = random.choice(word_list)

guessed_word = ["_"] * len(word)
guessed_letters = []
attempts = 6

print("Welcome to Hangman!")
print("Guess the word:", " ".join(guessed_word))

while attempts > 0 and "_" in guessed_word:
    guess = input("Enter a letter: ").lower()

    # Validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    # Check guess
    if guess in word:
        print("Correct guess!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        attempts -= 1
        print("Wrong guess! Attempts left:", attempts)

    print("Word:", " ".join(guessed_word))
    print("Guessed letters:", guessed_letters)
    print()

# Result
if "_" not in guessed_word:
    print("Congratulations! You guessed the word:", word)
else:
    print("Game Over! The word was:", word)
