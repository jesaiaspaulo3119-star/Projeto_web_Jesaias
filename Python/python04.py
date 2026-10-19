#1. Entrada de Dados
nome_produto= input("Digite o nome do produto: ")
preco_original= float(input("Digite o preço original do produto (R$): "))

#2. Processamento (calculo do preço com desconto)
valor_desconto = preco_original * 0.10
preco_final = preco_original - valor_desconto

#3. Saída de Dados
print("===Resumo do Compra===")
print(f"Produto: {nome_produto}")
print(f"Preço Original: R$ {preco_original:.2f}")
print(f"Desconto: R$ {valor_desconto:.2f}")
print(f"Preço Final: R$ {preco_final:.2f}")