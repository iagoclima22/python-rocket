# Criando um dicionário de exemplo
pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}

# Exibindo o dicionário
print("Meu dicionário de exemplo:", pessoa)

# Acessando valores por chave
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])

pessoa["sobrenome"] = "Silva"
print("Sobrenome:", pessoa["sobrenome"])
print("Meu dicionário de exemplo:", pessoa)

pessoa["idade"] = 31
print("Idade atualizada:", pessoa["idade"])

# Removendo um par chave-valor
del pessoa["sobrenome"]
print("Meu dicionário de exemplo:", pessoa)

# Métodos: keys(), values(), items()
chaves = list(pessoa.keys())
print("Chaves do dicionário:", chaves)
print("Primeira chave:", chaves[0])

# Método values
valores = pessoa.values()
print("Valores do dicionário:", valores)
print("Primeiro valor do dicionário:", valores[0])

# Métodos items
itens = pessoa.items()
print("Pares chave-valor do dicionário:", itens)
print("Primeiro valor:", itens[0][1])

