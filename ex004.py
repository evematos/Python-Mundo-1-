t=input("Digite algo: ")
print("O tipo primitivo desse valor é: {}".format(type(t)))
#verificar se tem apenas números
print("É numérico? {}".format(t.isnumeric()))

#verificar se tem apenas letras E números (tendo 1 dos dois será true)
print("É alfanumérico? {}".format(t.isalnum()))

#verificar se tem apenas letras
print("É alfabético? {}".format(t.isalpha()))

#verificar se tudo está em letra maiúscula
print("É maiúsculo? {}".format(t.isupper()))

#verificar se tudo está em letra minúscula
print("É maiúsculo? {}".format(t.islower()))

#verificar se foi digitado APENAS espaço
print("É maiúsculo? {}".format(t.isspace()))

#verificar se SOMENTE 1 letra é maiúscula e o resto é minúscula
print("É capitalizada? {}".format(t.istitle()))

#Aqui "t" é um objeto, todos os objetos string têm uma caracteristica, realizam uma funcionalidade e possuem atributos e métodos (islower, isupper, etc)
