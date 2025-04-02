# Construa um programa onde serão fornecidas as duas notas de dez alunos. Calcule a média de cada aluno e mostre a situação de cada aluno de acordo com as seguintes condições:
# Se a média for maior igual a 70 -> ATENDIDO
# Se a média for maior igual a 30 e menor que 70 -> PARCIALMENTE ATENDIDO
# Se a média for menor que 30 -> NÃO ATENDIDO

# Entrada de dados
for i in range (10):
    nome = input('Informe o nome do usuário: ')
    nota_1 = int(input('Informe a nota 1 do aluno:') ) 
    nota_2 = int(input('Informe a nota 2 do aluno:') ) 
    media = (nota_1 + nota_2)/2
    if media >= 70:
        situacao = 'ATENDIDO'
    elif media >= 30 and media < 70:
        situacao = 'PARCIALMENTE ATENDIDO'
    else:
        situacao ='NÃO ATENDIDO'
    print(f'Sr (a) {nome} a sua média foi {media:.2f}, portanto você está {situacao}')
     



  



