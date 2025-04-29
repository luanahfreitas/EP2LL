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
  
def remover_dado(rolados,estoque,num):
    #num= número inteiro que representa o indice do dado a ser removido
    resposta = []

    rolados.append(estoque[num])

    del(estoque[num])

    resposta = [rolados,estoque]
    return resposta

def calcula_pontos_regra_simples(faces):
    soma1=0
    soma2=0
    soma3=0
    soma4=0
    soma5=0
    soma6=0
    for i in faces:
        if i == 1:
            soma1+=1
        if i == 2:
            soma2+=2
        if i == 3:
            soma3+=3
        if i == 4:
            soma4+=4
        if i == 5:
            soma5+=5
        if i == 6:
            soma6+=6
    
    dic={}
    dic[1] = soma1
    dic[2] = soma2
    dic[3] = soma3
    dic[4] = soma4
    dic[5] = soma5
    dic[6] = soma6

    return dic

        
        
def calcula_pontos_soma(faces): #sem combinacao
    soma = 0
    for i in range(len(faces)):
        soma+=faces[i]
    return soma

def calcula_pontos_sequencia_baixa(faces): #sequencia baixa
    pontos = 0
    nova = []

    for i in range(len(faces)):
        if faces[i] not in nova:
            nova.append(faces[i])

    sequencia = sorted(nova)
    n=1
    if len(faces) < 4:
        pontos = 0
    else:
        for i in range(len(sequencia)-1):
            if sequencia[i] +1 == sequencia[i+1]:
                n += 1
            else:
                if n < 4:
                    n = 0
        if n >= 4:
            pontos = 15
        else:
            pontos = 0
    return pontos


def calcula_pontos_sequencia_alta(faces): #sequencia alta
    pontos=0
    nova=[]

    for i in range (len(faces)):
        if faces[i] not in nova:
            nova.append(faces[i])

    sequencia = sorted(nova)
    n=1
    if len(faces) < 5:
        pontos = 0
    else:
        for i in range(len(sequencia)-1):
            if sequencia[i] +1 == sequencia[i+1]:
                n += 1
            else:
                if n < 5:
                    n = 0
        if n >= 5:
            pontos = 30
        else:
            pontos = 0
    return pontos