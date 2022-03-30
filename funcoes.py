from random import randint
import sys
import time

        

def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./70)

def apresentarRegrasDoJogo():
    
    mantem_while = True
    while mantem_while:
        mantem_while = False

        sSlow = '\nDeseja saber as regras do jogo? [s] sim ou [n] não? '
        slowprint(sSlow)
        escolha = input()

        if escolha == 's':
            print(
                """s
Regras
A cada rodada o jogo deve seguir os passos descritos a seguir:
Respirar: 
Jogo verifica se há a necessidade de reduzir o oxigênio.
O oxigênio deve ser reduzido de acordo com a quantidade de tesouros que o mergulhador estiver carregando.
Ou seja, se o jogador estiver carregando 2 tesouros o nível do oxigênio deve diminuir 2 níveis.
Se o mergulhador não estiver carregando nenhum tesouro então não há a necessidade de reduzir o oxigênio.
Se o oxigênio alcançar o nível 0 ou menor, o jogador da vez termina a rodada e o jogo acaba.


Avançar ou Retroceder?: 
No início da partida o jogador começa dentro do submarino.
Depois de sair do submarino ele deve escolher continuar avançando para o fundo do mar ou voltar para o submarino.
O mergulhador não pode voltar para o submarino sem tesouros.
O mergulhador só pode voltar para o submarino uma única vez.
Quando o mergulhador decidir retornar para o submarino ele não pode avançar de volta para o fundo do mar.
Depois que o jogador decidir retroceder o jogador não precisa passar por este passo,
pois a única opção agora será retroceder.
 
Nadar: 
Jogador rola dois dados d3 (Dado de três faces.) para verificar o avanço.
A soma dos dois resultados do dado d3 representa a profundidade em que o mergulhador vai nadar.

Se o jogador estiver carregando tesouros,
então a quantidade de tesouros carregados deve ser subtraído do valor do avanço.
(Exemplo: Se um dado sorteou o valor 1 e o outro dado sorteou o valor 3 e o jogador está carregando 3 tesouros,
então o jogador vai avançar somente uma casa.) Note que se o valor for negativo o jogador deve ficar parado.
Esse passo se aplica tanto para avançar para o fundo do mar quanto para retornar para o submarino.


Caça ao tesouro: 
Neste passo o jogador pode fazer uma busca por tesouros ou decidir soltar um dos tesouros que ele carrega.
(Obs.: Este passo pode ser realizado independente da direção que o mergulhador estiver indo.
Então se o mergulhador estiver retornando para o submarino ele pode vasculhar a área em busca de tesouros.)
Se o mergulhador decidir soltar um tesouro, ele pode escolher qual tesouro deve ser descartado. Note que se o mergulhador estiver retornando ao submarino ele não pode soltar o tesouro se for o único que ele carrega.
Se o mergulhador decidir vasculhar a área:
O jogo deve informar o valor da recompensa. O valor da recompensa é um número aleatório que depende da profundidade do mar em que o mergulhar se encontra.
O jogador decide se ele deseja ficar ou não com o tesouro. Note que o jogador só pode carregar no máximo 4 tesouros. Então se ele já estiver com 4 tesouros, o jogador escolhe qual tesouro deve ser descartado.
O jogo acaba quando o mergulhador voltar para o submarino ou se o oxigênio do tanque se esgotar. O mergulhador só receberá a recompensa dos tesouros se conseguir voltar para o submarino. Caso o oxigênio se esgote antes do mergulhador chegar ao submarino os tesouros serão perdidos e os pontos não são computados.

Oxigênio
O jogo começa com o oxigênio cheio, marcando o nível em 25. Conforme o jogo avança, o nível do oxigênio irá reduzindo conforme as ações do jogador. Se o nível de oxigênio alcançar o valor 0 o jogador da vez termina a rodada e o jogo acaba.

Profundidade
A profundidade máxima que o mergulhador pode alcançar em direção ao fundo do mar é representada pelo valor 32. Onde a profundidade de nível 1 representa a profundidade mais próxima do submarino e a profundidade de nível 32 representa a profundidade mais distante do submarino. E a posição de valor 0 representa o submarino.

Tesouro
O valor da recompensa de cada tesouro varia de acordo com o nível de profundidade em que o tesouro se encontra

Entendeu tudo? Agora é seguir em frente e se divertir.

                """
            )
        elif escolha == 'n':

            sSlow = '\nPois bem, que comece a jornada. '
            slowprint(sSlow)
            
        else:

            sSlow = '\nOpa, não entendi, tente novamente. '
            slowprint(sSlow)
            mantem_while = True

## Função de respirar que apresenta o nivel de oxigenio, realiza o decremento conforme a quantidade de Tesouros
def respirar(nivelOxigenio, quantidadeTesouros):

    mantem_while = True
    while mantem_while:
        mantem_while = False

        sSlow = '\nEtapa atual: Respiração\nPressione enter para continuar '
        slowprint(sSlow)
        continuar = input()
        if continuar == '':

            sSlow = f'\nO nível de oxigênio está em {nivelOxigenio}.'
            slowprint(sSlow)
            
            sSlow = f'A quantidade de tesouros que você carrega no momento é de {quantidadeTesouros}.'
            slowprint(sSlow)

            sSlow = f'O novo nível de oxigênio é: {nivelOxigenio} - {quantidadeTesouros} = {nivelOxigenio-quantidadeTesouros}.\n'
            slowprint(sSlow)

            nivelOxigenio = nivelOxigenio-quantidadeTesouros
            return nivelOxigenio
        else:

            sSlow = '\nEntrada inválida, retornaremos para o ponto anterior, por favor digite enter e nada mais.'
            slowprint(sSlow)

            mantem_while = True

## Função para escolher o sentido do movimento que o jogador apresenta. 
def avancarOuRetroceder(quantidadeTesouros):

    if quantidadeTesouros > 0:
        mantem_while = True
        while mantem_while:
            mantem_while = False

            sSlow = '\nVocê deseja (a)Avançar ou (r)retroceder? '
            slowprint(sSlow)
            escolha = input()

            if escolha == 'a':

                sSlow = '\nVocê escolheu avançar em direção ao fundo do mar. Cuidado com a pressão!'
                slowprint(sSlow)
            
                return 'avancar'

            elif escolha == 'r':

                sSlow = '\nVocê escolheu retroceder e voltar para o submarino.\nAvance para chegar antes de acabar o oxigênio.'
                slowprint(sSlow)

                return 'retroceder'
    
            else:

                sSlow = '\nEntrada inválida. As opções serão mostradas novamente. Por Favor escolher uma opção válida.'
                slowprint(sSlow)
                
                mantem_while = True
    else: 
        return 'avancar'

## Função de nadar que retorna a quantidade de passos que o jogador dará
def nadar(quantidadeTesouros):

    mantem_while = True
    while mantem_while:
        mantem_while = False

        sSlow = '\nEtapa atual: Nadar\nPressione enter para continuar'
        slowprint(sSlow)
        continuar = input()

        if continuar == '':

            d1 = randint(1,3)
            d2 = randint(1,3)
            sSlow = f'\nOs dados foram lançados e o resultado foi... D1 = {d1} e D2 = {d2}.'
            slowprint(sSlow)
        
            passos = (d1 + d2) - quantidadeTesouros
            if passos > 0:

                sSlow = f'\nÓtimo, você dará {passos} passos nessa rodada.'
                slowprint(sSlow)
                return passos
            else:

                sSlow = f'\nInfelizmente você não dará nenhum passo nessa rodada'
                slowprint(sSlow)
                return 0

        else:
            sSlow = '\nEntrada inválida, retornaremos para o ponto anterior, por favor digite enter e nada mais.'
            slowprint(sSlow)
            mantem_while = True

## Função de caçar tesouros, responsavel por retornar a lista de tesouros atualizada
## A função permite que o user escolha entre  vasculhar um tesouro ou abandonar
def cacaAoTesouro(quantidadeTesouros, nivelDeProfundidade, listaTesouros, jogadorEstaAvancando):
    mantem_while = True
    while mantem_while:
        mantem_while = False

        sSlow = '\nEtapa atual: Tesouros\nVocê deseja vasculhar o mar em busca de um novo tesouro ou abandonar um tesouro? (v) Vasculhar ou (s) Soltar: '
        slowprint(sSlow)
        escolha = input()

        if escolha == 'v':
            if quantidadeTesouros == 4:

                sSlow = '\nVocê é um tanto ambicioso não?\nComo o limite de tesouros é de 4, você não pode vasculhar novos tesouros a menos que abandone um deles.'
                slowprint(sSlow)
                
                resultadoDeVasculhar = vasculhar(nivelDeProfundidade, listaTesouros)
                if resultadoDeVasculhar == 'nao ficou com o tesouro':
                    return listaTesouros
                else:
                    listaTesouros.append(resultadoDeVasculhar)
                    return soltar(listaTesouros, jogadorEstaAvancando)

            else:

                sSlow = '\nVasculhar o mar em busca de tesouros, certo? Então vasculhas.'
                slowprint(sSlow)

                resultadoDeVasculhar = vasculhar(nivelDeProfundidade, listaTesouros)
                if resultadoDeVasculhar == 'nao ficou com o tesouro':
                    return listaTesouros
                else:
                    listaTesouros.append(resultadoDeVasculhar)
                    return listaTesouros

        elif escolha == 's':
            return soltar(listaTesouros, jogadorEstaAvancando)

        else:

            sSlow = '\nEntrada inválida, retornaremos para o ponto anterior, por favor digite "v" ou "s".'
            slowprint(sSlow)
            mantem_while = True

## Função auxiliar de "vasculhar" que retorna o valor que o tesouro vale, levando em conta a regra de negocio
## que os tesouros valem um certo valor (aleatorio) a depender do nivel de profundidade que se encontra o 
## jogador.
def retornaValorDoTesouro(nivelDeProfundidade):

    if((nivelDeProfundidade > 0) and (nivelDeProfundidade <= 8)):
        valorTesouro = randint(0, 3)

    elif((nivelDeProfundidade > 8) and (nivelDeProfundidade <= 16)):
        valorTesouro = randint(4, 7)

    elif((nivelDeProfundidade > 16) and (nivelDeProfundidade <= 24)):
        valorTesouro = randint(8, 11)

    elif((nivelDeProfundidade > 24) and (nivelDeProfundidade <= 32)):
        valorTesouro = randint(12, 15)

    else:
        raise Exception(f"A função retornaValorDoTesouro apresenta um valor inválido, verifique o erro e tente novamente.\nO valor de nivel de profundidade recebido foi: {nivelDeProfundidade}")
    return valorTesouro

## Função vasculhar, auxiliar da função cacaAoTesouro, responsavel pelo aumento de tesouros do jogador
## a função deve retorna o valor do novo Tesouro ou a string "nao ficou com o tesouro" que é usada para validacao posterior
def vasculhar(nivelDeProfundidade, listaTesouros):
    mantem_while = True
    while mantem_while:
        mantem_while = False

        sSlow = '\nVasculhemos o mar em busca de tesouros então. Selecione enter para vasculhar um tesouro. '
        slowprint(sSlow)

        continuar = input()
        if continuar == '':
            valorDoTesouro = retornaValorDoTesouro(nivelDeProfundidade)
            #print('Mas antes, relembre o que já tens antes de almejar o novo:')
            apresentarTesouros(listaTesouros)
            mantem_while2 = True
            while mantem_while2:

                sSlow = f'\nVocê vasculhou o mar e encontrou um tesouro que vale {valorDoTesouro}.\nDeseja ficar com ele? (s) Sim ou (n) Não. '
                slowprint(sSlow)

                escolha = input()
                mantem_while2 = False
                if escolha == 's':
                    return valorDoTesouro
                elif escolha == 'n':
                    return 'nao ficou com o tesouro'
                else:

                    sSlow = '\nO mar não é lugar para indecisão camarada. Sim ou não, só precisamos disso. Vamos tentar novamente.'
                    slowprint(sSlow)
                    
                    mantem_while2 = True
        else:

            sSlow = '\nEi, não é assim que se vasculha o mar! Retornaremos para o ponto anterior, por favor digite enter e nada mais.'
            slowprint(sSlow)

            mantem_while = True

## Função para apresentar os tesouros que o jogador já conquistou
def apresentarTesouros(listaTesouros):

    sSlow = '\nA lista com seus tesouros atuais e as respectivas pontuações são: '
    slowprint(sSlow)
    
    if len(listaTesouros) == 0:

        sSlow = '\nOpa, não tens tesouros ainda. Vasculhe para ter tesouros.'
        slowprint(sSlow)
        
    else:
        for i in range(len(listaTesouros)):

            sSlow = f'Tesouro {i+1} vale {listaTesouros[i]}.'
            slowprint(sSlow)

## Função auxiliar de soltar criada posteriormente para reaproveitar código
## ela realiza o processo de deleção da lista tesouros. Retorna a lista de tesouros atualizada a ser utilizada 
## posteriormente na função cacaAoTesouro
def soltarAuxiliar(listaTesouros):

    sSlow = '\nConhecer seus limites é parte de uma trajétoria de sucesso.\nPois bem camarada qual tesouro você gostaria de soltar?'
    slowprint(sSlow)
    
    mantem_while = True
    apresentarTesouros(listaTesouros)
    while mantem_while:
        
        if len(listaTesouros) > 0:
            mantem_while =  False

            sSlow = '\nDigite o número correspondente ao tesouro que deseja soltar: '
            slowprint(sSlow)
            escolha = int(input())

            if ((escolha>0) and (escolha<=5)) and (isinstance(listaTesouros[escolha-1], int)):

                sSlow = f'\nO tesouro {escolha} será lançado ao mar.'
                slowprint(sSlow)
                
                del listaTesouros[escolha-1]
                return listaTesouros
            else:

                sSlow = '\nIhh, parece que alguém está delirando, você não tem tantos tesouros quanto pensa.\nTente novamente e dessa vez sem alucinações.'
                slowprint(sSlow)
                
                mantem_while = True
        else:
            return listaTesouros

## Função de soltar um tesouro que retorna a lista de tesouros atualizada na função cacaAoTesouro
def soltar(listaTesouros, jogadorEstaAvancando):
    if jogadorEstaAvancando:
        return soltarAuxiliar(listaTesouros)
    else:
        if len(listaTesouros) > 1:
           return soltarAuxiliar(listaTesouros)
        else:

            sSlow = 'Epa, cadê sua ambição camarada? Não podes voltar de mãos vazias.\nTraz esse teu tesouro a custo de tua vida se necessário.'
            slowprint(sSlow)
        
            return listaTesouros

## Retorna os dados do jogador atualizados
def status(nivelOxigenio, profundidade, listaTesouros, index_jogador):

    sSlow = f'\nStatus do jogador {index_jogador}:'
    slowprint(sSlow)
    
    sSlow = f'Nivel de oxigênio atual {nivelOxigenio}'
    slowprint(sSlow)
    
    sSlow = f'Nivel de profundidade atual {profundidade}\n'
    slowprint(sSlow)
    
    apresentarTesouros(listaTesouros)


def faltouOxigenio():
    
    sSlow = '\nÉ camarada, você não é peixe nem aquaman. Sem oxigênio não rola.\nInfelizmente você não conseguiu pontuar dessa vez.'
    slowprint(sSlow)

## Apresenta a pontuação do total do jogador
def finalizarJogo(listaTesouros):
    somaPontuacao = sum(listaTesouros)

    sSlow = f'\nParabéns camarada! Você alcançou o submarino com sucesso.\nSua pontuação foi de {somaPontuacao}.'
    slowprint(sSlow)

    return somaPontuacao