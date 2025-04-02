# Faça um programa que pergunte a uma pessoa, a sua idade, o seu peso e quanto dormiu nas últimas 24 h e diga se ela pode doar ou não sangue de acordo com as seguintes condições:
#• Ter entre 16 e 69 anos.
#• Pesar mais de 50 kg.
#• Estar descansado (ter dormido pelo menos 6 horas nas últimas 24 horas)

# Entrada dos dados
nome = input('informe o seu nome:')
idade = int(input('Informe a idade:'))
peso = float(input('Informe o peso:'))
horas = int(input('Informe a quantidade de horas que dormiu:'))

# Processamento de dados

if idade >= 16 and idade <= 69 and peso >50 and horas >=6 :
    print(f'Sr(a) {nome}, pode doar sangue') 
elif idade <16 or idade >70:
    print(f'Sr(a) {nome}, para doação a sua idade deverá estar entre 16 e 69 anos')
elif peso <50:
    print (f'Sr(a) {nome}, para doação deverá com mis de 50kg')
elif horas <6:
    print(f'Sr(a) {nome}, para doação deverá ter dormindo pelo menos 6 horas')

