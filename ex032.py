from datetime import date

ano = int(input('insira 0 para o ano atual ou o ano que desejar para análise: '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('o ano de {} É BISSEXTO'.format(ano))
else:
    print('o ano de {} NÃO É BISSEXTO'.format(ano))