import random
maxn=90
luckynums= random.sample(range(1,maxn+1),6)
userguesses=[]
print("Welcome to the lottery system!")
print(f"Guess 6 numbers between 1 and {maxn}.")
print("Enter Q or Quit to stop. (You have minimum 2 guesses)")
while len(userguesses) <6:
    trial= input(f"Trial{len(userguesses) +1}:")
    if trial.lower() == "Q" or trial.lower() == "Quit":
        if len(userguesses) < 2:
            print("You must enter a minimum of 2 guesses!")
    else:
        guess= int(trial)
        if guess < 1 or guess > maxn:
            print(f"Please enter a number between 1 and {maxn}")
        elif guess in userguesses:
            print("You have already guessed that number!")
        else:
            userguesses.append(guess)
print("Here are the results!")
print("Your Guesses:", userguesses)
print("The Lucky Numbers:", luckynums)
correct= 0
for i in userguesses:
    if i in luckynums:
        correct= correct+1
if correct == 1:
    print("Sorry you guessed only one correctly!")
if correct == 2:
    print("Congratulations you guessed 2 correctly!")
if correct == 3:
    print("Congratulations you guessed 3 correctly!")
if correct == 4:
    print("Congratulations you guessed 4 correctly!")
if correct == 5:
    print("Congratulations you guessed 5 correctly!")
if correct == 6:
    print("Congratulations you just on a JACKPOT!")
if correct == 0:
    print("Better luck next time")

