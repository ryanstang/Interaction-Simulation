#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMaxStreaks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY toss as parameter.
#

def getMaxStreaks(toss):
    result = [0,0]
    for num in range(len(toss)-1):
        repeat = 0
        if toss[num] == "Heads":
            for t in toss[num:]:
                if t == "Heads": 
                    repeat += 1
            if repeat > result[0]:
                result[0] = repeat
        else:
            for t in toss[num:]:
                if t == "Tails": 
                    repeat += 1
            if repeat > result[1]:
                result[1] = repeat
    return result
        

if __name__ == '__main__':

    toss_count = int(input().strip())

    toss = []

    for _ in range(toss_count):
        toss_item = input()
        toss.append(toss_item)

    ans = getMaxStreaks(toss)

    fptr.write(' '.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
