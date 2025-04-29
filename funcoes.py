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
    pontos1 = 0
    sequencia1 = sorted(faces)
    n1=1
    if len(faces) < 5:
        pontos1 = 0
    else:
        for i in range(len(sequencia1)-1):
            if sequencia1[i] == sequencia1[i+1]:
                n1 += 1
            else:
                if n1 < 5:
                    n1 = 1
        if n1 >= 5:
                pontos1=50
        else:
            pontos1 = 0


    pontos2 = 0
    soma2 = 0
    if len(faces) != 5:
        pontos2=0
    sequencia2 = sorted(faces)
    for i in faces:
        soma+=i
    if sequencia2[0]==sequencia2[1]==sequencia2[2]==sequencia2[3]==sequencia2[4]:
        pontos2=0
    elif sequencia2[0]==sequencia2[1]==sequencia2[2] and sequencia2[3]==sequencia2[4]:
        pontos2=soma2
    elif sequencia2[2]==sequencia2[3]==sequencia2[4] and sequencia2[0]==sequencia2[1]:
        pontos2=soma2


    

    pontos3 = 0
    sequencia3 = sorted(faces)
    n3=1
    if len(faces) < 4:
        pontos3 = 0
    else:
        for i in range(len(sequencia3)-1):
            if sequencia3[i] == sequencia3[i+1]:
                n3 += 1
            else:
                if n3 < 4:
                    n3 = 1
        if n3 >= 4:
            for j in range(len(faces)):
                pontos3+=faces[j]
        else:
            pontos3 = 0

    
    pontos4=0
    for i in range(len(faces)):
        pontos4+=faces[i]

    
    
    pontos5=0
    nova=[]
    for i in range (len(faces)):
        if faces[i] not in nova:
            nova.append(faces[i])

    sequencia5 = sorted(nova)
    n=1
    if len(faces) < 5:
        pontos5 = 0
    else:
        for i in range(len(sequencia5)-1):
            if sequencia5[i] +1 == sequencia5[i+1]:
                n5 += 1
            else:
                if n5 < 5:
                    n5 = 0
        if n5 >= 5:
            pontos5 = 30
        else:
            pontos5 = 0
            

    pontos6 = 0
    nova2 = []
    for i in range(len(faces)):
        if faces[i] not in nova2:
            nova2.append(faces[i])

    sequencia6 = sorted(nova2)
    n6=1
    if len(faces) < 4:
        pontos6 = 0
    else:
        for i in range(len(sequencia6)-1):
            if sequencia6[i] +1 == sequencia6[i+1]:
                n6 += 1
            else:
                if n6 < 4:
                    n6 = 0
        if n6 >= 4:
            pontos6 = 15
        else:
            pontos6 = 0

    dic_pontos={
    'cinco_iguais': pontos1,
    'full_house': pontos2,
    'quadra': pontos3,
    'sem_combinacao': pontos4,
    'sequencia_alta': pontos5,
    'sequencia_baixa': pontos6
    }
    return dic_pontos

    



