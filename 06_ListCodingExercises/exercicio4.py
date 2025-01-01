"""
Middle function

Write a function called middle that takes a list and returns a new list that
contains all but the first and last elements.
"""

# pythonico
def middle(lst: list) -> list:
    return lst[1:-1]


print(middle([1,2,3,4]))


# Apeser de simples aqui aprendi que a operação de slice é O(N) em tempo e espaço


