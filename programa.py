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

rodadas = 0
#RODADA
while rodadas < 12:
    rolados = rolar_dados(5)
    estoque = []
    rolagens = 0
    jogo = True

    while jogo == True:
        print(f"Dados rolados: {rolados}")
        print(f"Dados guardados: {estoque}")
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

        escolha = input()

        if escolha.isdigit():
            escolha = int(escolha)
        else:
            print("Opção inválida. Tente novamente.")
            escolha = -1


        if escolha == 1:
            print("Digite o índice do dado a ser guardado (0 a 4):")
            dado_guardar = input()
            if dado_guardar.isdigit():
                dado_guardar_int = int(dado_guardar)
                if dado_guardar_int >= 0 and dado_guardar_int < len(rolados):
                    estoque.append(rolados.pop(dado_guardar_int))

                else:
                    print("Opção inválida. Tente novamente.")
            else:
                print("Opção inválida. Tente novamente.")


        elif escolha == 2:
            print("Digite o índice do dado a ser removido (0 a 4):")
            dado_remover = input()
            if dado_remover.isdigit():
                dado_remover_int = int(dado_remover)
                if 0 >= dado_remover_int and dado_remover_int < len(estoque):
                    rolados.append(estoque.pop(dado_remover_int))
                else:
                        print("Opção inválida. Tente novamente.")
            else:
                print("Opção inválida. Tente novamente.")  


        elif escolha == 3:
            if rolagens < 2:
                rolagens += 1
                n = len(rolados)
                rolados = rolar_dados(n)
            else: 
                print("Você já usou todas as rerrolagens.")


        elif escolha == 4:
            imprime_cartela(cartela_de_pontos)


        elif escolha == 0: #faz jogada
            dados_totais = rolados + estoque
            jogada_feita = False

            while jogada_feita == False:
                print("Digite a combinação desejada:")
                categoria = input()

                if categoria == 'sem_combinacao' or categoria == 'quadra' or categoria == 'full_house' or categoria == 'sequencia_baixa' or categoria == 'sequencia_alta' or categoria == 'cinco_iguais':
                    if cartela_de_pontos['regra_avancada'][categoria] == -1:
                        faz_jogada(dados_totais, categoria, cartela_de_pontos)
                        jogada_feita = True
                        jogo = False
                        
                    else:
                        print("Essa combinação já foi utilizada.")

                elif categoria in ['1', '2', '3', '4', '5', '6']:
                    categoria_int = int(categoria)
                    
                    if cartela_de_pontos['regra_simples'][categoria_int] == -1:
                        faz_jogada(dados_totais, categoria_int, cartela_de_pontos)
                        jogada_feita = True
                        jogo = False
                    else:
                        print("Essa combinação já foi utilizada.")
                else:
                    print("Combinação inválida. Tente novamente.")

        else:
            print("Opção inválida. Tente novamente.")

    rodadas +=1

imprime_cartela(cartela_de_pontos)    

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
    

    
    

