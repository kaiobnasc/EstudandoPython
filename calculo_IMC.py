# IMC é o peso dividido pela altura ao quadrado.

nome = 'Kaio Nascimento'
altura = 1.74
peso = 64
imc = peso/altura**2

# f strings ou formatação de strings

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'Pesa {peso} quilos e seu imc é {imc}'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)