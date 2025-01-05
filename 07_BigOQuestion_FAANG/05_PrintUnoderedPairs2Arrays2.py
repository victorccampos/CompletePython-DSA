def print_unordered_pairs(arrayA, arrayB):
    for i in range(len(arrayA)): # O(a)
        for j in range(len(arrayB)): # O(b)
            for k in range(0, 100_000):
                if arrayA[i] < arrayB[j]: # O(1)
                    print(f'{arrayA[i]}, {arrayB[j]}')

# O pior caso possível é se todos elementos de A forem menor que todos de B.
# O(a) * O(b) * 100_000? = 100_000*a*b = O(a*b)