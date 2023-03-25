km = float(input('insira distância da viagem em km: '))

if km <= 200:
    valor = km * 0.50
else:
    valor = km * 0.45

print('o valor da sua viagem de {}km será R${:.2f}'.format(km,valor))