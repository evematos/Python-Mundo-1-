s = float(input('insira salário: '))

porcent = (s*15)/100
ns = s + porcent

print('Seu salário sairá de R${} para R${:.2f} com um aumento de 15%'.format(s, ns))