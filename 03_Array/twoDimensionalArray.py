import numpy as np

# Matriz 4x4
two_dim_array = np.array([[11, 15, 10, 6],
                          [10, 14 , 11, 5],
                          [12, 17, 12, 8],
                          [15, 18, 14, 9],])

# Insert values along the given axis before the given indices.
# axis = 1 : coluna, axis = 0 : linha

INDEX_TO_INSERT: int = 0
novo_array = np.insert(two_dim_array, INDEX_TO_INSERT, [[1, 2, 3, 4]], axis=0)
print(novo_array)


# Append 
novo_array2 = np.append(two_dim_array, [[1, 2, 3, 4]], axis=0)
print('\n', novo_array2)