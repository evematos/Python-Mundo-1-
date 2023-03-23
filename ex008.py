m = float(input('insira valor em métros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000

print('convertendo {} métros temos os valres: '.format(m))
print('{} quilômetro'.format(km))
print('{} hectômetro'.format(hm))
print('{} decâmetro'.format(dam))
print('{:.0f} decímetros'.format(dm))
print('{:.0f} centímetros'.format(cm))
print('{:.0f} milímetros'.format(mm))