r1 = float(input('insira a 1° segmento: '))
r2 = float(input('insira a 2° segmento: '))
r3 = float(input('insira a 3° segmento: '))

if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print('os segmentos indicados PODEM FORMAR um triândulo')
else:
    print('os segmentos indicados NÃO PODEM FORMAR um triângulo')