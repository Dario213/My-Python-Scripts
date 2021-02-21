def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def substract(a, b):
    print(f"SUBSTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
     print(f"DIVIDING {a} / {b}")
     return a / b

print("Let's do some math with just functions!")

age = add(10, 5)
height = substract(200, 25)
weight = multiply(40, 2)
iq = divide(78, 3)

print(f"Age: {age}, Height: {height}, weight: {weight}, IQ: {iq}")

# A puzzle for extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age, substract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do this by hand(NO!)")
