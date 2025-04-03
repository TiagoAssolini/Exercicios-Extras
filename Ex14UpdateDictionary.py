livro = {
    'titulo': 'Aprendendo Python',
    'autor': 'Fabrício Silva',
    'ISBN': '12345',
    'preco': 59.90,
    'em_estoque': True
}


# Como você faria o acesso ao preço do livro e atualizaria o valor para 69.90 utilizando o que aprendeu sobre dicionários?

#1
livro['preco'] = 69.90
#2
livro.update({'preco': 69.90})

# both are correct