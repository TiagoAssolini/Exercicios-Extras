# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

lista_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

soma_impares = 0

for i in range(1, 11, 2):
    soma_impares += i
print(soma_impares)