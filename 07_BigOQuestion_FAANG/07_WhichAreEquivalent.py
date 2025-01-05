"""
Which of the expressions are equivalent to O(N) and why?

1. O(N+P) where P < N/2
2. O(2N)
3. O(N + logN)
4. O(N + NlogN)
5. O(N+M) 
"""

"""
1 - P simplifies to N # O(N)
2. The number 2 is just a constant factor # O(N)
3. Is equal to O(N) because log(N) is just a constant # O(N)
4. diff -> NlogN is dominant
5. (In doubt, i guess is equivalent cuz N+M could be thought as some arbitrary N)

errata: 5. is O(N+M) there is no conection between M and N
"""