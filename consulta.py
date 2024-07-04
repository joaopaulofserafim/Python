produtos = {
    'celular': 1500.00,
    'câmera': 1000.00,
    'fone de ouvido': 800.00,
    'monitor': 2000.00
}

def mostraProdutos(): 
    print(f'Os produtos disponíveis são {produtos}') 

def cadastraProduto():

    cadastrar = input('Deseja cadastrar o produto? (sim/não):').lower()

    if cadastrar == 'sim':
        produto = input('Digite o nome do produto: ').lower()
        preco = int(input(f'Digite o preço do produto: '))
        produtos[produto] = preco
        print('Produto cadastrado com sucesso!')
        print('Lista de produtos atualizada:')
        print(produtos)

    else:
        print('Operação cancelada.')

def consultaProduto():
    mostraProdutos()
    produto = input('Digite o nome do produto: ').lower()

    if produto in produtos:
        print(f'O valor do produto {produto} é R$:{produtos[produto]}')

    else:
        print(f'O produto {produto} não foi encontrado.')
        print(f'Produto {produto} não foi encontrado, Digite "Tentar novamente" para tentar novamente ou "Cadastrar" para cadastrar o produto')
        opcao = input('Digite "Tentar novamente" ou "Cadastrar": ').lower()


        if opcao == 'cadastrar':
            cadastraProduto()
        
        elif opcao == "tentar novamente":
            consultaProduto()

        else:
            print('Opção oferecida não existente')
            mostraProdutos()

consultaProduto()

