import random

words= ['apple','happy','music','smile','error']
word= random.choice(words)
guesses=['_']*len(word)
attempts=6
guessedletters=[]
print("Welcome to Hangman!")
print("Programmed by: Ritika Talwar")

while attempts>0 and "_" in guesses:
    print("\nWord: " + "".join(guesses))
    print(f"Attempts left: {attempts}")
    guess= input("Enter a letter to guess the word: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single letter.")
        continue
    if guess in guessedletters:
        print("Letter guessed already.")
        continue
    guessedletters.append(guess)

    if guess in word:
        for i,l in enumerate(word):
            if l==guess:
                guessed[i]=guess
        print("Correct Guess!")
    else:
        attempts -= 1
        print("Wrong Guess!")

if '_' not in guesses:
    print(f"\nCongratulations! You guessed the word correctly: {word}")
else:
    print(f"\nGame Over! The word was: {word}")
