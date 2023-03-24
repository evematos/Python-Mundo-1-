num = int(input('insira número de 0 a 9999: '))

print('unidade: {}'.format(num // 1 % 10))
print('dezena: {}'.format(num // 10 % 10))
print('centena: {}'.format(num // 100 % 10))
print('milhar: {}'.format(num // 1000 % 10))

