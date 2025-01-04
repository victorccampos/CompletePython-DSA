"""
Contains Duplicate
Given an integer array nums, return true if any value appears at least twice
in the array, and return false if every element is distinct.        
"""


def contains_duplicate(nums):
    # TODO
    uniques = set(nums)
    for number in nums:
        if len(nums) == len(uniques):
            return False
        else:
            return True