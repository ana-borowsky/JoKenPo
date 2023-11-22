import sys
from functions import *

# A classe jogador humano traz um menu de jogadas possíveis, que pede que o usuário digite uma das teclas: 0, 1 ou 2, que representam pedra, papel e tesoura. 
# Enquanto o jogador não digitar uma destas opções, será mostrada a mensagem 'opção inválida', e não sairá do menu das jogadas.
class JogadorHumano:
    def joga(self):
        jogada = input(OPCOES_DE_JOGADA)
        while not(jogada == '0' or jogada == '1' or jogada == '2'):
            print('Opção inválida. Tente novamente.\n')
            jogada = input(OPCOES_DE_JOGADA)
        return int(jogada)

# A classe jogador computador gera a jogada a partir de uma escolha aleatória entre os números 0, 1 e 2, que representam pedra, papel e tesoura.
class JogadorComputador:
    def joga(self):
        return random.randint(0, 2)

continuar = True
partidas = []
ganhadores = []

# As constantes foram usadas para gerar menus esteticamente mais agradáveis, e evitar repetições no código.
MODALIDADE_DE_JOGO = "\n +--------------------------------+ \
                      \n |      ESCOLHA A MODALIDADE      | \
                      \n +--------------------------------+ \
                      \n | [ 1 ] HUMANO VS HUMANO         | \
                      \n | [ 2 ] HUMANO VS COMPUTADOR     | \
                      \n | [ 3 ] COMPUTADOR VS COMPUTADOR | \
                      \n +--------------------------------+ \n"
                      
CONTINUAR = "\n +-----------------+ \
             \n |    CONTINUAR    | \
             \n +-----------------+ \
             \n |  [ S ]    SIM   | \
             \n |  [ N ]    NÃO   | \
             \n +-----------------+ \n"

OPCOES_DE_JOGADA = '\n +--------------------+ \
                    \n | ESCOLHA SUA JOGADA | \
                    \n +--------------------+ \
                    \n |    [ 0 ] Pedra     | \
                    \n |    [ 1 ] Papel     | \
                    \n |    [ 2 ] Tesoura   | \
                    \n +--------------------+ \n '

# O resumo das partidas é uma tabela que é gerada ao fim do jogo, quando o usuário informa que não quer mais continuar a jogar, 
# que mostra todas as partidas, e quem venceu qual partida, ou se houve empate. 
CABECALHO_RESUMO_PARTIDAS = '\n \tRESUMO DAS PARTIDAS\t \
                             \n +--------------+--------------------+ \
                             \n \tPARTIDA\t|\tVENCEDOR\t \
                             \n +--------------+--------------------+'

# Ao iniciar o jogo, uma mensagem de boas vindas é impressa na tela, e em seguida, o menu com as opções de modalidade de jogo.
print("\n Boas vindas ao jogo Jo-Ken-Pô!")

opcao_jogo = input(MODALIDADE_DE_JOGO)

# As modalidades são: são humano vs humano, humano vs computador e computador vs computador, representadas no menu pelas opções
# 1, 2 e 3. Caso o usuário insira uma opção inválida, irá mostrar uma mensagem e encerrar o programa.
# Caso seja escolhida uma das opções válidas, uma nova instância das classes JogadorHumano e/ ou JogadorComputador serâo criadas
# e as partidas serão inicializadas.
if opcao_jogo == '1':
    j1 = JogadorHumano()
    j2 = JogadorHumano()
elif opcao_jogo == '2':
    j1 = JogadorHumano()
    j2 = JogadorComputador()
elif opcao_jogo == '3':
    j1 = JogadorComputador() 
    j2 = JogadorComputador()
else:
    print("\n Opção inválida \n")
    sys.exit() 

# Inicia o loop das partidas.
while continuar == True:
    # Chamará o método de jogar de cada tipo de jogador, conforme a modalidade escolhida.
    jogador_1 = j1.joga()
    jogador_2 = j2.joga()

    # Chama a função que irá mostrar que jogada cada jogador escolheu, e irá guardar essas informações, mais quem
    # foi o vencedor, ou se foi empate, e guardar isso em um dicionário.
    partida = compila_partida(jogador_1, jogador_2)

    # Adiciona cada nova partida e cada ganhador em um array específico.
    partidas.append(partida)
    ganhadores.append(partida['ganhador']) 

    # Chama a função que mostra na tela a jogada escolhida por cada jogador, e o ganhador (ou empate).
    imprime_resultado_partida(partida)

    # Chama a função que mostra o placar geral até o momento.
    imprime_placar(ganhadores)

    # Chama o menu que pergunta se o usuário quer continuar a jogar, ou encerrar o programa.
    opcao = (input(CONTINUAR)).upper()
    continuar = (opcao == 'S')

# Imprimirá o resumo das partidas na tela, mostrando quem foi o vencedor, ou se houve empate em cada partida.
print(CABECALHO_RESUMO_PARTIDAS)
for index, partida in enumerate(partidas):
    print(f"\t[{index + 1}]\t|\t{partida['ganhador']}\t")
print(' +--------------+--------------------+')

# Chama a função que imprime o placar geral.
imprime_placar(ganhadores)

# Imprime uma mensagem de despedida e o nome da aluna que desenvolveu o jogo.
print('\n Até mais! \n \n Desenvolvido por Ana Paula Borowsky de Borba.\n')