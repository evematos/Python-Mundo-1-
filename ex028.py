from random import randint
from time import sleep

print('-=-'*20)
print('Tente adivinhar o número que estou pensando...boa sorte...')
print('-=-'*20)
numpc = randint(0,5)
numus = int(input('Chute um número entre 0 e 5: '))

print('PROCESSANDO...')
sleep(1.5)

if numpc == numus:
    print('ACERTOU!! Eu pensei em {}'.format(numpc))
else:
    print('ERROU!! Eu pensei em {}'.format(numpc))
