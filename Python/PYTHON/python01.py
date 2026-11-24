
#ENTRADA DE DADOS
nome=str(input("Digite seu Nome: "))
idade=int(input("Digite sua Idade: "))
altura=float(input("Digite sua Altura: "))

#SAIDA DE DADOS
print("+++++ Dados Pessoais +++++")
print()
print(f"Nome Completo: {nome}")
print(f" Sua Idade: {idade}")
print(f" Sua Altura: {altura}")

produto=str(input("Digite o produto: "))
qtd=int(input("Digite a quantidade: "))
valor=float(input("Digite o valor do produto: "))
total= qtd*valor
print(f"Produto: {produto}")
print(f"Quantidade: {qtd}")
print(f"Valor Unitário: {valor}")
print(f"Total: {total}")