def foo(array):
    sum = 0 # O(1)
    product = 0 # O(1)

    for i in array: # O(N)
        sum += i

    for i in array: # O(N)
        product *=i

    print(f'Sum = {sum} and product = {product}')
    # Total time complexity O(2N) = O(N)