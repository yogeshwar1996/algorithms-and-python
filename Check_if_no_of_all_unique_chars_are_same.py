#!/bin/python3
"""
Sherlock considers a string to be valid if all characters of the string appear
the same number of times. It is also valid if he can remove just one character from the
string, and the remaining characters will occur the same number of times.
Given a string , determine if it is valid. If so, return YES, otherwise return NO.
Example
a - 'YES'
aa - 'YES'
aaa - 'YES'
aaae - 'YES'
abbcc - 'YES'
aaabbcc - 'YES'
aaaabbcc - 'NO'
aabbcd- 'NO'
aabbcceeee - 'NO'
aabbccdddeeefff = 'NO'
abbccc - 'NO'
abbbbcccc - 'NO'
"""
import math
import os
import random
import re
import sys
import collections

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    frequency_of_characters_in_string = dict(collections.Counter(s))
    print(f"frequency_of_characters_in_string: {frequency_of_characters_in_string}")
    list_of_unique_frequencies = list(set(frequency_of_characters_in_string.values()))
    freq_to_list_of_characters = {}
    for k,v in frequency_of_characters_in_string.items():
        if v not in freq_to_list_of_characters:
            freq_to_list_of_characters[v] = []
        freq_to_list_of_characters[v].append(k)
    print(f"freq_to_list_of_characters: {freq_to_list_of_characters}")

    print(f"list_of_unique_frequencies: {list_of_unique_frequencies}")
    length_of_list_of_unique_frequencies = len(list_of_unique_frequencies)
    print(f"length_of_list_of_unique_frequencies: {length_of_list_of_unique_frequencies}")
    if length_of_list_of_unique_frequencies == 1:
        return 'YES' 
    elif length_of_list_of_unique_frequencies == 2:
        no_of_characters_with_freq_f1 = len(freq_to_list_of_characters[list_of_unique_frequencies[0]])
        no_of_characters_with_freq_f2 = len(freq_to_list_of_characters[list_of_unique_frequencies[1]])
        is_there_most_common_frequency = False if no_of_characters_with_freq_f1 == no_of_characters_with_freq_f2 else True
        print(f"is_there_most_common_frequency: {is_there_most_common_frequency}")
        if is_there_most_common_frequency:
            """
            Example  aabbc, aabbccc, aabbcd

            """
            if len(freq_to_list_of_characters[list_of_unique_frequencies[0]])> len(freq_to_list_of_characters[list_of_unique_frequencies[1]]):
                 most_common_frequency = list_of_unique_frequencies[0]
                 other_frequency = list_of_unique_frequencies[1]
                 difference_of_most_common_frequency_and_other_frequency = abs(most_common_frequency- list_of_unique_frequencies[1])
            else:
                most_common_frequency = list_of_unique_frequencies[1]
                difference_of_most_common_frequency_and_other_frequency = abs(most_common_frequency- list_of_unique_frequencies[0])
                other_frequency = list_of_unique_frequencies[0]
            print(f"most_common_frequency: {most_common_frequency}")
            print(f"difference_of_most_common_frequency_and_other_frequency: {difference_of_most_common_frequency_and_other_frequency}")
            print(f"other_frequency: {other_frequency}")
            highest_frequency = max(list_of_unique_frequencies)
            if difference_of_most_common_frequency_and_other_frequency > 1:

                if other_frequency == 1 and len(freq_to_list_of_characters[other_frequency])==1:
                    """Example - abbbbcccc"""
                    return 'YES'
                else:
                    """Example - abceee, aaabbbc"""
                    return 'NO'
            else:
                no_of_characters_in_other_frequency = len(freq_to_list_of_characters[other_frequency])
                print(f"no_of_characters_in_other_frequency: {no_of_characters_in_other_frequency}")
                if no_of_characters_in_other_frequency >1:
                    """example aabbccddeefghi"""
                    return 'NO'
                else:
                    return 'YES'

        else:
            if no_of_characters_with_freq_f1 == no_of_characters_with_freq_f2 == 1:
                """Example aaae """
                return 'YES'
            else:
                """Example aabbcd """
                return 'NO'            
    else:
        return 'NO' 

if __name__ == '__main__':
    
    s = input()
    while s!='exit':
        result = isValid(s)
        print(f"Result: {result}")
        s = input()
            