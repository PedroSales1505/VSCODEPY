# While
contador = 1

while contador <= 5:
    print(f'Contagem: {contador}')
    contador += 1

print('Fim')

# ==============
SENHA = 'senai2026'
tentativas = 0
MAX = 3

while tentativas < MAX:
    senha = input('Digite a senha: ')
    tentativas += 1

    if senha == SENHA:
        print('Acesso concedido')
        break
    else:
        restantes = MAX - tentativas
        if restantes > 0:
            print(f'{restantes} tentativas restantes')
if tentativas == MAX and senha != SENHA:
    print('Conta bloqueada')

# FOR - RANGE()
for i in range(5): # imprimir 5 digitos 0, 1, 2, 3, 4
    print(i, end='')
print()

for i in range(6): # imprimir 6 digitos 0, 1, 2, 3, 4, 5
    print(i, end='')
print()

for i in range(0, 11, 2): # imprimir pares 0, 2, 4, 6, 8, 10
    print(i, end='')
print()


for i in range(11, 0, -1): # contagem regressiva
    print(i, end='')
print()

# BREAK e CONTINUE
# break - para o loop
for numero in range(1, 11):
    if numero == 6:
        print( '\n Achei o 6! Parando')
        break
    print(numero, end='')

# continue - pula a interação atual
for n in range (1, 11):
    if n % 2 == 0: #pula pares
        continue
    print(n, end='')