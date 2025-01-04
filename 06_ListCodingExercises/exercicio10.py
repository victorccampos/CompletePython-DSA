"""
Permutation
"""

def permutation(list1, list2):
    if len(list1) != len(list2):
        return False

    # Sort the list and compare
    list1.sort()  # O(nlog(n))
    list2.sort()


    return list1 == list2


######## IMPLEMENTACAO O(N) ########

from collections import Counter

def permutation(list1, list2):
    if len(list1) != len(list2):
        return False

    return Counter(list1) == Counter(list2)