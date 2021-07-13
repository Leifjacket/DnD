from random import randrange

# idea from this post: https://rpg.stackexchange.com/a/96753

while True:
    try:
        #first we need user input in this file
        saveDC = int(input("Enter Save DC:"))
        abiMod = int(input("Enter Ability Modifier:"))
        enemies = 0
        while True:
            try:
                enemies = int(input("Enter Number of Enemies (between including 5 and 40):"))
                if enemies < 5 or enemies > 40:
                    raise ValueError 
                break
            except ValueError:
                if enemies < 5:
                    print("Everything under 5 you can roll yourself :P")
                else:
                    print("That's too many monsters for me :(")

        expecSuccSaves = 0
        pSucc = 0

        if (abiMod + 2) > saveDC:
            pSucc = 1
        elif (1 - (saveDC - (abiMod + 1)) * 0.05) >= 0:
            pSucc = 1 - (saveDC - (abiMod + 1)) * 0.05
        else:
            pSucc = 0
        print()
        expecSuccSaves = round(pSucc*enemies)
        print("Expected Number of Successful Saves: " + str(expecSuccSaves))

        succSaves = 0

        r_1d4_1 = randrange(1,5)
        r_1d4_2 = randrange(1,5)

        r_1d6_1 = randrange(1,7)
        r_1d6_2 = randrange(1,7)

        if enemies<=20:
            succSaves = expecSuccSaves + r_1d4_1 - r_1d4_2
        else:
            succSaves = expecSuccSaves + r_1d6_1 - r_1d6_2
            
        if succSaves < 0:
            succSaves = 0

        print("Successful Saves: " + str(succSaves) + " (if you need I rolled some dice and this is the number of Successful saves.)")
        print()    
        goAgain = str(input("Another round? (y/n): "))
        if goAgain == "y":
            raise ValueError
        else:
            print("see ya")
            break
    except ValueError:
        print()