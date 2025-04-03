# Você está criando seu portfólio para mostrar seus projetos de Python. 
# Para isso, você quer incluir uma seção que destaque suas habilidades com listas, 
# loops for e tratamento de exceções, mas quer garantir que mesmo que algum dado esteja ausente, 
# seu portfólio não quebre.

# A que melhor implementa o uso de listas, blocos for e try except.


projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

for projeto in projetos:
  if projeto:
    print(f"Projeto: {projeto}")
  else:
    print("Projeto não disponível.")