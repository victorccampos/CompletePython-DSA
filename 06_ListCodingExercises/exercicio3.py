"""
Max Product of Two Integers

Find the maximum product of two integers in an array where all elements are
positive.

arr = [1, 7, 3, 4, 9, 5] 
Output: 63 (9*7)
"""

# O(n²)
def max_product(arr):
    products = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
                products.append(arr[i]*arr[j])
                
    return max(products)
