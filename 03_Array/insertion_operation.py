import array

arr = array.array('i', [1, 2, 3, 4])
print(f'Before {arr=}')
# Insert a new item v into the array before position i.
arr.insert(0, 6) # (element, index_to_insert)
print(f'after {arr=}')