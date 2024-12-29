"""
How to Measure using Big O?
"""

def find_max_number(sample_array: list) -> int | float:
    max_number = sample_array[0] # O(1)
    for index in range(1, len(sample_array)): # O(N)
        if sample_array[index] > max_number: # O(1)
            max_number = sample_array[index] # O(1)
    print(max_number) # O(1)

# Time Complexity --- O(1) + O(N) + O(1) = O(N)

        
