# Escreva um programa que, dados 2 números inteiros (n1 e n2), diga se eles são iguais ou diferentes.Some os dois valores se forem diferentes e multiplique-os se forem iguais.

# Entrada dos dados
n1 = int(input('Informe o primeiro valor:'))
n2 = int(input('Informe o segundo valor:'))

# Processamento dos dados
if n1 == n2:
    valor = n1 * n2
    print(f'Eles são iguais, sua multiplicação é {valor}: ')
else:
    valor = n1 + n2
    print(f'Eles são diferentes, sua soma é {valor}:')


