def print_pairs(array):
    for i in array: # O(N)
        for j in array: # O(N)
            print(f'{i}, {j}') # O(1)
# Total time complexity = O(N) * O(N) = O(N^2)