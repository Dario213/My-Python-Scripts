my_name = 'Dario Adamović'
my_age = 15 #not a lie
my_height = 175 #centimeters
my_weight = 81 #kg
my_eyes = 'Light blue'
my_teeth = 'White'
my_hair = 'Light brown'
weight_in_lbs = my_weight * 2.20462262
centimeters_in_inches = my_height / 2.54

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} centimeters tall, or {centimeters_in_inches} inches tall.")
print(f"He's {my_weight} kilograms heavy, or {weight_in_lbs} pounds heavy.")
print("Actually that's not too heavy.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

#This line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height} and {my_weight} I get {total}.")
