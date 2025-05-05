import funcoes
from funcoes import *


cartela_de_pontos = {
    'regra_simples':  {
        1:-1,
        2:-1,
        3:-1,
        4:-1,
        5:-1,
        6:-1
    },
    'regra_avancada' : {
        'sem_combinacao':-1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}

rodadas = 1
jogo = True


rolados = rolar_dados(5)
estoque = []

print( "Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
escolha = int(input())

#RODADA 
while jogo == True:
    if escolha == 1:
        dado_guardar = int(input("Digite o índice do dado a ser guardado (0 a 4):"))
        while  0 > dado_guardar > 4:
            print("Opção inválida. Tente novamente.")
            print("Digite o índice do dado a ser guardado (0 a 4):")
            dado_guardar = int(input())

        guardar_dado(rolados,estoque,dado_guardar)

    elif escolha == 2:
        print("Digite o índice do dado a ser removido (0 a 4):")
        dado_remover = int(input())
        while  0 > dado_remover > 4:
            print("Opção inválida. Tente novamente.")
            print("Digite o índice do dado a ser removido (0 a 4):")
            dado_remover = int(input())

        remover_dado(rolados,estoque,dado_remover)

    elif escolha == 3:
        rolagens = 1
        n = len(rolados)
        rolar_dados(n)

    elif escolha == 4:
        imprime_cartela(cartela_de_pontos)

    elif escolha == 0: #faz jogada
        print("Digite a combinação desejada:")
        categoria = input()
        faz_jogada(rolados, categoria, cartela_de_pontos)
        if cartela_de_pontos[categoria] != -1:
            print("Essa combinação já foi utilizada.")
        elif categoria not in cartela_de_pontos:
            print("Combinação inválida. Tente novamente.")
        
    else:
        print("Opção inválida. Tente novamente.")


    print(rolados)
    print(estoque)
    
    
    for regras in cartela_de_ponto.values():
        for valor in regras.values():
            if valor <= 0:
                jogo = True
            else:
                jogo = False

    

    
    

