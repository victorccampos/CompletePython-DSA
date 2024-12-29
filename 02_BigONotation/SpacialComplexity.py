"""
Space Complexity
"""

def sum(n: int) -> int:
    """
    Space Complexity O(N)
    """
    if n <= 0:
        return 0
    return n + (n-1)

def pair_sum(a: int, b: int) -> int:
    return a + b

def pair_sum_sequence(n: int) -> int:
    """
    Space Complexity O(1)
    """
    total: int = 0
    for i in range(n):
        total = total + pair_sum(i, i+1)
    return total


pair_sum_sequence(4)