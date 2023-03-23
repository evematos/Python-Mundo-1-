p = float(input('insira o preço do produto: '))

porcent = (5*p)/100
np = p - porcent

print('A compra de R${} sairá por R${:.2f} com 5% de desconto'.format(p,np))
