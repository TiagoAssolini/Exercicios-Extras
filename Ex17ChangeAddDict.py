# 2 - Utilizando o dicionário criado no item 1:

# Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
# Adicione um campo de profissão para essa pessoa;
# Remova um item do dicionário.

Info = {
    'nome':'Carlos', 
    'idade':20, 
    'cidade':'Araraquara'
}
print(Info)

Info['idade'] = 24 # Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
print(Info)

Info['profissão']='vagabundo' # Adicione um campo de profissão para essa pessoa;
print(Info)

del Info['cidade'] # Remova um item do dicionário.
print(Info)

Info.pop('idade') # Remova um item do dicionário.
print(Info)

nome = Info.get('nome')
print(type(nome))

carlos = ("Patrono")
print(type(carlos))

carlos3 = ("Patrono",)
print(type(carlos3))


carlos2 = {
    'nome':'Carlos', 
    'idade':20, 
    'cidade':'Araraquara',
    'nome':'Carlos',
}
print(type(carlos2))
print(carlos2)

print('')

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict['year'])

