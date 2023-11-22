import random

# Mostra o ganhador da partida.
def ganhador(jogador_1, jogador_2):
    jogadas_possiveis = [['Empate!','Jogador 1','Jogador 2'],
                         ['Jogador 2','Empate!','Jogador 1'],
                         ['Jogador 1','Jogador 2','Empate!']]

    ganhador = jogadas_possiveis[jogador_2][jogador_1]
    
    return ganhador

# Guarda o resultado de cada partida em um dicionário.
def compila_partida(jogador_1, jogador_2):
    jogadas = { 
        0: "Pedra", 
        1: "Papel", 
        2: "Tesoura"
    }

    jogada_jogador_1 = jogadas.get(jogador_1)
    jogada_jogador_2 = jogadas.get(jogador_2)
    partida = {
        'jogador_1' : jogada_jogador_1, 
        'jogador_2' : jogada_jogador_2, 
        'ganhador' : ganhador(jogador_1, jogador_2)
    }

    return partida

# Imprime a jogada de cada jogador, e quem foi o vencedor de cada partida ou se foi empate.
def imprime_resultado_partida(partida):
    print(f"\n JOGADOR 1 JOGOU: {partida['jogador_1']} \
            \n JOGADOR 2 JOGOU: {partida['jogador_2']}")

    if partida['ganhador'] == 'Empate!':
        print('\n O RESULTADO DA PARTIDA É: EMPATE!')
    else:
        print(f"\n O GANHADOR DA PARTIDA É: {partida['ganhador']}")

# Imprime o placar geral.
def imprime_placar(ganhadores):
    print(f"\n _____PLACAR_____ \
            \n  - JOGADOR 1: {ganhadores.count('Jogador 1')}\
            \n  - JOGADOR 2: {ganhadores.count('Jogador 2')}\
            \n  - EMPATES:   {ganhadores.count('Empate!')}")