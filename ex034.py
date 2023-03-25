sal = float(input('insira seu salário: '))

if sal > 1250:
    aumento = (sal * 10) / 100
    print('seu novo salário é R${} com 10% de aumento'.format(sal + aumento))
else:
    aumento = (sal * 15) / 100
    print('seu novo salário é R${} com 15% de aumento'.format(sal + aumento))