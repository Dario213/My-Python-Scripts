from sys import argv

script, user_name = argv
prompt = '> '

print(f"Hi {user_name}, I'm the {script} script")
print("I'd like to ask you a few questions. (Be sure to answer good or the World DIES cause AI)")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives_in = input(prompt)

print("Who made your web-camera?")
camera = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.(SMART "choice")
You live in {lives_in}. Don't know the f where that shit is.
And you have a {camera} camera. NICE.
""")
