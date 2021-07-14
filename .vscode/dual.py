import numpy as np
from random import seed
from random import random


def dual_once(p):
    turn_num=0
    while(1):
        turn_num = turn_num + 1                 # Player 1 fires
        r = random()
        if(r <= p[0]):
            survivor = 0
            break

        turn_num = turn_num + 1                 # Player 2 fires
        r = random()
        if(r <= p[1]):
            survivor = 1
            break 
    return(survivor, turn_num)


p = np.array([4/6, 5/6])
s = np.zeros(2)
total_turns =  0
dual_num = 10000
print("Number of Duals = ", dual_num)

for i in range(0, dual_num):
    (survivor, turn_num) = dual_once(p)
    s[survivor] = s[survivor] + 1
    total_turns = total_turns + turn_num
print(s)
Probability_of_Winning = s/dual_num

print("---Simulation Results---")
print("Probability of A Winning = ", Probability_of_Winning[0])
print("Probability of B Winning = ", Probability_of_Winning[1])
turn_average = total_turns/dual_num
print("Turn Average = ", turn_average)

print("---Theoritical Values---")
print("Theoritical Probability of A Winning = ", 12/17)
print("Theoritical Probability of B Winning = ", 5/17)
    