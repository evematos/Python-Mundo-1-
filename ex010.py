r = float(input('insira valor em reais: '))

print('Com R${} reais você pode comprar US${:.2f} ou €{:.2f}'. format(r, (r / 5.28), (r / 5.63)))