# ler se 3 retar e dizer se pode ser dormado um triangulo
print('-='*20)
print('Analisandor de Triangulos')
print('-='*20)
r1 = float(input('Primeiro segmento:'))
r2 = float(input('SEGUNDO SEGMENTO:'))
r3 = float(input('Terceiro segmento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triangulos!')
else:
    print('Os segmentos acima NAO PODEM FORMAR triangulo!')