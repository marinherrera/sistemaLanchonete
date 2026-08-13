# Menu principal
def menu():
    print("\n---------- MENU PRINCIPAL ----------")
    print("1 - Administrador")
    print("2 - Operador")
    print("0 - Sair")
    return input("Escolha uma opção: ").strip()

# Funções do administrador
def cadastrar_produto():
    lista = listar()
    codigo = input("Código do produto: ").strip()
    codigos = []
    for p in lista:
        codigos.append(p[0])
    if codigo in codigos:
        print("Código já existe.")
    else:
        produto = input("Nome do produto: ").strip()
        preco = input("Preço do produto: ").strip()
        if preco.replace(".", "", 1).isdigit():
            lista.append([codigo, produto, preco])
            gravar_txt(lista)
            print("Produto cadastrado!")
        else:
            print("Preço inválido.")

def listar_produtos():
    lista = listar()
    if len(lista) == 0:
        print("Nenhum produto cadastrado.")
    else:
        print("\n---------- PRODUTOS ----------")
        for p in lista:
            print("Código:", p[0], "| Produto:", p[1], "| Preço: R$", p[2])

def alterar_produto():
    lista = listar()
    if len(lista) == 0:
        print("Nenhum produto para alterar.")
    else:
        ind = buscar_indice(lista)
        novo_prod = input("Novo produto [" + lista[ind][1] + "]: ").strip()
        novo_preco = input("Novo preço [" + lista[ind][2] + "]: ").strip()
        if novo_prod != "":
            lista[ind][1] = novo_prod
        if novo_preco != "":
            if novo_preco.replace(".", "", 1).isdigit():
                lista[ind][2] = novo_preco
            else:
                print("Preço inválido.")
        gravar_txt(lista)
        print("Produto alterado!")

def remover_produto():
    lista = listar()
    if len(lista) == 0:
        print("Nenhum produto para remover.")
    else:
        ind = buscar_indice(lista)
        produto = lista[ind][1]
        del lista[ind]
        gravar_txt(lista)
        print("Produto", produto, "removido.")

def menu_administrador():
    continuar = "1"
    while continuar == "1":
        print("\n---------- MENU ADMINISTRADOR ----------")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Alterar produto")
        print("4 - Remover produto")
        print("0 - Voltar")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            alterar_produto()
        elif opcao == "4":
            remover_produto()
        elif opcao == "0":
            continuar = "0"
        else:
            print("Opção inválida.")

# Menu do operador
def menu_operador():
    nome = input("Digite seu nome: ")
    print(f"\nOlá, {nome}! Iniciando atendimento.")
    operar_pedido()

# Função para realizar um pedido
def operar_pedido():
    lista = listar()
    if len(lista) == 0:
        print("Cardápio vazio.")
        return

    pedido = []

    continuar = "1"
    while continuar == "1":
        print("\n========== CARDÁPIO ==========")
        for p in lista:
            print(p[0], "|", p[1], "| R$", p[2])
        cod = input("Digite o código do produto (ou 0 para finalizar): ").strip()
        if cod == "0":
            continuar = "0"
        else:
            achou = "0" 
            for p in lista:
                if p[0] == cod:
                    achou = "1"
                    qtd = input("Digite a quantidade: ").strip()
                    if qtd != "" and qtd.isdigit() and int(qtd) > 0:
                        qtd_int = int(qtd)
                        ja_tem = "0"
                        for item in pedido:
                            if item[0] == cod:
                                item[3] += qtd_int
                                ja_tem = "1"
                        if ja_tem == "0":
                            pedido.append([p[0], p[1], p[2], qtd_int])
                        print("Produto adicionado!")
                    else:
                        print("Quantidade inválida.")
            if achou == "0":
                print("Código inválido.")
    if len(pedido) == 0:
        print("Nenhum produto escolhido.")
        return

    total = 0
    for item in pedido:
        preco = item[2]
        qtd = item[3]
        subtotal = float(preco) * qtd
        print(qtd, "x", item[1], "- R$", subtotal)
        total = total + subtotal
    print("Total: R$", total)

    print("\nFormas de pagamento:")
    print("1 - Dinheiro")
    print("2 - Cartão")
    print("3 - Pix")
    forma = input("Escolha a forma de pagamento: ").strip()

    if forma == "1":
        print("Pagamento em Dinheiro")
    elif forma == "2":
        print("Pagamento em Cartão")
    elif forma == "3":
        print("Pagamento em Pix")
    else:
        print("Forma inválida. Pedido cancelado.")
        return

    print("Pedido finalizado. Volte sempre :)!")

# Função para listar os produtos do arquivo
def listar():
    lista_prod = []

    arquivo = open('produtos1.txt', 'a', encoding='utf-8')
    arquivo.close()

    arquivo = open('produtos1.txt', 'r', encoding='utf-8')
    linhas = arquivo.readlines()
    arquivo.close()

    for linha in linhas:
        partes = linha.strip().split(" | ")
        if len(partes) == 3:
            lista_prod.append(partes)
    return lista_prod

# Função para gravar a lista no arquivo
def gravar_txt(lista_prod):
    arquivo = open('produtos1.txt', 'w', encoding='utf-8')
    for produto in lista_prod:
        linha = produto[0] + " | " + produto[1] + " | " + produto[2] + "\n"
        arquivo.write(linha)
    arquivo.close()

# Função para buscar produto
def buscar_indice(lista_prod):
    codigos = []
    for i in range(len(lista_prod)):
        codigos.append(lista_prod[i][0])
    op = input("Escolha o código do produto que você deseja alterar: ").strip()
    while op not in codigos:
        print("\nCódigo inválido. Confira a lista de produtos:\n")
        for prod in lista_prod:
            print("Código:", prod[0], "| Produto:", prod[1], "| Preço:", prod[2])
        op = input("\nEscolha um código válido: ").strip()
    return codigos.index(op)

op = ""
while op != "0":
    op = menu()
    if op == "1":
        menu_administrador()
    elif op == "2":
        menu_operador()
    elif op == "0":
        print("Saindo do sistema. Até mais!")
    else:
        print("Opção inválida.")
