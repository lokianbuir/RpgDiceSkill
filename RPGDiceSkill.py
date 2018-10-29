from random import randint

countDice = 1 #keeps track of dice rolled
userInput = raw_input("Dice being rolled? ex 3d6 or 1d20: ")
rollBonus = input("Bonus to roll? 0 for none: ")
advantageRoll = raw_input("Advantage? (a) Disadvantage? (d):")
diceTotal = 0 #No dice rolled yet, duh

results = userInput.split("d")
results = [int(i) for i in results]
print results #testing

diceNum = results[0]
diceSides = results[1]

print diceNum
print diceSides

while True:
    diceSides = results[1]
    diceSides = randint(1,diceSides)

    diceTotal = diceTotal + diceSides
    print "Die", countDice, "is:", diceSides #print each die/result
    #print diceSides #testing
    countDice += 1

    if countDice >= diceNum + 1:
        rollBonus = diceTotal + rollBonus
        print "And the total is:", diceTotal
        print "With the bonus:", rollBonus
        break
