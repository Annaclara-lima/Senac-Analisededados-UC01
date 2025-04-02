# Tendo como dado de entrada à altura (h) de uma pessoa, construa um programa que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

# Entrada dos dados
nome = input('informe o seu nome:')
altura = float(input('informe a sua altura em metros: '))
sexo = input ('Informe M para Masculino ou F para Feminino:')

# Processamento dos dados
if sexo == 'M'or sexo == 'm':
    h = (72.7*altura) - 58
    print(f'Sr(a) {nome}, o seu peso ideal  é {h:.0f} kg.')
elif sexo == 'F' or sexo == 'f':
    m = (62.1*altura) - 44.7
    print(f'Sr(a){nome}, o seu peso ideal é {m} kg.')
else:
    print('Verifique o sexo informado')
