numero1 = 17
numero2 = 5

print(numero1 + numero2) # Adição
print(numero1 - numero2) # Subtração
print(numero1 * numero2) # Multiplicação
print(numero1 / numero2) # Divisão (sempre Float)
print(numero1 // numero2) # Divisão inteira (descarta o decimal)
print (numero1 % numero2) # Módulo (RESTO da divisão)
print (numero1 ** numero2) # Potenciação

# Precendência - igual à matemática
print(2+3 * 4) #14 (não 20)
print((2+3)* 4) #20

# Operadores de Atribuição
saldo = 1000
saldo += 500 # saldo = saldo + 500 Resultado 1500
saldo -= 200 # saldo = 1300
saldo *= 2 #2600
print(saldo)


# Operadores Relacionais
x = 10
y = 7
print(x == y) # False - Igual a
print(x != y) # True - diferente de
print(x > y) # True - maior que
print(x < y) # False - menor que
print(x < y) # True - maior ou igual
print(x >= y) # True - maior ou igual
print(x <= y) # False - menor ou igual

# Comparando String
nome = 'Ana'
print(nome == 'Ana')  # True
print(nome == 'ana')  # False (case-sensitive)

# Operadores Lógicos: and, or, not
idade = 20
tem_carteira = True

# and: as Duas condições precisam ser verdadeiras
pode_dirigir >= 18 and tem_carteira
print(pode_dirigir) # True

nota = 6.5
frequencia = 70

# or: PELO MENOS UMA precisa ser verdade
precisa_recuperar = nota < 7.0 or frequencia < 75
print(precisa_recuperar)

# not: Inverte
print(not True)
print(not False)

