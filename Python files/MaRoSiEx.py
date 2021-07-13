from random import randrange

while True:
    try:
        #first we need user input in this file
        saveDC = int(input("Enter Save DC:"))
        abiMod = int(input("Enter Ability Modifier:"))
        enemies = int(input("Enter Number of Enemies:"))
        succSaves = 0
        for enemy in range(enemies):
            r_1d20 = randrange(1,21)
            if r_1d20 + abiMod >= saveDC:
                succSaves = succSaves + 1

        print("Successful Saves: " + str(succSaves))
        print()    
        goAgain = str(input("Another round? (y/n): "))
        if goAgain == "y":
            raise ValueError
        else:
            print("Understandable, have a nice day")
            break
    except ValueError:
        print()