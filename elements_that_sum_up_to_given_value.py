#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'whatFlavors' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY cost
#  2. INTEGER money
#
def whatFlavors(cost, money):
    cost_frequency = Counter(cost)
    for i in range(len(cost)):
        if cost[i] >= money:
            pass
        cost_Sunny = cost[i]
        cost_Johnny = money - cost_Sunny
        if cost_Johnny != cost_Sunny:
            if cost_frequency[cost_Johnny]:
                index_Johnny_cost = cost.index(cost_Johnny)
                # print(f"Johnny's cost index matches current index {i}")
                print(f"{min(i, index_Johnny_cost)+1} {max(i, index_Johnny_cost)+1}")
                return
           
        else:
            if cost_frequency[cost[i]]>1:
                try:
                    del cost[i]
                    index_Johnny_cost = cost.index(cost_Johnny)+1
                    print(f"{min(i, index_Johnny_cost)+1} {max(i, index_Johnny_cost)+1}")
                    return
                except:
                    pass               
            
def whatFlavorsnaive(cost, money):
    cost_range = range(len(cost))
    for i in cost_range:
        if cost[i]>=money:
            continue
        #print(f"i={i}")
        for j in cost_range:
            if cost[j] >= money:
                continue
            # print(f"i={i}, amount={cost[i]},  j={j}, amount_={cost[j]}")
            if i!=j and cost[i]+ cost[j]== money:
                print(f"{min(i,j)+1} {max(i,j)+1}")
                return
            

            

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        money = int(input().strip())

        n = int(input().strip())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
