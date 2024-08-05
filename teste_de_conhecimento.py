'''
Peça ao usuário para digitar seu nome e sua idade
Exiba na tela:
    seu nome 
    seu nome invertido
    se seu nome contém ou não
    número de letras que contem no nome
    a primeira letra do nome
    a última letra do nome
    se nada for digitado, exiba "Desculpe, você deixou os campos vazios."
'''

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print('Desculpe, você deixou os campos vazios.')