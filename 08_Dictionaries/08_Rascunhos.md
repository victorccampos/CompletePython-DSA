<h1 style="text-align: center;"> Dicionários </h1>  

> É uma coleção não-ordenada, mutável e indexada  

```python
# Criação de um dicionário

empty_dict = {}                 # Pythonic
empty_dict2 = dict()            # menos Pythonic - dict() constructor
grades = {"Joel": 80, "Tim":95} # dicionário literal - O(N) O(N)

list_of_tuples = dict(
    [('key1', 'value1'),('key2', 'value2')]
    ) 
```

Uma _tabela hash_ é uma forma de fazer pesquisas de chave-valor. 
Você armazena os valores em um array e, em seguida, usa uma função hash para encontrar o índice da célula do array que corresponde ao seu par de chave-valor. A _colisão_ ocorre quando a hash function dá um index já ocupado. Esse novo elemento é tratado como uma _linked list_ nesse index.


### Insert/Update element in dictionary  

Pra inserir, por exemplo com a atribuição `meu_dic['key'] = 'value'` é O(1) no tempo e O(1) amortizado no espaço.  

> $\Omicron(1)$ amortizado se dá quando não é o caso da estrutura de dados adicionada puder aumentar o diminuir de tamanho como uma lista.

### Tranverse a dict  

```python

def tranverse_a_dict(dic):
    for key in dic:          # O(N)
        print(key, dic[key]) # O(1)

# Time complexity: O(N)
# Space complexity: O(1)
```

### Search for an element in Dictionary  

```python
def linear_search_in_dict(dic: dict, value):
    for key in dic:               # O(N)
        if dic[key] == value:     # O(1)
            return key, value     # O(1)
    return "Value dos not exists" # O(1)
# Time complexity: O(N)
# Space complexity: O(1)
```

### Delete/Remove an element from a Dictionary  
- `del` keyword:  
```python
del my_dict['age'] 
```  
A complexidade de tempo para excluir um elemento usando a instrução `del` é O(1) porque envolve a operação da tabela
hash. A complexidade de espaço também é O(1) porque não cria nenhuma estrutura de dados adicional para implementar essa operação.

- `pop()`  
```python
my_dict = {"name": "joão", "age": 22}

removed_element = my_dict.pop('age') # O(1)
print(removed_element)
>>> 22
print(my_dict)
>>> {"name": "joão"}  
# Time complexity: O(1)
# Space complexity: O(1)
```
> 💡 None como default value evita erros com método `pop() -> value`  
> 💡 Tem a forma mais pythonic com método `popitem() -> key, value`

- `dictionary.clear() -> None` limpa todo o dicionário: T: O(N), S: O(1).  

### Dictionay methods  

- `dictonary.copy()` : retorna uma cópia superficial do original (cria uma nova).  

- `dictionary.fromkeys()`
```python
dic = {}.fromkeys(sequence=[1,2,3], value=0)
>>> {1:0, 2:0, 3:0}
```  
```python
# methods
dic.copy() -> dict` # cria uma shallow copy do original 
dic.get() 
dic.items() -> list[(keys,values)]
dic.keys() -> list[(keys,values)]  
dic.values() -> list[(values)]  
dic.setdefault(key, defaultvalue) -> key | defaultavalue | None
dic.update() -> dict  
```  

### Dictionary Operations / Builtin Functions  
> 💡 O operandor `in` do Python trabalha apenas com as __chaves__ dos dicionários e não com os valores. 

```python
dic = {3: "three", 4: "four}
3 in dic 
>>> True
"three" in dic
>>> False
"three" in dic.values()  # ["three", "four"]
>>> True
```
> A função `len()` conta apenas os pares do dicionário.

A função `all()` e `any()` do Python:
```python
# All keys are true -> True
dic1 = {1: "one", 2: "two"}
all(dic1) >>> True
any(dic1) >>> True
# All keys are false -> False
dic2 = {0: "zero", False:"False"}       
all(dic2) >>> False
any(dic2) >> False

# One key is true -> False
dic3 = {1: "zero", False:"False"}       
all(dic3) >>> False
any(dic3) >>> True
```

> O método `sorted()` do Python ordena as chaves do dicionário.  

### Time and Space Complexity  

<table>
  <thead style="background-color: lightgray;">
    <tr>
      <th>Operantion</th>
      <th>Time Complexity</th>
      <th>Space Complexity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Creating a dict</td>
      <td>O(len(dict))</td>
      <td>O(N)</td>
    </tr>
    <tr>
      <td>Insert a value</td>
      <td>O(1)/O(N)</td>
      <td>O(1)</td>
    </tr>
    <tr>
      <td>Traversing a dict</td>
      <td>O(N)</td>
      <td>O(1)</td>
    </tr>
    <tr>
      <td>Search a given value</td>
      <td>O(N)</td>
      <td>O(1)</td>
    </tr>
    <tr>
      <td>Acessing a given cell</td>
      <td>O(1)</td>
      <td>O(1)</td>
    </tr>
    <tr>
      <td>Deleting a given value</td>
      <td>O(1)</td>
      <td>O(1)</td>
    </tr>
    
  </tbody>
</table>  

> "Search for a value" : usando o operador `in` é O(1).  

### Dictionary Comprehension  

```python
                                      # iterable  
new_dict = {new_key:new_value for item in list}
new_dict = {new_key:new_value for (key,value) in dic.items()}
new_dict = {new_key:new_value for (key,value) in dic.items() if condition}
```