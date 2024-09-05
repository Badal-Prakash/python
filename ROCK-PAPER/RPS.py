import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


print("")
playersChoice = input(
    "Enter... \n1 for Rock\n2 For Paper\n3 For Scissors:\n\n")

player = int(playersChoice)
if player < 1 or player > 3:
    sys.exit("You must enter 1,2, or 3.")

computerChoice = random.choice('123')
computer = int(computerChoice)


print("")
print("you choose "+str(RPS(player)).replace("RPS.", " ") + ".")
print("python choose "+str(RPS(computer)).replace("RPS.", " ") + ".")

if player == 1 and computer == 3:
    print("🎉🎉You Win!🎉🎉")
elif player == 2 and computer == 1:
    print("🎉🎉You Win!🎉🎉")
elif player == 3 and computer == 2:
    print("🎉🎉You Win!🎉🎉")
elif player == computer:
    print("Tie Game")
else:
    print("Python Win!")
