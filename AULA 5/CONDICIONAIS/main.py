# Estruturas Condicionais
idade = int(input("Digite a sua idade: "))
anos = 18 - idade
if idade >= 18:
    print('Você é maior de idade, sua idade é:',idade )
    print('Acesso permitido')
else:
    print('Você é menor de idade, sua idade é:', idade )
    print('Faltam', anos, 'anos para ser maior de idade')
    print('Acesso negado') 

#if / else
nota = float(input('Digite a nota do aluno:'))
if nota >= 7.0:
    print('Aprovado')
else:
    print('Recuperação.')

# if / elif / else
historia = float(input('Digite a nota: '))
if historia >= 9.0:
    conceito = 'A'
    situacao = 'Excelente'
elif historia >= 7.0:
    conceito = 'B'
    situacao = 'Bom'
elif historia >= 5.0:
    conceito = 'C'
    situacao = 'Regular'
else:
    conceito = 'D'
    situacao = 'Ruim'

print(f'Conceito: {conceito} | Situação: {situacao}')