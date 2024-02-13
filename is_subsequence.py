# Author: Kristin Towns
# GitHub username: kristinlashun
# Date: 2/12/2024
# Description: This file contains a recursive function named is_subsequence that checks if the first string
# is a subsequence of the second string. It returns True if it is a subsequence, and False otherwise.

def is_subsequence(s1, s2, index1=0, index2=0):
    # If all characters of s1 have been accounted for, it's a subsequence
    if index1 == len(s1):
        return True
    # If s2 ends before s1, then s1 can't be a subsequence
    if index2 == len(s2):
        return False
    # If characters match, move to the next character in s1
    if s1[index1] == s2[index2]:
        return is_subsequence(s1, s2, index1 + 1, index2 + 1)
    else:
        # Move to the next character in s2 and try again
        return is_subsequence(s1, s2, index1, index2 + 1)
