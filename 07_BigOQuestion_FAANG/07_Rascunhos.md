03. `PrintUnorderedLists`  

Aprendi dois métodos para estudar a complexidade:
- _Counting iterations_
- _Average work_  

05. `Print Unorderes Lists 2 Arrays 100 000 units`

Meu raciocínio foi que:

```python
def print_unordered_pairs(arrayA, arrayB):
    for i in range(len(arrayA)): # O(a)
        for j in range(len(arrayB)): # O(b)
            for k in range(0, 100_000):
                if arrayA[i] < arrayB[j]: # O(1)
                    print(f'{arrayA[i]}, {arrayB[j]}')

# O pior caso possível é se todos elementos de A forem menor que todos de B.
# O(a) * O(b) * 100_000? = 100_000*a*b = O(a*b)
```
Mas, deveria colocar no loop em $k$ que a complexidade é na verdade $O(1)$. Não sei se
essas duas abordagens são equiavalentes e o argumento, mas a resposta final foi a mesma.  

07. `WhichAreEquivalent`  

Fiquei numa pequena dúvida na expressão $O(N+M)$, mas ela é apenas $O(N+M)$, não tem nenhuma relação entre $N$ e $M$ e não podemos pensar que $N+M$ = "algum N".