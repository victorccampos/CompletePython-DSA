<h1 style="text-align: center;">O que aprendi ? </h1>

1. Na questão `missing_number` minha implementação foi:

```python
def missing_number(arr: list[int], n: int) -> int | list[int]:
    completed_arr = [i for i in range(1, n+1)] # size n
    
    for i in range(1, n+1): # ----------> O(N)
        if i not in arr[:n+1]: # ----------> O(N)
            return i
        else:
            continue
    

missing_number([1,2,3,4,6] ,6)
```
Apesar de passar nos testes, essa implementação tem complexidade temporal $\Omicron(n^2)$ e espacial $\Omicron(1)$. A alternativa, também no __gabarito__ da questão, usa a soma dos `n` primeiros números.

```python
def missing_number(arr, n):
    # Calculate the sum of first n natural numbers
    total = n * (n + 1) // 2
    
    # Calculate the sum of numbers in the array
    sum_arr = sum(arr)
    
    # Find the missing number by subtracting sum_arr from total
    missing = total - sum_arr
    
    return missing
 
# Example
print(missing_number([1, 2, 3, 4, 6], 6))  # Output: 5
```