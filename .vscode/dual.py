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

    