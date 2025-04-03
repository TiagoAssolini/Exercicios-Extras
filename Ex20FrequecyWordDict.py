# 5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.

frase = "O Peixe nadava na água. É a repetição de palavras diferentes, porém, parônimas. Caiu e caiu, como se cair, caiu em si! "

contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) +1
print(contagem_palavras)

# [] - são usados para acessar o valor associado a uma chave em um dicionário
# .get() - forma de acessar o valor de uma chave com a possibilidade de definir um valor padrão caso a chave não exista


