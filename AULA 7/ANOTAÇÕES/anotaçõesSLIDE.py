# FUNÇÕES
def dobro(numero): # numero é parâmetro
    return numero * 2

dobro(10) # 10 é argumento

def saudacao_com_horario(nome, periodo = 'Tarde'):
    print(f'Boa {periodo}, {nome}!')

saudacao_com_horario('Carlos')

def operacoes_basicas(a, b):
    return a + b, a - b, a * b

soma, sub, mult = operacoes_basicas(6, 2)
print(soma, sub, mult) # 8 4 12

x = 30 # global

def testar():
    y = 45 # local
    print(x, y)

testar() #10 5
#print(y) -> erro! y não existe fora da função

#Ruim
def soma_ruim(a, b):
    print(a + b)

#Bom
def soma_bom(a,b):
    return a + b

def calcular_imc(peso, altura):
    imc = peso/ (altura ** 2 )
    return imc
peso = float(input('Peso (kg): '))
altura = float(input('Altura (m): '))
imc = calcular_imc(peso, altura)
print(f'Seu IMC é {imc:.2f}')