"""
List Comprehension 
"""

sentenca: str = 'Hoje e dia 30 de dezembro de 2024'

def is_consoante(letra: str) -> bool:
    vogais = 'aeiou'
    return letra.isalpha() and letra.lower()  not in vogais


consoantes_frase = [letra for letra in sentenca if is_consoante(letra=letra)]
print(consoantes_frase) # ['H', 'j', 'd', 'd', 'd', 'z', 'm', 'b', 'r', 'd']