#4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura 
#if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra 
#de acordo com as seguintes condições:

#Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
#Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
#Terceiro Quadrante: os valores de x e y devem ser menores que zero;
#Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
#Caso contrário: o ponto está localizado no eixo ou origem.



coordenada_x = float(input('Digite o número para coordenada X: '))
coordenada_y = float(input('Digite o número para coordenada Y: '))

if coordenada_x > 0 and coordenada_y > 0:
    print("O ponto está no Primeiro Quadrante.")
elif coordenada_x < 0 and coordenada_y > 0:
        print('O ponto está no Segundo Quadrante')
elif coordenada_x < 0 and coordenada_y < 0:
        print('O ponto está no Terceiro Quadrante')
elif coordenada_x > 0 and coordenada_y < 0:
        print('O ponto está no Quarto Quadrante')
else:
    print('O ponto está sobre um eixo ou na origem.')

    

#RESPOSTA

#x = float(input("Digite a coordenada x: "))
#y = float(input("Digite a coordenada y: "))

#- if x > 0 and y > 0:
#-     print("O ponto está no primeiro quadrante.")
#- elif x < 0 and y > 0:
#-   print("O ponto está no segundo quadrante.")
#- elif x < 0 and y < 0:
#   print("O ponto está no terceiro quadrante.")
#elif x > 0 and y < 0:
#    print("O ponto está no quarto quadrante.")
#else:
#    print("O ponto está sobre um eixo ou na origem."
