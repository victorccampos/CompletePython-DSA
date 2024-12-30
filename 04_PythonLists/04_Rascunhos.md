<h1 style="text-align: center;">Introdução </h1>

<br><br>

## O que aprendi?
- Podemos usar o operador `in` para saber se um elemento pertence ou não a uma lista.
```python
minha_lista = [1,2,3,4,5]
print(4 in minha_lista )
>>> True
```
- Métodos de lista:


|Complexidade |`extend()`  | `append` | `insert()` |
|-------------|---------------|---------------|---------------|
| Espacial | $\Omicron(n)$ | $\Omicron(1)$ | $\Omicron(n)$ |  


```python
lista1 = [1, 2, 3]
lista2 = [9, 4, 2]
lista1.extend(lista2) # O(N)
print(lista1)
>>> [1, 2, 3, 9, 4, 2]
```
- `pop()` apaga utilizando o index e retorna o objeto apagado
- `remove()`  apaga especificando o objeto

### List and Strings

```python
a = 'spam'
b = list(a)
print(b)
>>> ['s','p','a','m']
```
```python
a = 'spam spam spam'
b = a.split() # defaul delimiter is ' '
print(b)
>>> ['spam', 'spam', 'spam']
```

### List Comprehension  
💡 Funciona para outros tipos __além das listas__  

```python
tupla = (1, 2, 3, 4)
nova_tupla = tuple(x * 2 for x in tupla)
print(nova_tupla)  # Saída: (2, 4, 6, 8)

Conjuntos:
conjunto = {1, 2, 3, 4}
novo_conjunto = {x * 2 for x in conjunto}
print(novo_conjunto)  # Saída: {8, 2, 4, 6}

Dicionários:
dicionario = {'a': 1, 'b': 2, 'c': 3}
novo_dicionario = {chave: valor * 2 for chave, valor in dicionario.items()}
print(novo_dicionario)  # Saída: {'a': 2, 'b': 4, 'c': 6}
```
Esses exemplos mostram como a list comprehension pode ser adaptada para diferentes tipos de estruturas de dados.

