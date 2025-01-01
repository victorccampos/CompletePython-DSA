"""
Write a program to find all pairs of integers whose sum is equal to
a given number

[2, 7, 11, 15] , target 9
Output: [0,1]

Valid questions:
- Does array contain only positive or negative numbers?
- What if the same pair repeats twice, should we print it every time?
- If the simetric of the pair is acceptable e.g. can we print both?
- Do we need to print only distinct pairs? (3, 3) is valid?
- How big is the array?
"""

# (2,2) or (3,3) not valid pairs

def two_sum(numbers: list, target: int) -> None:
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            # simetria
            if numbers[i] == numbers[j]:
                continue
            elif numbers[i] + numbers[j] == target:
                print(i, j)


arr = [i for i in range(10)]                
print(arr)
twosum(numbers=arr, target=5)



    

