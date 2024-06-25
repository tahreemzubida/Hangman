import random
word_list = ["bananas", "mangoes", "pineapples", "grapes", "dates"]
word = random.choice(word_list)
    
def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Well done! The letter {guess} is in the word")
    else:
        print(f"Sorry, the letter {guess} is not in the word. Try again")

def ask_for_input():
    while True:
        guess = input("Please enter a single letter")
        if len(guess) == 1 and guess.isalpha() == True:
            print("Good guess!")
            break
        else:
            print("Invalid letter. Please enter a single alphabetical character.")
            break
    check_guess(guess)

ask_for_input()