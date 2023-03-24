km = float(input('insira a velocidade do carro: '))

if km > 80:
    multa = (km-80) * 7
    print('você está ACIMA DO LIMITE e irá receber uma multa de R${}'.format(multa))
else:
    print('Tenha um bom dia! Dirija com segurança!')