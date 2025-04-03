# 7 - Construa um código que calcule a média dos valores em uma lista. 
# Utilize um bloco try-except para lidar com a divisão por zero, 
# caso a lista esteja vazia.

lista_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

soma = 0

try:
    for i in lista_num:
        soma += i 
        media = soma / len(lista_num) #dificil
        print(f"Média dos valores: {media}")
        #print(soma/10)
#except Exception as e:
#    print('Houve um erro, divisão não pode ser efetuada por ZERO! ')
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
