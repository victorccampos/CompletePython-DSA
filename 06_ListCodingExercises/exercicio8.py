"""
Pairs
Write a function to find all pairs of an integer array whose sum is equal to a
given number. Do not consider commutative pairs.
"""

def pair_sum(myList, sum):
    # TODO
    vec = []
    for i in range(len(myList)):
        for j in range(i+1, len(myList)):
            if myList[i] + myList[j] == sum:
                vec.append(f'{myList[i]}+{myList[j]}')
    return vec
        
vec_Teste = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
soma = 7

print(
    pair_sum(myList=vec_Teste, sum=soma)
)