a: str = 'spam-spam-spam'

delimiter: str = '-'
b = a.split(sep=delimiter)

print('Split of a:',  b)

reconstructed = delimiter.join(b)

print(f'{reconstructed=}')
