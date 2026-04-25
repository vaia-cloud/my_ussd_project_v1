
# ## Dict
person = {
    'firstname': "John",
    'lastname': "Smith",
    'age': 30,
    'courses': ['java', 'graphics', 'python'],
}
print(person)
print(person['firstname'])
print(person['age'])
print(person['courses'][1])
print(person.keys())
print(person.values())
print(person.items())


 # #### Control flow
# ## Conditional Statement
#entry = input("enter your name")
#print(f"hello {entry}")

# # if
# if codition
#   expression
entry = input("Enter your name: ")
if entry == "Vaia" or entry == "Victoria" or entry == "Victoria Joseph":
        print(f"Hello {entry}")