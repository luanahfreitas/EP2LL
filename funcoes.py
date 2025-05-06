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
            soma1 += i
        if i == 2:
            soma2 += i
        if i == 3:
            soma3 += i
        if i == 4:
            soma4 += i
        if i == 5:
            soma5 += i
        if i == 6:
            soma6 += i

    dic = {
        1: soma1,
        2: soma2,
        3: soma3,
        4: soma4,
        5: soma5,
        6: soma6
    }

    return dic

        
        
def calcula_pontos_soma(faces): #sem combinacao
    soma = 0
    for i in range(len(faces)):
        soma+=faces[i]
    return soma

def calcula_pontos_sequencia_baixa(faces): #sequencia baixa
    sequencia = sorted(set(faces))
    n = 1  
    for i in range(len(sequencia) - 1):
        if sequencia[i] + 1 == sequencia[i + 1]: 
            n += 1
            if n >= 4:  
                return 15
        else:
            n = 1  

    return 0 


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

def calcula_pontos_full_house(faces):
    pontos = 0
    soma = 0
    if len(faces) != 5:
        pontos=0
    sequencia = sorted(faces)
    for i in faces:
        soma+=i
    if sequencia[0]==sequencia[1]==sequencia[2]==sequencia[3]==sequencia[4]:
        pontos=0
    elif sequencia[0]==sequencia[1]==sequencia[2] and sequencia[3]==sequencia[4]:
        pontos=soma
    elif sequencia[2]==sequencia[3]==sequencia[4] and sequencia[0]==sequencia[1]:
        pontos=soma

    return pontos
    

def calcula_pontos_quadra(faces):
    pontos = 0
    sequencia = sorted(faces)
    n=1
    if len(faces) < 4:
        pontos = 0
    else:
        for i in range(len(sequencia)-1):
            if sequencia[i] == sequencia[i+1]:
                n += 1
            else:
                if n < 4:
                    n = 1
        if n >= 4:
            for j in range(len(faces)):
                pontos+=faces[j]
        else:
            pontos = 0
    return pontos


def calcula_pontos_quina(faces):
    pontos = 0
    sequencia = sorted(faces)
    n=1
    if len(faces) < 5:
        pontos = 0
    else:
        for i in range(len(sequencia)-1):
            if sequencia[i] == sequencia[i+1]:
                n += 1
            else:
                if n < 5:
                    n = 1
        if n >= 5:
                pontos=50
        else:
            pontos = 0
    return pontos



def calcula_pontos_regra_avancada(faces):

    pontos4 = calcula_pontos_soma(faces)
    pontos6 = calcula_pontos_sequencia_baixa(faces)
    pontos5 = calcula_pontos_sequencia_alta(faces)
    pontos2 = calcula_pontos_full_house(faces)
    pontos3 = calcula_pontos_quadra(faces)
    pontos1 = calcula_pontos_quina(faces)

    dic_pontos={
    'cinco_iguais': pontos1,
    'full_house': pontos2,
    'quadra': pontos3,
    'sem_combinacao': pontos4,
    'sequencia_alta': pontos5,
    'sequencia_baixa': pontos6
    }
    return dic_pontos


def faz_jogada(faces, categoria, cartela_de_pontos):
    #categoria=string
    # ver se categoria é uma chave--reg simples
    if categoria in ['1', '2', '3', '4', '5', '6']:
        num = int(categoria)
        if cartela_de_pontos["regra_simples"][num] == -1:
            pontos = calcula_pontos_regra_simples(faces)
            cartela_de_pontos["regra_simples"][num] = pontos[num]
    else:  
        if categoria in cartela_de_pontos["regra_avancada"].keys():
            if cartela_de_pontos["regra_avancada"][categoria] == -1:
                pontos = calcula_pontos_regra_avancada(faces)
                cartela_de_pontos["regra_avancada"][categoria] = pontos[categoria]
    
    return cartela_de_pontos


def imprime_cartela(cartela):
    print("Cartela de Pontos:")
    print("-"*25)    
    for i in range(1, 7):
        filler = " " * (15 - len(str(i)))
        if cartela['regra_simples'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_simples'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    for i in cartela['regra_avancada'].keys():
        filler = " " * (15 - len(str(i)))
        if cartela['regra_avancada'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_avancada'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    print("-"*25)