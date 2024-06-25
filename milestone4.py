import random
word_list = ["bananas", "mangoes", "pineapples", "grapes", "dates"]
word = random.choice(word_list)
    
class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = word 
        self.word_guessed = ["_" * len(word)]
        self.num_letters = len(word)
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
    
    def check_guess(self,guess):
        guess = guess.lower()
        if guess in word:
            print(f"Well done! The letter {guess} is in the word")
            for letter in word:
                if letter == guess:
                    self.word_guessed[letter] = guess
            num_letters = num_letters - 1
        else:
            num_lives = num_lives - 1
            print(f"Sorry, the letter {guess} is not in the word. Try again")
            print(f"You have {num_lives} lives left")

    def ask_for_input(self, guess):
        while True:
            guess = input("Please enter a single letter")
            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You've already tried that letter!")
            else:
                Hangman.check_guess(guess)
                self.list_of_guesses.append(guess)

Hangman.ask_for_input()