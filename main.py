from funcoes import faltouOxigenio, respirar, avancarOuRetroceder, nadar, cacaAoTesouro, slowprint, status, finalizarJogo, apresentarRegrasDoJogo

iniciar_jogo = True 
while iniciar_jogo:
####################### DISCENTE: ESDRAS GOMES CARVALHO ################################################
##### PROJETO: AVENTURA EM ALTO MAR  ////  DISCIPLINA DEVELOPER LIFE //// INSTITUIÇÃO: INSPER ##########

## OBS.: No jogo foi utilizada a regra de que, ao acabar o oxigênio, o jogador não continua a jogada (nadar ou cacar tesouros)
## Além disso, os demais jogadores que não tiverem chegado ao submarino perdem logo que acaba o oxigênio

####### INICIALIZAÇÃO DE VARIAVEIS UTILIZADAS AO LONGO DO PROGRAMA ####################################
    iniciar_jogo = False

    while_jogadores = True
    while while_jogadores:
        while_jogadores = False
        sSlow = 'Quantidade de jogadores que irão participar no jogo: '
        slowprint(sSlow)
        quantidade_de_jogadores = input()
        try:
            int(quantidade_de_jogadores)
            if (int(quantidade_de_jogadores) > 0):
                quantidade_de_jogadores = int(quantidade_de_jogadores)
            else:
                sSlow = 'Digite um valor válido'
                slowprint(sSlow)
        except ValueError:
            sSlow = 'Oh abestado(a), aprendeu os numeros na escola não? Digite certo vá.'
            slowprint(sSlow)
            while_jogadores = True
        
    while_rodadas = True
    while while_rodadas:
        while_rodadas = False
        sSlow = '\nQuantidade de rodadas que a partida terá: '
        slowprint(sSlow)
        quantidade_de_rodadas = input()
        try:
            int(quantidade_de_rodadas)
            if (int(quantidade_de_rodadas) > 0):
                quantidade_de_rodadas = int(quantidade_de_rodadas)
            else:
                sSlow = 'Digite um valor válido'
                slowprint(sSlow)
        except ValueError:
            sSlow = 'Oh abestado(a), aprendeu os numeros na escola não? Digite certo vá.'
            slowprint(sSlow)
            while_rodadas = True       
    
    

    index_jogador = 0
    index_rodada = 0

    nivelOxigenio = 25

    profundidade = []
    for i in range(quantidade_de_jogadores):
        profundidade.append(0)

    listaTesouros = []
    for i in range(quantidade_de_jogadores):
        listaVazia = []
        listaTesouros.append(listaVazia)

    jogadorEstaAvancando = []
    for i in range(quantidade_de_jogadores):
        jogadorEstaAvancando.append(True)

    jogadorNaoFinalizou = []
    for i in range(quantidade_de_jogadores):
        jogadorNaoFinalizou.append(True)

    pontuacaoDoJogador = []
    for i in range(quantidade_de_jogadores):
        pontuacaoDoJogador.append(0)

    jogoNaoTerminou = True

############ PROGRAMA PRINCIPAL #################################################
    apresentarRegrasDoJogo()
    while (index_rodada < quantidade_de_rodadas) and jogoNaoTerminou: ### Laço que especifica a rodada atual do jogo
        sSlow = f'\nRodada: {index_rodada+1}: '
        slowprint(sSlow)

        index_jogador = 0  ## reinicia a variavel index jogador para o novo ciclo do proximo laço
        while (index_jogador < quantidade_de_jogadores): ## Laço que contem as etapas de jogo de um jogador.
                                                        ## Cada jogador passa por todas as etapas do jogo para que o próximo possa jogar.


            if ((jogadorNaoFinalizou[index_jogador])):  ## Condição para analisar se o jogador já finalizou o jogo ou não
                                                    ## Caso tenha finalizado, o proximo jogador que não tenha finalizado faz suas jogadas.
                
                continua_o_jogo = True  ## variavel utilizada para a posterior verificação se o jogador chegou ao fim
                                        ## na etapa "nadar" e garantir que as demais etapas não se sigam.
                quantidadeTesouros = len(listaTesouros[index_jogador]) 

                sSlow = f'\nVez do jogador {index_jogador+1}: '
                slowprint(sSlow)

                if index_rodada > 0:
                    status(nivelOxigenio, profundidade[index_jogador], listaTesouros[index_jogador], index_jogador+1)
                        ## Apresenta os principais dados do jogador, tais como lista de tesouros, profundidade e nivel de oxigenio

                nivelOxigenio = respirar(nivelOxigenio, quantidadeTesouros)  ## chama a funcao respirar que retorna o nivel de oxigenio atualizado.
                if nivelOxigenio < 1:  ## Verificação para analisar se ainda há oxigenio. Caso não haja, o jogo finaliza.
                    faltouOxigenio()
                    quantidade_de_jogadores_que_ficaram_sem_oxigenio = 0
                    for i in range(quantidade_de_jogadores):
                        if jogadorNaoFinalizou[i]:
                            quantidade_de_jogadores_que_ficaram_sem_oxigenio += 1
                        jogadorNaoFinalizou[i] = False
                    if quantidade_de_jogadores_que_ficaram_sem_oxigenio > 1:
                        sSlow = '\nMas veja o lado bom, ao menos você não vai perecer nas profundezas sozinho.\nA amizade do séc XXI é ir pro fundo do poço e levar os amiguinhos junto.'
                        slowprint(sSlow)
                
                if jogadorNaoFinalizou[index_jogador]:
                        
                    if jogadorEstaAvancando[index_jogador]: ## Faz a verificação se o jogador está indo em direção ao fundo do mar ou do submarino
                                                            ## caso esteja indo ao submarino, ela não roda mais, pois não é mais possivel mudar o sentido.
                        escolhaDaDirecao = avancarOuRetroceder(quantidadeTesouros)
                        if escolhaDaDirecao == 'retroceder':
                            
                            sSlow = '\nA caminho do submarino é nosso destino! Lembre que não será mais possível mudar de rumo.'
                            slowprint(sSlow)

                            jogadorEstaAvancando[index_jogador] = False
                        elif escolhaDaDirecao == 'avancar':

                            sSlow = '\nAudacioso como um bom aventureiro deve ser, siga em frente, os tesouros o aguardam.'
                            slowprint(sSlow)

                        else:
                            raise Exception(f'Algum erro ocorreu com a função avancarOuRetroceder, pois foi retornado: {escolhaDaDirecao}.')
                    
                    else:
                        
                        sSlow = '\nComo já estás a retornar, não tens escolha a não seguir em frente.\nApresse o nado para não acabar o oxigênio.'
                        slowprint(sSlow)

                    # A função nadar retorna a quantidade de passos a serem dados pelo jogador
                    passos = nadar(quantidadeTesouros)

                    if jogadorEstaAvancando[index_jogador]: ## Analisa o sentido do movimento e incrementa ou decrementa do nivel de profundidade do jogador.
                        profundidade[index_jogador] = profundidade[index_jogador] + passos
                        if profundidade[index_jogador] > 32:

                            sSlow = f'\nComo o nivel de profundidade máximo é de 32, o valor de sua profundidade atual de {profundidade[index_jogador]} será reduzido ao limite.'
                            slowprint(sSlow)

                            profundidade[index_jogador] = 32
                    else: 
                        profundidade[index_jogador] = profundidade[index_jogador] - passos
                        if profundidade[index_jogador] < 1: ## Caso o jogador volte para uma profundidade nula ou negativa o jogo finaliza
                                                            ## pois ele terá chegado ao submarino.
                            pontuacaoDoJogador[index_jogador] = finalizarJogo(listaTesouros[index_jogador])
                            jogadorNaoFinalizou[index_jogador] = False
                            continua_o_jogo = False

                    if continua_o_jogo:
                        ## chama a função cacaAoTesouro que retorna a lista de Tesouros atualizada
                        listaTesouros[index_jogador] = cacaAoTesouro(quantidadeTesouros, profundidade[index_jogador], listaTesouros[index_jogador], jogadorEstaAvancando[index_jogador])

                        ## apresenta os dados atualizados do jogador. 
                        status(nivelOxigenio, profundidade[index_jogador], listaTesouros[index_jogador], index_jogador+1)

            else:

                sSlow = f'\njogador {index_jogador+1} já finalizou o jogo, aguarde os demais finalizarem para iniciar um novo jogo.'
                slowprint(sSlow)
            index_jogador += 1
        
        ## Verificação para ver se todos os jogadores finalizaram a partida e finaliza o jogo
        NemtodosFinalizaram = True 
        for i in range(len(jogadorNaoFinalizou)):
            NemtodosFinalizaram = NemtodosFinalizaram and (not jogadorNaoFinalizou[i])
        NemtodosFinalizaram = not NemtodosFinalizaram
        if NemtodosFinalizaram:
            pass
        else:
            jogoNaoTerminou = False
        index_rodada += 1

    ## apresenta as pontuações dos jogadores
    for i in range(quantidade_de_jogadores):

        sSlow = f'O jogador {i+1} fez {pontuacaoDoJogador[i]}.'
        slowprint(sSlow)

    mantem_while = True
    while mantem_while:
        mantem_while =  False

        sSlow = '\nDeseja reiniciar o jogo? [s] Sim ou [n] Não. '
        slowprint(sSlow)
        reiniciar_jogo = input()

        if reiniciar_jogo == 's':
            iniciar_jogo = True
        elif reiniciar_jogo == 'n':

            sSlow = '\nObrigado por jogar.'
            slowprint(sSlow)

        else:
            sSlow = 'Não entendi. Pode repetir?'
            slowprint(sSlow)
            mantem_while = True
