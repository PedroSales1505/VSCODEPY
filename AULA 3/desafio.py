produto = input("Produto: ")
preco = float(input("Preço: "))
quantidade = int(input("Quantidade: "))

disponivel = True

print(f"Produto: {produto}")
print(f"Preço: {preco}")
print(f"Quantidade: {quantidade}")
print(f"Disponível: {disponivel}")
print(f"Valor total em estoque: {preco * quantidade}")

print(f"Tipo de nome: {type(produto)}")
print(f"Tipo de preço: {type(preco)}")
print(f"Tipo de quantidade: {type(quantidade)}")
print(f"Tipo de disponível: {type(disponivel)}")