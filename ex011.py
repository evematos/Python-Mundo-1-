b = float(input('insira largura da parede: '))
h = float(input('insira altura da parede: '))

a = b * h
l = a / 2

print('A dimensão da sua parede é {}x{} e a área é {}m2'.format(b, h, a))
print('Para pintar a parede você precisa de {} litros de tinta'.format(l))
