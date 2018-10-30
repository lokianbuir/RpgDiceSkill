from random import randint

count = 1  # for tracking dice rolled
userInput = input("How many and what dice are you rolling? (Use standard RPG dice terms: 3d6, 1d12, etc.:")
rollBonus = input("Is there a bonus to the roll, if yes how much? If no, put 0:")
advRoll = input("Is this roll with advantage (a) or disadvantage (d), or neither (n)?")
diceTotal = 0  # No dice have been rolled yet, duh...

results = userInput.split("d")
results = [int(i) for i in results]
# print(results)
# print(rollBonus)

diceNumber = results[0]
diceSides = results[1]


# print(diceNumber)
# print(diceSides)

class StandardRollLoop:
    while True:
        diceSides = results[1]
        diceSides = randint(1, diceSides)

        diceTotal = diceTotal + diceSides
        print("Die", count, "rolled", diceSides)
        count += 1

        if count >= diceNumber + 1:
            rollBonus = diceTotal + int(rollBonus)
            print("Your total rolled is:", diceTotal)
            print("With the bonus:", rollBonus)
            break
