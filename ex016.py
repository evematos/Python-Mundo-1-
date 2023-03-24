import math

num = float(input('insira número: '))

print('a porção inteira do número {} é {}'.format(num, math.floor(num)))
print('a porção inteira do número {} é {}'.format(num, math.trunc(num)))

"""
num = float(input('insira número: '))
print('a porção inteira do número {} é {}'.format(num, int(num)))
"""