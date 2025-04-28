import random

def rolar_dados(n):
    lista_dados = []
    while len(lista_dados) != n:
        dado = random.randint(1,6)
        lista_dados.append(dado)
    return lista_dados

def guardar_dado(rolados,estoque,indice_dado):
    resposta = []
    novo_estoque = []

    i = 0
    while i < len(estoque):
        novo_estoque.append(estoque[i])
        i+=1

    novo_estoque.append(rolados[indice_dado])
    del(rolados[indice_dado])
    resposta = [rolados,novo_estoque]
    return resposta
  