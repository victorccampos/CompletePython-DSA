def reverse(array):
    """
    reverse an array
    ex: [1,2,3,4,5] -> [5, 4, 3, 2, 1]
    """
    for i in range(0, int(len(array)/2) ): # O(N/2)
        other = len(array) - i - 1 # -------- O(1)
        temp = array[i] # --------------------O(1)
        array[i] =  array[other] # -----------O(1)
        array[other] = temp # ----------------O(1)

    print(array) # O(1)
# Total time complexity : O(N)