nome = str(input('insira seu nome completo: ')).strip()

res = 'SILVA' in nome.upper()
print('este nome contem "silva"? {}'.format(res))