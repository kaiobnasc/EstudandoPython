# Operadores in e not in
# Strings são iteráveis 
# 0 1 2 3 4 5
# O T Á V I O
#-6-5-4-3-2-1
#nome = 'Otávio'
#print([2])
#print([4])
#print('vio' in nome)
#print('zero' in nome)
#print('vio' not in nome)
#print('zero' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está contido em {nome}')
else:
    print(f'{encontrar} não está contido em {nome}')