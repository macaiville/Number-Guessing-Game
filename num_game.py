import random


print('Welcome To the Number Guessing Game!')
print('Im Thinking of a Number between 1 and 100.')
how_hard = input("Choose a difficulty. Type 'easy' or 'hard' :")


number = random.randint(1, 101)
lives = 0
if how_hard == "easy":
    lives = 10
elif how_hard == "hard":
    lives = 5
else:
    print('Invalid Response')
    lives = 0

print(number)
while lives > 0:
    print(f"You have {lives} remaining")
    guess = int(input("Guess A Number: "))
    if guess < number:
        print("Too Low")
        print("Guess Again")
        lives -= 1
    elif guess > number:
        print("Too High")
        print("Guess Again")
        lives -= 1
    elif guess == number:
        print('You Guessed the Number!')
        lives = 0
    else:
        print('You ran Out of lives. Play Again')
        break

if lives == 0:
    print(f"You ran out of lives. The correct number was, {number}")




