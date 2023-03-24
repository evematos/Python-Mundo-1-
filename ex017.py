from math import hypot

cop = float(input('insira valor do cateto oposto: '))
cad = float(input('insira valor do cateto adjacente: '))

'''hi = (cop ** 2 + cad **2) ** (1/2)'''
hi = hypot(cop,cad)

print('o comprimento da hipotenusa será {:.2f}'.format(hi))