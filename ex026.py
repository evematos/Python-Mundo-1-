frase = str(input('insira frase desejada: ')).upper().strip()

print('a letra "A" aparece {} vezes'.format(frase.count('A')))
print('ela aparece na posição {} pela primeira vez'.format(frase.find('A')+1))
print('ela aparece na posição {} pela última vez'.format(frase.rfind('A')+1))