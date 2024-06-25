import random

word_list = ["bananas", "mangoes", "pineapples", "grapes", "dates"]
print(word_list)

word = random.choice(word_list)
print(word)

guess = input("Please enter a single letter")

if len(guess) == 1 and ((guess >= 'a' and guess <= 'z') or (guess >= 'A' and guess <= 'Z')):
    print("Good guess!")
else:
    print("That is not a valid input")

