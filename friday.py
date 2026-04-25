# entry = input("Enter your name: ")
# if entry == "John":
#     print(f"Welcome {entry}")
#     print("Successful")
# else:
#     print(f"We don't know {entry}")
#     print("Failed")

# # true Expression if condition else default expression
# entry = input("Enter your name: ")
# print(f"Welcome {entry}") if entry == "John" else print(f"We don't know {entry}")

# ### if, elif, else
# if condition1:
#     expression1
# elif conditionN:
#     expressionN
# else:
#     defaultExpression

# wallet = float(input("How much do you have: "))
# if wallet >= 1500:
#     print("Visit the NEPO babies (Fhasasi or Teniola")
# elif wallet >= 1000:
#     print("Visit Uche, Delight or Pearl")
# elif wallet >= 400:
#     print("Visit Fareed or Victoria")
# else:
#     print("Stay at home")

# Graderemark= int(input("input your score:"))
# if Graderemark >= 101:
#     print("No Grade")
# elif Graderemark >= 80 :
#     print("A1 Excellent")
# elif Graderemark >= 70:
#     print("B2 Very Good")
# elif Graderemark >= 65:
#     print("B3 Good")
# elif Graderemark >= 60:
#     print("C4 Credit")
# elif Graderemark >= 55:
#     print("C5 Credit")
# elif Graderemark >= 50:
#     print("C6 Credit")
# elif Graderemark >= 45:
#     print("D7 Pass")
# elif Graderemark >= 40:
#     print("E8 Pass")
# else:
#     print("Fail")

# score = input("Enter a score: ")
# if score.isnumeric():
#     mark = float(score)
#     if mark > 100:
#         print(f"{mark} can't be greater than 100")
#     elif mark >= 80:
#         print("A1 Excellent")
#     elif mark >= 70:
#         print("B2 Very Good")
#     elif mark >= 65:
#         print("B3 Good")

    # if mark >= 80 and mark <= 100:
    # if 80 <= mark <= 100:
    #     print("A1 Excellent")
    # elif 70 <= mark <= 79:
    #     print("B2 Very Good")
    # else:
    #     print("Invalid")
# else:
#     print(f"{score} is not a number value"
#           f"Please input score again")

Username=input("Enter your username:").capitalize()
Password=input("Enter your Password:").capitalize()
if Username == "Vaia" and  Password == "Victoria07":
    print("Welcome to your account, Vaia.")
    print("What would you like to do today, Vaia?")
    print("Or enter Q to Quit.")
    action=input()
    if action=="Q":
        print("Bye Vaia.")
    else:
        print("Play guess the number game")
        import random
        maxn=10
        print("Welcome to 'Guess the number game'!")
        print("Guess the number from 1 to", maxn)
        n = random.randint(1, maxn)
        guess = None
        while guess!=n:
            guess = int(input("Input your try:"))




else:
    print("Invalid Credentials")
    print("Check your password or username for errors")




