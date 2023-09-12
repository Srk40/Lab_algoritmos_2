estoque = {}

def adicionar_produto():
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade em estoque: "))
    preco = float(input("Digite o preço unitário: "))
    
    if nome in estoque:
        estoque[nome]["amount"] += quantidade
    else:
        estoque[nome] = {"amount": quantidade, "price": preco}

def buscar_produto():
    nome = input("Digite o nome do produto: ")
    
    if nome in estoque:
        print(f"Produto: {nome}")
        print(f"Quantidade em estoque: {estoque[nome]['amount']}")
        print(f"Preço unitário: R${estoque[nome]['price']:.2f}")
    else:
        print("Produto não encontrado.")

def visualizar_produtos():
    print("Lista de produtos:")
    for nome, info in estoque.items():
        print(f"Produto: {nome}")
        print(f"Quantidade em estoque: {info['amount']}")
        print(f"Preço unitário: R${info['price']:.2f}")
        print("------------")

def vender_produto():
    nome = input("Digite o nome do produto vendido: ")
    
    if nome in estoque:
        quantidade_vendida = int(input("Digite a quantidade vendida: "))
        if quantidade_vendida <= estoque[nome]['amount']:
            estoque[nome]['amount'] -= quantidade_vendida
            valor_venda = quantidade_vendida * estoque[nome]['price']
            print(f"Venda realizada! Total da venda: R${valor_venda:.2f}")
        else:
            print("Quantidade insuficiente em estoque.")
    else:
        print("Produto não encontrado.")

relatorio_vendas = []

def relatorio_de_vendas():
    print("Relatório de Vendas:")
    for venda in relatorio_vendas:
        print(f"Produto: {venda['nome']}")
        print(f"Quantidade vendida: {venda['quantidade']}")
        print(f"Valor total da venda: R${venda['valor']:.2f}")
        print("------------")

while True:
    print("\nOpções:")
    print("1. Adicionar Produto")
    print("2. Buscar Produto")
    print("3. Visualizar Todos os Produtos")
    print("4. Vender Produto")
    print("5. Relatório de Vendas")
    print("6. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        adicionar_produto()
    elif escolha == '2':
        buscar_produto()
    elif escolha == '3':
        visualizar_produtos()
    elif escolha == '4':
        vender_produto()
    elif escolha == '5':
        relatorio_de_vendas()
    elif escolha == '6':
        break
    else:
        print("Opção inválida. Tente novamente.")

