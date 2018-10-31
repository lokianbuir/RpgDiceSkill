from random import randint


class RpgRoll:
    count = 1  # for tracking dice rolled
    roll_type = input("What kind of roll are you wanting to make? (Advantage, Disadvantage, Normal)").lower()
    user_input = input("How many and what dice are you rolling? (Use standard RPG dice terms: 3d6, 1d12, etc.:").lower()
    roll_bonus = input("Is there a bonus to the roll, if yes how much? If no, put 0:")
    dice_total = 0  # No dice have been rolled yet, duh...

    def roll_normal(self, count, user_input, roll_bonus, dice_total):
        results = user_input.split("d")
        results = [int(i) for i in results]

        while True:
            dice_number = results[0]
            dice_sides = results[1]
            dice_sides = randint(1, dice_sides)

            dice_total = dice_total + dice_sides
            print("Die", count, "rolled", dice_sides)
            count += 1

            if RpgRoll.count >= dice_number + 1:
                roll_bonus = dice_total + int(roll_bonus)
                print("Your total rolled is:", dice_total)
                print("With the bonus:", roll_bonus)
                break

    if roll_type == "normal":
        roll_normal(count, user_input, roll_bonus, dice_total)

# def roll_normal(self):
#
#     while True:
#         dice_number = RpgRoll.results[0]
#         dice_sides = RpgRoll.results[1]
#         dice_sides = randint(1, dice_sides)
#
#         dice_total = RpgRoll.dice_total + dice_sides
#         print("Die", RpgRoll.count, "rolled", dice_sides)
#         RpgRoll.count += 1
#
#         if RpgRoll.count >= dice_number + 1:
#             roll_bonus = dice_total + int(RpgRoll.roll_bonus)
#             print("Your total rolled is:", dice_total)
#             print("With the bonus:", roll_bonus)
#             break
#
#
# def roll_advantage(self):  # How do I call this from an input???

