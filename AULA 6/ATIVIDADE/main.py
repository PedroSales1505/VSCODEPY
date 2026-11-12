Continuar = True
while Continuar:
    numero = int(input('Por favor, informe um número inteiro: '))
    for i  in range(+1, 11):
        tabuada = numero * i
        print(f'{numero} x {i} = {tabuada}')
    resposta2 = input('Deseja ver outra tabuada, escolha (s/n): ')
    if resposta2 == 's':
        Continuar = True
        print('Então irei continuar')

    else:
        Continuar = False
        print('Então irei parar')
        break