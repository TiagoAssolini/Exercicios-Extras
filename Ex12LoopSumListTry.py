# 6 - Crie uma lista de números e 
# utilize um loop for para calcular a 
# soma de todos os elementos. 
# Utilize um bloco try-except para lidar com possíveis exceções.

lista_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# EZ WAY - print(sum(lista_num))
soma = 0

try:
    for i in lista_num:
        soma += i
        print(f'Soma dos elementos {soma}')
except Exception as e:
    print('Ocorreu um erro {e}')
