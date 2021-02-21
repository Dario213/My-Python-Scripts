
numbers = []

prompt = "Enter a range number\n> "
user_range = int(input(prompt))
def while_loop(range):
    i = 0
    while i < range:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

while_loop(user_range)

print("The numbers: ")

for num in numbers:
    print(num)
