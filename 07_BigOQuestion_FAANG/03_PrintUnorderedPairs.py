def print_unordered_pairs(array):
    for i in range(0, len(array)): # O(N)
        for j in range(i+i, len(array)): # O(N-1)
            print(array[i] + ",", array[j]) # O(1)


### 1. Couting iterations
"""
inner loop:
1st -> n-1
2nd -> n-2
...
    1

Sum :: (n-1) + (n-2) + ...
= 1 + 2 + ... + (n-3) + (n-2) + (n-1)

sum of firts n number -> n (n-1) / 2 -> O(N²)
"""

### 2. Average Work
"""
Outer loop - N times
inner loop?
Suppose inner loop runs 10 Times;

1st - 10
2nd - 9
...
1

which ~ averages to 5 = 10 / 2
for N numbers the averages can be N/2
N * N/2 ----> O(N²)
"""