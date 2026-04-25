#from vaia import guess
# luckynums= []
# for i in range(6):
#     num= random.randint(1,10)
#     if luckynums.count(num) > 0:
#         continue
#     else:
#         luckynums.append(num)
#         print(luckynums)

# luckynums= []
# while True:
#     if len(luckynums) == 6:
#         break
#     num = random.randint(1,10)
#     if luckynums.count(num) > 0:
#         continue
#     else:
#         luckynums.append(num)
#         print(luckynums)


# luckynums= []
# while True:
#     if len(luckynums) == 6:
#         break
#     num = random.randint(1,90)
#     if luckynums.count(num) > 0:
#         continue
#     else:
#         luckynums.append(num)
#         print(luckynums)
#     if guess > n:
#         print("too high")
#     if guess < n:
#         print("Too low")
# print("Congratulations! You won! ")
#
# maxn= 90
# print("Welcome to the guessing game! \n"
#       "Guess the number from 1 to 90.\n"
#       "You only have a minimum of 2 trials and a maximum of 6 trials")
# guess= None
# while guess!= input("Input your try:"):
#     luckynums= random.sample(range(1,91))
# if guess == luckynums:
#     again= int(input("Input your try:"))
#     val= input("Do you still want to proceed with guessing? \n"
#                "Input Yes or No:")
#     if val == "Yes":
#         print("Start again from top")
#     elif val == "No":
#         print(luckynums)
#     else:
#         print("Invalid Input!")
# elif guess == luckynums:
#     nuo= int(input("Input your try:"))
# elif guess == luckynums:
#     nil= int(input("Input your try:"))
# elif guess == "Q":
#     print("Exited Successfully. Bye!")
# else:
#     print("Better luck next time")
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
        break
guess= int(trial)
if guess < 1 or guess > maxn:
    print(f"Please enter a number between 1 and {maxn}")
elif guess in userguesses:
    print("You have already guessed that number!")
else:
    userguesses.append(guess)
print("Here are the results!")
correct= 0
for i in userguesses:
    if i in luckynums:
        correct= correct+1

