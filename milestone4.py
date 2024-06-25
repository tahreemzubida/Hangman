import random
word_list = ["bananas", "mangoes", "pineapples", "grapes", "dates"]
word = random.choice(word_list)
       
class Hangman:
    """
    This class is used to create a game of Hangman.
     
    Attributes: 
    word (str): the random word the player has to guess.
    word_guessed (list): shows the player's progress towards guessing the word.
    num_letters (int): The number of UNIQUE letters in the word that have not been guessed yet.
    num_lives (int): The number of lives the player has left.
    word_list (list): A list of words which the word the player has to guess is randomly picked from.
    """
    def __init__(self, word_list, num_lives=5):
        """
        See help(Hangman) for accurate signature.
        """
        self.word = word 
        self.word_guessed = ["_"] * len(word)
        self.num_letters = len(word)
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
    
    def check_guess(self,guess):
        """
        This function checks if the letter that the player has guessed is in the word.
        
        Parameters:
            guess (str): the letter that the player has guessed.
        """
        guess = guess.lower()
        if guess in word:
            print(f"Well done! The letter {guess} is in the word")
            for index, letter in enumerate(word):
                if letter == guess:
                    self.word_guessed[index] = guess
            self.num_letters = self.num_letters - 1
        else:
            self.num_lives = self.num_lives - 1
            print(f"Sorry, the letter {guess} is not in the word. Try again")
            print(f"You have {self.num_lives} lives left")
        print(self.word_guessed)

    def ask_for_input(self):
        """
        This function asks the player to guess a letter and ensures that their input is valid.
        """
        while True:
            guess = input("Please enter a single letter")
            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You've already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

def play_game(word_list):
    """
    This funcion runs the game and checks the number of letters and lives left to see if it should 
    continue.
        
    Parameters:
        word_list (list): A list of words which the word the player has to guess is randomly picked 
        from.
    """
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print("You have no lives left. Game over")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations, you've won!")
            break
play_game(word_list)

