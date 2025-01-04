"""
Duplicate Number

Write a function to remove the duplicate numbers on given integer array/list.
"""

def remove_duplicates(arr):
    # TODO
    arr_copy: list[int] = []
    for number in arr:
        if number not in arr_copy:
            arr_copy.append(number)      
    return arr_copy
                
resposta = remove_duplicates(arr=[1,1,2,2,3,4,5])
print(f'{resposta=}')