from sys import maxunicode

# ## Dict
# person = {
#     'firstname': "John",
#     'lastname': "Smith",
#     'age': 30,
#     'courses': ['java', 'graphics', 'python'],
# }
# print(person)
# print(person['firstname'])
# print(person['age'])
# print(person['courses'][1])
# print(person.keys())
# print(person.values())
# print(person.items())


 # #### Control flow
# ## Conditional Statement
#entry = input("enter your name")
#print(f"hello {entry}")

# # if
# if codition
#   expression
# entry = input("Enter your name: ").capitalize()
# if entry == "Vaia" or entry == "Victoria" or entry == "Victoria Joseph":
#         print(f"Hello {entry}")
 # # # if, else
 #if condition:
 #  expression
 #else:
 #  defaultExpression
# entry = input("Enter your name: ").capitalize()
# if entry == "Vaia" or entry == "Victoria" or entry == "Victoria Joseph":
#         print(f"Hello {entry}")
# else:
#     print(f"{entry} is unknown")
# name1 = "Johndoe"
# name2 = "John123"
# entry1 = input("Enter your username: ")
# entry = input("Enter your password: ")
# entry2 = input("Welcome to your account dashboard")
# if entry1 == name1 and entry2 == name2 :
#     print("elcome to your account dashboard")
# else:
#     print("Invalid Credentials")
# username = input("Enter your username: ")
# password = input("Enter your passord: ")
# if username == "JohnDoe" and password == "John123":
#     print("elcome to your account dashboard")
# else:
#     print("Invalid Credentials")
# # # ##PSUEDOCODES
# ## FOR & WHILE LOOP
#counter=0
# while counter<11:
#     print(counter, end=" ")
#     counter=counter+1
# for n in range(1,21):
#     print(n**2, end=" ")
# for x in range(1,101):
# #     print(x//2, end=" ")
# for x in range(1,51):
#     print(x%2, end=" ")


import random

maxn = 10
print("Welcome to guess the number game!")
print("Guess the number from 1 to", maxn)
n = random.randint(1,maxn)
guess= None
while guess!= n:
    guess = int(input("Input your try:"))
    if guess > n:
        print("too high")
    if guess < n:
        print("Too low")
print("Congratulations! You won! ")

# # ## ### Dictionary
print("What do you want to do?")
print("Or enter Q to [Q]uit")
action= input()
if action == "Q":
    print("Bye")

