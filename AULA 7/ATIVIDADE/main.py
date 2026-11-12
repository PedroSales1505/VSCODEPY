salarios = [] 
for i in range (1, 6):
    salario = int(input("Digite o seu salário:"))
    salarios.append(salario)
# Cálculos
total = sum(salarios)
media = total / len(salarios)
maior = max(salarios)
menor = min(salarios)

# Conta quantos funcionários ganham acima da média
acima = sum(1 for salarios in salarios if salarios > media)

print(f'Salários registrados: {salarios}')
print(f'Média salarial:R${media:>8.2f}')
print(f'Maior salário:R${maior:>8.2f}')
print(f'Menor salário:R${menor:>8.2f}')
print(f'Acima da média: {acima} funcionário(s)')
print(f'Total da folha: R${total:>8.2f}')