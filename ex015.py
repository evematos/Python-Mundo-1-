km = float(input('insira a quantidade de km rodados: '))
d = int(input('insira a quantidade de dias de aluguel: '))

valor = (d * 60) + (km * 0.15)

print('O valor a pagar pelo aluguel é de R${:.2f}'.format(valor))