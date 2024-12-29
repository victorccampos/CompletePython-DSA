

def linear_search(arr: list[int], target: int):
    for index, element in enumerate(arr):
        if element == target:
            return index
    return -1



print(linear_search(arr=[4,12,2,], target=2))

