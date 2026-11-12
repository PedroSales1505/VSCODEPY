# Capturar texto
nome = input('Digite seu nome: ')
print(f'Olá, {nome}')

# SEM conversão gera erro (errado para calculo)
# idade = input ('Idade: ')
# print(idade + 1) TypeError!

#COM conversão (correto):
idade = int(input('Digite sua idade'))
print(f'Você tem {idade} anos')
print (f'Em 10 anos você terá {idade + 10} anos')