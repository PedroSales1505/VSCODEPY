# Trecho A - NameError: o print estava com P maiúsculo.
print("Olá, turma!")

# Trecho B - SyntaxError: faltava fechar as aspas duplas no final do texto.
print("Bem-vindo ao SENAI")

# Trecho C - NameError: o texto precisava estar entre aspas para ser reconhecido como string.
curso = "Desenvolvimento de Sistemas"
print(curso)

# Trecho D - NameError: o valor booleano em Python deve começar com letra maiúscula (True).
ativo = True
print(ativo)

# Trecho E - SyntaxError: nomes de variáveis em Python não podem começar com números.
nome2 = "Ana"
print(nome2)

# Trecho F - SyntaxError/NameError: faltava a vírgula separando o texto da variável e o continue estava isolado.
total = 150
print("Total:", total)

#Trecho G (digite um número quando o programa pedir) - TypeError: Faltou o int para ser um input formatado para inteiro.
idade = int(input("Digite sua idade: "))
print("Ano que vem você terá:", idade + 1)

#Trecho H (atenção: este não mostra mensagem de erro, mas o resultado está errado) - A vírgula cria uma tupla.
preco = 10.50
print("Preço de duas unidades: ", preco * 2)

#Trecho I (atenção: também não mostra erro; a média de 8 e 6 deveria ser 7) - Não teve parênteses assim fazendo começar pela divisão.
nota1 = 8
nota2 = 6
media = (nota1 + nota2) / 2
print("Média:", media)