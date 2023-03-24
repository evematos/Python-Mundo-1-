nome = str(input('insira seu nome completo: ')).strip()

n = nome.split()

print('primeiro nome: {}'.format(n[0]))
print('último nome: {}'.format(n[len(n)-1]))
