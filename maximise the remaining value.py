#!/bin/python3

import math
import os
import random
import re
import sys

#
# Maximise the remaining luck when you are allowed to loose only k
#  important games and loosing the game saves you luck
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#
"""
STDIN       Function
-----       --------
6 3         n = 6, k = 3
        
5 1         contests = [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]
2 1
1 1
8 1
10 0
5 0
"""


def luckBalance(k, contests):
    # Write your code here
    important_contests = []
    sum_of_all_lucks=0
    for i in contests:
        sum_of_all_lucks+=i[0]
        if i[1]  >0 :
            #important
            important_contests.append(i[0]) 
    important_contests.sort()
    print(f"len(important_contests)-k {len(important_contests)-k}")
    print(f"sum_of_all_lucks {sum_of_all_lucks}")
    print(f"Important contests {important_contests}")
    for indx in range(len(important_contests)-k):
        sum_of_all_lucks = sum_of_all_lucks-2*important_contests[indx]
    return sum_of_all_lucks
        
                   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
