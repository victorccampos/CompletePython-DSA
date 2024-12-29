"""
Aula 27 - Create an array

module array: This module defines an object type which can efficiently
represent an array of basic values: characters, integers, floating-point
numbers. Arrays are sequence types and behave very much like lists, except that
the type of objects stored in them is constrained

"""

import array
import numpy as np

# built-in
empty_arr: array = array.array('i') # empty array of type integer O(1)
my_arr: array = array.array('i', [1,2,3,4]) # array of type integer O(N)
array3 = array.array('d', [1.5, 2.2, 3.1]) # array of type float O(N)

# numpy
numpy_array = np.array([], dtype=int) # empty array of type integer O(1)
numpy_array2 = np.array([1,2,3,4]) # array of type integer O(N)

 
print('EMPTY ARRAYS:')
print(f'\t{empty_arr=}')
print(f'\t{numpy_array=}')

print('NON-EMPTY ARRAYS')
print(f'\t {my_arr=}')
print(f'\t {numpy_array2=}')
print(f'\t {array3=}')
