from random import randint


count = 1  # for tracking dice rolled
roll_type = input("What kind of roll are you wanting to make? (Advantage, Disadvantage, Normal)").lower()
roll_bonus = input("Is there a bonus to the roll, if yes how much? If no, put 0:")
dice_total = 0  # No dice have been rolled yet, duh...


def roll_normal(count, roll_bonus, dice_total):
    user_input = input("How many and what dice are you rolling? (Use standard RPG dice terms: 3d6, 1d12, etc.:").lower()
    results = user_input.split("d")
    results = [int(i) for i in results]

    while True:
        dice_number = results[0]
        dice_sides = results[1]
        dice_sides = randint(1, dice_sides)

        dice_total = dice_total + dice_sides
        print("Die", count, "rolled", dice_sides)
        count += 1

        if count >= dice_number + 1:
            roll_bonus = dice_total + int(roll_bonus)
            print("Your total rolled is:", dice_total)
            print("With the bonus:", roll_bonus)
            break


def roll_advantage(count, roll_bonus):
    rolled_results = []

    while True:
        dice_sides = 20
        dice_sides = randint(1, dice_sides)
        rolled_results.append(dice_sides)
        print("Die", count, "rolled", dice_sides)
        count += 1

        if count > 2:
            print(rolled_results)
            best_roll = max(rolled_results)
            total_result = int(roll_bonus) + int(best_roll)
            print("Your highest roll of", best_roll, "with your bonus is:", total_result)
            break


def roll_disadvantage(count, roll_bonus):
    rolled_results = []

    while True:
        dice_sides = 20
        dice_sides = randint(1, dice_sides)
        rolled_results.append(dice_sides)
        print("Die", count, "rolled", dice_sides)
        count += 1

        if count > 2:
            print(rolled_results)
            worst_roll = min(rolled_results)
            total_result = int(roll_bonus) + int(worst_roll)
            print("Your lowest roll of", worst_roll, "with your bonus is:", total_result)
            break


if roll_type == "normal":
    roll_normal(count, roll_bonus, dice_total)
elif roll_type == "advantage":
    roll_advantage(count, roll_bonus)
elif roll_type == "disadvantage":
    roll_disadvantage(count, roll_bonus)

