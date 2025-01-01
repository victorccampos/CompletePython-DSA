"""
2D Lists

Given 2D list calculate the sum of diagonal elements.
"""

def diagonal_sum(matrix):
    # TODO
    soma = 0 # O(1) em espaco
    for i in range(len(matrix[0])): # O(N_cols ou N_rows)
        soma += matrix[i][i]
        
    return soma