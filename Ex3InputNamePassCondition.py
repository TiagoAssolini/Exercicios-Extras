#3 - Solicite um nome de usuário e uma senha e use uma estrutura 
#if else para verificar se o nome de usuário e a senha fornecidos 
#correspondem aos valores esperados determinados por você.
import re
name = str(input('\nEnter your name: '))
password = (input('Enter a password. \nPassword is at lest 6 letters, \nhas a number in it, \nhas a capital letter in it: \n'))

if len(password) < 6:
    print("Make sure your password is at lest 6 letters. ")
elif re.search('[0-9]',password) is None:
    print("Make sure your password has a number in it. ")
elif re.search('[A-Z]',password) is None: 
    print("Make sure your password has a capital letter in it. ")
else:
    print("Your password seems fine, congratulations!")



#RESPOSTA
    
#usuario_correto = "alura"
#senha_correta = "alura123"

#usuario = input("Digite o nome de usuário: ")
#senha = input("Digite a senha: ")

#if usuario == usuario_correto and senha == senha_correta:
#    print("Login bem sucedido!")
#else:
#    print("Credenciais inválidas. Tente novamente.")
