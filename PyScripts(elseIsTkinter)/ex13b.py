from sys import argv

script, car, food, country = argv

print(f"""
This program is called {script} and it's going to ask you some
questions about your favourite things.
""")

car = input("What is your favorite color? ")
food = input("What is your favorite number? ")
country = input("What is your favorite shape? ")

print("Your favorite car is a:", car)
print("Your favorite food is:", food)
print("Your favorite country is:", country)
