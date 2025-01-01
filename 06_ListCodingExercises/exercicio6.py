"""
Best Score
Given a list, write a function to get first, second best scores from the list.

List may contain duplicates

myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
first_second(myList) # 90 87
"""

def first_second(lst: list[int]):
    max1 = 0
    max2 = 0

    for index, number in enumerate(lst):
        if number > max1:
            max2 = max1 
            max1 = number
        # Se o numero atual for maior que max2 mas n max1
        elif number > max2:
            max2 = number

    return max1, max2

MAX1, MAX2 = first_second(lst=[84,85,86,87,85,90,85,83,23,45,84,1,2,0])

print(MAX1, MAX2)
