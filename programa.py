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
#RODADA
while rodadas <= 12:
    rolados = rolar_dados(5)
    estoque = []
    rolagens = 0
    jogo = True

    while jogo == True:
        print(rolados)
        print(estoque)
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        escolha = int(input())

        if escolha == 1:
            dado_guardar = int(input("Digite o índice do dado a ser guardado (0 a 4):"))
            while dado_guardar < 0 or dado_guardar > 4:
                print("Opção inválida. Tente novamente.")
                print("Digite o índice do dado a ser guardado (0 a 4):")
                dado_guardar = int(input())

            guardar_dado(rolados,estoque,dado_guardar)

        elif escolha == 2:
            print("Digite o índice do dado a ser removido (0 a 4):")
            dado_remover = int(input())
            while dado_remover < 0 or dado_remover > 4:
                print("Opção inválida. Tente novamente.")
                print("Digite o índice do dado a ser removido (0 a 4):")
                dado_remover = int(input())

            remover_dado(rolados,estoque,dado_remover)

        elif escolha == 3:
            if rolagens < 2:
                n = len(rolados)
                rolador = rolar_dados(n)
                rolagens += 1

        elif escolha == 4:
            imprime_cartela(cartela_de_pontos)

        elif escolha == 0: #faz jogada
            print("Digite a combinação desejada:")
            categoria = input()
            categoria_int = int(categoria)
            if categoria_int in cartela_de_pontos["regra_simples"]:
                if cartela_de_pontos['regra_simples'][int(categoria_int)] != -1:
                    print("Essa combinação já foi utilizada.")
                else:
                    faz_jogada(rolados, categoria_int, cartela_de_pontos)
                    jogo = False
            
            elif categoria in cartela_de_pontos['regra_avancada']:
                if cartela_de_pontos['regra_avancada'][categoria] != -1:
                    print("Essa combinação já foi utilizada.")
                else:
                    faz_jogada(rolados, categoria, cartela_de_pontos)
                    jogo = False
            else:
                print("Combinação inválida. Tente novamente.")

        else:
            print("Opção inválida. Tente novamente.")

    rodadas +=1

        
#TOTAL
total_simples = 0
for valor in cartela_de_pontos['regra_simples'].values():
    if valor != -1:
        total_simples += valor

total_avancada = 0
for valor in cartela_de_pontos['regra_avancada'].values():
    if valor != -1:
        total_avancada += valor

if total_simples >= 63:
    bonus = 35
else:
    bonus = 0

total = total_simples + total_avancada + bonus

print(f"Pontuação total: {total}")
    

    
    

