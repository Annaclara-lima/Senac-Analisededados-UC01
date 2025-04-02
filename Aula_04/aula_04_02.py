#  Faça um programa que receba do usuário o nome e a idade de 10 pessoas. Ao final mostre a soma e a média das idades.

# Entrada dos dados
soma = 0
maior_idade = 0
menor_idade = 200

# Processamento dos dados
for i in range (3):
    nome = input('Informe o nome do usuário: ')
    idade = int(input('Informe a idade do usuário:') )
    
    if idade > maior_idade:
        maior_idade = idade
        maior_nome = nome

    if idade < menor_idade:
        menor_idade = idade
        menor_nome = nome

    soma = soma + idade

# Saída dos dados
print(f'A soma das idades foi {soma}')
print(f'A média das idades foi {(soma / (i+1)):.2f}')
print(f'A pessoa mais velha é: {maior_nome}')
print(f'A pessoa mais nova é: {menor_nome}')



