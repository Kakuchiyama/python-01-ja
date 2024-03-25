import random
import math

hand_type = ("rock", "scissors", "paper")

# ユーザー
input_string = int(input ("Select your hand_type by 0/1/2 (0-rock, 1-scissors, 2=paper) :"))

# コンピューター
# 0 1 2
# print (hand_type[math.floor(random.random() * 3)})
computer_choice = math.floor(random.random() * 3)

if (
    (input_string == 0 and computer_choice == 1) 
    or (input_string == 1 and computer_choice == 2) 
    or (input_string == 2 and computer_choice == 0)
    ):
    print("You win!")
elif input_string == computer_choice:
    print("It is a draw!")
elif (
    (input_string == 0 and computer_choice == 2) 
    or (input_string == 1 and computer_choice == 0) 
    or (input_string == 2 and computer_choice == 1)
    ):
    print("Computer wins")
