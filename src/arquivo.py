nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

def informaIdade(nome, idade):
    print(f'Olá, seu nome é {nome} e irá fazer {idade + 1} anos no proximo ano')
    return nome, idade

informaIdade(nome, idade)
