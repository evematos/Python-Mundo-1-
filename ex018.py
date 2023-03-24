import math
angulo = float(input('insira ângulo desejado: '))

seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))

print('o SENO de {} é {:.2f}'.format(angulo,seno))
print('o COSSENO de {} é {:.2f}'.format(angulo,cos))
print('a TANGENTE de {} é {:.2f}'.format(angulo,tang))
