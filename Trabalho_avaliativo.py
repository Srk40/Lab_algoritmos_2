#O programa começa com um dicionário vazio chamado "estoque" para armazenar informações sobre os produtos em estoque.
#Cada chave no dicionário é o nome de um produto, e os valores associados são outro dicionário que contém a quantidade em estoque e o preço unitário do produto.

estoque = {}

# "adicionar_produto" Esta função permite ao usuário adicionar um novo produto ao estoque ou atualizar a quantidade de um produto existente.
#Ela solicita ao usuário que insira o nome do produto, a quantidade em estoque e o preço unitário.
#Se o produto já existir no estoque, a quantidade é atualizada; caso contrário, um novo produto é adicionado ao dicionário de estoque.

def adicionar_produto():
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade em estoque: "))
    preco = float(input("Digite o preço unitário: "))
    
    if nome in estoque:
        estoque[nome]["amount"] += quantidade
    else:
        estoque[nome] = {"amount": quantidade, "price": preco}

# "buscar_produto" Esta função permite ao usuário buscar informações sobre um produto específico.
#O usuário fornece o nome do produto, e o programa verifica se o produto existe no estoque.
#Se existir, exibe o nome, quantidade em estoque e preço unitário. Se não existir, informa que o produto não foi encontrado.

def buscar_produto():
    nome = input("Digite o nome do produto: ")
    
    if nome in estoque:
        print(f"Produto: {nome}")
        print(f"Quantidade em estoque: {estoque[nome]['amount']}")
        print(f"Preço unitário: R${estoque[nome]['price']:.2f}")
    else:
        print("Produto não encontrado.")

# "visualizar_produtos" Esta função lista todos os produtos no estoque, exibindo o nome, quantidade em estoque e preço unitário de cada produto.

def visualizar_produtos():
    print("Lista de produtos:")
    for nome, info in estoque.items():
        print(f"Produto: {nome}")
        print(f"Quantidade em estoque: {info['amount']}")
        print(f"Preço unitário: R${info['price']:.2f}")
        print("------------")

# "vender_produto" Esta função permite ao usuário registrar uma venda de um produto.
#O usuário fornece o nome do produto e a quantidade vendida.
#Se houver estoque suficiente, a quantidade vendida é subtraída do estoque e o valor total da venda é calculado e exibido.
#Caso contrário, é informado que a quantidade em estoque é insuficiente.

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

# "relatorio_vendas" Esta lista é usada para armazenar informações sobre as vendas realizadas.
#Cada venda é representada como um dicionário com as chaves 'nome' (nome do produto), 'quantidade' (quantidade vendida) e 'valor' (valor total da venda).

while True:
    print("\nOpções:")
    print("1. Adicionar Produto")
    print("2. Buscar Produto")
    print("3. Visualizar Todos os Produtos")
    print("4. Vender Produto")
    print("5. Relatório de Vendas")
    print("6. Sair")

#O programa entra em um loop infinito que exibe um menu com opções para o usuário.
#O usuário pode escolher entre adicionar um produto, buscar um produto, visualizar todos os produtos, vender um produto, exibir um relatório de vendas ou sair do programa.
#O programa lê a escolha do usuário e chama a função correspondente com base na escolha.

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

#Quando o usuário escolhe sair (opção 6), o programa sai do loop principal e encerra a execução.
