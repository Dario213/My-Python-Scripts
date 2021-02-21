formater = "{} {} {} {}"

print(formater.format(1, 2, 3, 4))
print(formater.format("one", "two", "three", "four"))
print(formater.format(True, False, False, True))
print(formater.format(formater, formater, formater, formater))
print(formater.format(
    "Dugo u noć, u zimsku gluhu noć",
    "Moja mati bijelo platno tka.",
    "O mati žalosna! Kaži, što sja",
    "U tvojim očima"
))
