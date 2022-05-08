#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    start = arr[0]
    absdiff = None
    arr.remove(start)
    minabsdiff = None
    while len(arr):
        for v in arr:
            absdiff = abs(start-v)
            if minabsdiff is None:
                minabsdiff = absdiff
            else:
                minabsdiff = min(absdiff, minabsdiff)
                
        if minabsdiff == 0:
            return minabsdiff
        start=arr[0]
        arr.remove(start)
        
    return minabsdiff
        
        
        

if __name__ == '__main__':
    s = input()
    while s!='exit':
        arr = list(map(int, s.rstrip().split()))
        result = minimumAbsoluteDifference(arr)
        print(result)
        s = input()
    