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
2. `Two Sum`

No problema de Two Sum não consegui implementar nem o de força bruta. Faltou eu utilizar um índice auxiliar `j` que seria o sucessor do índice `i`. A solução da aula foi:

```python 
def two_sum(numbers: list, target: int) -> None:
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            # simetria
            if numbers[i] == numbers[j]:
                continue
            elif numbers[i] + numbers[j] == target:
                print(i, j)


arr = [i for i in range(10)]                
print(arr)
twosum(numbers=arr, target=5)
```

Existe outra solução mais otimizada que usa uma outra estrutura de dados que ainda não estudei (hashmap ?).

```python
def two_sum(nums, target):
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in seen:
            return [seen[complement], i]
        
        seen[num] = i
 
nums = [2, 7, 11, 15]
target = 9
indices = two_sum(nums, target)
print(f"Indices of the two numbers are: {indices}")
```

A complexidade de tempo geral desta solução é O(n), onde n é o número de elementos na lista de entrada. Isso ocorre porque iteramos pela lista uma vez, e as operações dentro do loop (adição e pesquisa de dicionário) têm uma complexidade de tempo média de O(1).

3. `Max Product of Two Integers` 

Minha implementação foi na força bruta, O(N²) temporal e espacial. Uma forma mais otimizada e intuitiva é selecionar os dois maiores números do array e retornar a multiplicação destes.

```python
def max_product(arr):
    # Initialize two variables to store the two largest numbers
    max1, max2 = 0, 0  # O(1), constant time initialization
 
    # Iterate through the array
    for num in arr:  # O(n), where n is the length of the array
        # If the current number is greater than max1, update max1 and max2
        if num > max1:  # O(1), constant time comparison
            max2 = max1  # O(1), constant time assignment
            max1 = num  # O(1), constant time assignment
        # If the current number is greater than max2 but not max1, update max2
        elif num > max2:  # O(1), constant time comparison
            max2 = num  # O(1), constant time assignment
 
    # Return the product of the two largest numbers
    return max1 * max2  # O(1), constant time multiplication
 
arr = [1, 7, 3, 4, 9, 5]
print(max_product(arr))  # Output: 63 (9*7)
```

Se eu entender melhor a lógica das atribuições de valores, vou ser capaz de fazer códigos mais otimizados.  

4. `Middle Function`

Apesar de ser um exercício bem simples, me ensinou que a operação de slice é: 
- O(N) no tempo pois o _slice_ percorre $n-2$ elementos
- O(N) no espaço pois o _slice_ cria uma __nova__ lista que tem $n-2$ elementos   


5. `Soma da diagonal de matriz 2D`  

6. `Best Score`  
Essa questão foi interessante porque utilizou de novo a ideia da __questão 3__. Nela
eu debuguei o código. As partes mais difíceis de entender foram:

`max2 = max1`: Se o elemento atual é maior que max1, atualiza max2 ao valor atual de max1.

`max1 = num`: Atribui ao max1 o valor do elemento atual, já que por ora, esse é o maior.



`elif num > max2 and num != max1: max2 = num` :  
Se o elemento atual é maior que max2 mas diferente de max1, atualiza max2. Atribui a max2 o valor atual já que esse é o segundo maior até o momento.







