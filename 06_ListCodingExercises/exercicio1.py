"""
Missing Number
Write a function to find the missing number in a given integer array of 1 to 100. 
The function takes to parameter the array and the number of elements that needs 
to be in array.For example if we want to find missing number from 1 to 6 the 
second parameter will be 6.

missing_number([1,2,3,4,6], 6) --> return 5
"""

def missing_number(arr: list[int], n: int) -> int | list[int]:
    completed_arr = [i for i in range(1, n+1)] # size n
    
    for i in range(1, n+1):
        if i not in arr[:n+1]:
            # missed.append(i)
            return i
        else:
            continue
    

missing_number([1,2,3,4,6] ,6)



# Teste completo com sucesso :)