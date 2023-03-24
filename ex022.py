nome = str(input('insira seu nome completo: ')).strip()

separa = nome.split()
print('seu nome em letras maiúsculas é: {}'.format(nome.upper()))
print('seu nome em letras maiúsculas é: {}'.format(nome.lower()))
print('seu nome possui {} letras'.format(len(nome) - nome.count(' ')))
print('seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
