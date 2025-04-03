#There are many ways that we can compare values with Python, such as 
#equals ( == ), not equals ( != ), greater than ( > ), less than ( < ), 
#greater than or equal to ( >= ), or less than or equal to ( <= ).

#2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:
#Criança: 0 a 12 anos;
#Adolescente: 13 a 18 anos;
#Adulto: acima de 18 anos.


idade = int(input('Informe sua idade: '))

if 0 <= idade <= 12:
    print('Você é uma Criança!')
elif 13 <= idade <=18:
    print('Você é um Adolescente!')
elif idade > 18:
    print('Você é um Adulto!')
else:
    print('Você não digitou um número válido, digite um número entre 0 e 140!')





# RESPOSTA
    
#idade = int(input("Digite sua idade: "))
#if 0 < idade <= 12:
#    print("Criança")
#elif 12 < idade <= 18:
#    print("Adolescente")
#elif idade > 18:
#    print("Adulto")
#else: 
#    print("Valor inválido!")
