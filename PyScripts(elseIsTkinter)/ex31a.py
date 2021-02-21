print("This game might be complicated. If you want tutorial type Tutorial after this. If not type Continue.")
prompt = "> "
help = input(prompt)

if help == "Tutorial":
    print("""\n\n\nIn this game you follow your choices.
I wount spoil you how. It is obvius.
Errors will occur if you dont type right answer.\n\n""")




print("""You are in search for your brother.
He was last saw half a mile from scary dungeon.
You are now in front of the dungeon.
People think there are witches and some scary ghousts.
In newspaper it said that demon has ripped apart mayor of the town.
What do you do.
\t1. Enter the dungeon.
\t2. Run away.""")
choice_entering = int(input(prompt))


if choice_entering == 1:
    print("""You have entered the dungeon.
Before continue, pick one item from your backpack.
\t1. Grenade
\t2. Sword
\t3. Voodo doll
\t4. AK - 47 (Why do you even have theese stuff! You are weird)""")
    pick = int(input(prompt))

    if pick == 1:
        print("You carried Grenade with you.")
    elif pick == 2:
        print("You carried Sword with you.")
    elif pick == 3:
        print("You carried Voodo doll with you.")
    elif pick == 4:
        print("You carried AK - 47 with you.")
    else:
        print("You don't have that many items in the backpack")


    print("There are two halls in whick you go: #1 or #2")
    hall_choice = int(input(prompt))

    if hall_choice == 1:
        print("""There is a demon evil smiling and running towards you.
    What do you do:
    \t1. Use your item
    \t2. Scream at demon
    \t3. Fight with fists
    \t4. Run away """)
        fight_demon = int(input(prompt))

        if fight_demon == 1 and pick == 3:
            print("""You used your Voodo doll and demon died cause he can't resist the dark magic of Voodo.
        You found your brother and saved him!
        You became the mayor of the town.
        \n\n\n\t\tGAME OVER, YOU WON THIS SECRET GAME!!\n\n""")
        elif fight_demon == 1 and pick != 3:
            print("""You used a weapon against a dark soul.
        Demon was not affected at all by your weapon.
        He just dashed through your fightings skilles and burned you with sulfur and fire.
        He ripped your soul and body apart with black magic.
        \n\n\n\t\tGAME LOST! I GUES YOU ARE NOT SMART.\n\n""")
        elif fight_demon == 2:
            print("""Demon just started smiling and laughing.
        He died of too much laughing.
        You found your brother and saved him!
        You became the mayor of the town.
        \n\n\n\t\tGAME WON! WOW THAT WAS CLEVER.\n\n""")
        elif fight_demon == 3:
            print("""You are stupid if you want kick him.
        He just dashed through your fightings skilles and burned you with sulfur and fire.
        He ripped your soul and body apart with black magic.
        \n\n\n\t\tGAME LOST! I GUES YOU ARE NOT SMART.\n\n""")
        elif fight_demon == 4:
            print("""You ran away like a coward.
        Demon killed your brother.
        He came to your house at night and killed you.
        \n\n\n\t\tGAME LOST! I GUES YOU ARE A COWARD.\n\n""")
        else:
            print("You did nothing and demon killed you.")
            print("\n\n\n\t\tGAME LOST! I GUES YOU ARE A COWARD.\n\n")

    elif hall_choice == 2:
        print("""You found your brother and mayor from the
        newspaper playing togheter.
    What you found is called heaven.
    You were awarded with nobel prize for discovering afterlife.
    \n\n\n\t\tGAME WON! LUCKY CHOICE!""")
    else:
        print("A big rock fell on you.")
        print("\n\n\n\t\tGAME LOST! I GUES YOU ARE A COWARD.\n\n")

elif choice_entering == 2:
    print("Your brother became new demon.")
    print("He found you and haunted you.")
    print("You died out of sadness.")
    print("\n\n\n\t\tGAME LOST! LIFE LESSON\n\n")

else:
    print("Your brother became new demon.")
    print("He found you and haunted you.")
    print("You died out of sadness.")
    print("\n\n\n\t\tGAME LOST! LIFE LESSON\n\n")
