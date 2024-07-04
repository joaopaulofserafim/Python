
numeros = []
pares = []  
impares = []

entrada = input("Digite um número (ou 'sair' para encerrar): ")
while entrada.lower() != 'sair':
    numero = int(entrada)
    numeros.append(numero)
    entrada = input("Digite um número (ou 'sair' para encerrar): ")

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

#sort()  EM ORDEM CRESCENTE 

print(f'Números pares em ordem crescente: {pares}')
print(f'Números ímpares em ordem crescente: {impares}')

    
somaImpares = sum(impares)  #sum FUNÇÃO DE SOMA
somaPares = sum(pares)

print(f'Soma dos números ímpares: {somaImpares}')
print(f'Soma dos números pares: {somaPares}')




