from random import randrange #importa a função de números aleatórios para o oponente.
import time #importa a função de espera para o console.

boardRows = [ #lista que compôes os espaços do tabuleiro.
    [1, 2, 3],
    [4, "X", 6],
    [7, 8, 9]
] #fim da lista.
def board(): #função que imprime o tabuleiro no console.
    print("+---------+---------+---------+")
    print("|         |         |         |")
    print("|   ", boardRows[0][0], "   |   ",boardRows[0][1], "   |   ", boardRows[0][2], "   |")
    print("|         |         |         |")
    print("+---------+---------+---------+")
    print("|         |         |         |")
    print("|   ", boardRows[1][0], "   |   ", boardRows[1][1], "   |   ", boardRows[1][2], "   |")
    print("|         |         |         |")
    print("+---------+---------+---------+")
    print("|         |         |         |")
    print("|   ", boardRows[2][0], "   |   ", boardRows[2][1], "   |   ", boardRows[2][2], "   |")
    print("|         |         |         |")
    print("+---------+---------+---------+") #fim da função de tabuleiro.

def move(location): #função que faz a ação de escolha do jogador ou oponente.
    global x, y

    # counter = 0
    # for i in boardRows:
    #     for j in boardRows:
    #         if j == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
    #             counter += 1
    # if counter <= 0:
    #     stop = True
    # else: stop = False

    if location == 1: #sequência de IFs para determinar a posição escolhida no tabuleiro.
        x, y = 0, 0
    elif location == 2:
        x, y = 0, 1
    elif location == 3:
        x, y = 0, 2
    elif location == 4:
        x, y = 1, 0
    elif location == 5:
        x, y = 1, 1
    elif location == 6:
        x, y = 1, 2
    elif location == 7:
        x, y = 2, 0
    elif location == 8:
        x, y = 2, 1
    elif location == 9:
        x, y = 2, 2
    else:
        x, y = 15, 15

    return x, y #retorna os valores para da index escolhida para a lista.
    #fim da função de escolha.

def check(): #função que verifica o estado do jogo entre vitória, derrota e próxima jogada.
    global gameState

    if ((boardRows[0][0] == "X" and boardRows[0][1] == "X" and boardRows[0][2] == "X")
        or (boardRows[1][0] == "X" and boardRows[1][1] == "X" and boardRows[1][2] == "X")
        or (boardRows[2][0] == "X" and boardRows[2][1] == "X" and boardRows[2][2] == "X")
        or (boardRows[0][0] == "X" and boardRows[1][0] == "X" and boardRows[2][0] == "X")
        or (boardRows[0][1] == "X" and boardRows[1][1] == "X" and boardRows[2][1] == "X")
        or (boardRows[0][2] == "X" and boardRows[1][2] == "X" and boardRows[2][2] == "X")
        or (boardRows[0][0] == "X" and boardRows[1][1] == "X" and boardRows[2][2] == "X")
        or (boardRows[0][2] == "X" and boardRows[1][1] == "X" and boardRows[2][0] == "X")
        ):
        gameState = "Loss" #o jogador perdeu.
        return gameState
    elif ((boardRows[0][0] == "O" and boardRows[0][1] == "O" and boardRows[0][2] == "O")
        or (boardRows[1][0] == "O" and boardRows[1][1] == "O" and boardRows[1][2] == "O")
        or (boardRows[2][0] == "O" and boardRows[2][1] == "O" and boardRows[2][2] == "O")
        or (boardRows[0][0] == "O" and boardRows[1][0] == "O" and boardRows[2][0] == "O")
        or (boardRows[0][1] == "O" and boardRows[1][1] == "O" and boardRows[2][1] == "O")
        or (boardRows[0][2] == "O" and boardRows[1][2] == "O" and boardRows[2][2] == "O")
        or (boardRows[0][0] == "O" and boardRows[1][1] == "O" and boardRows[2][2] == "O")
        or (boardRows[0][2] == "O" and boardRows[1][1] == "O" and boardRows[2][0] == "O")
        ):
        gameState = "Win" #o jogador ganhou.
        return gameState
    else:
        gameState = "Seu turno" #nem um nem outro resultado, o jogo continua.
        return gameState #fim da função de verificação.

playerWin = 0 #variáveis que fazer a tabela de pontos
botWin = 0
draw = 0

while True: #laço de repetição do programa executável

    print("Seu oponente começa o jogo.") #início do programa. O bot sempre começa marcando o meio do tabuleiro.
    time.sleep(3)
    board() #mostra o tabuleiro pela primeira vez.
    print("Agora é seu turno.") #indica o primeiro input do usuário.
    count = 4 #variável de controle para empatar o jogo se não tiver espaço disponível.

    while True: #laço de repetição para manter o programa rodando.
        while True: #laço de repetição para a escolha do jogador.
            try:
                location = int(input("Escolha o espaço desejado >> ")) #aceita número de 1 a 9
                move(location) #primeiro chamado da função de escolha de espaço.
            except ValueError: #verifica se o jogador escolheu algo além de inteiros.
                print("O valor escolhido não é válido. Tente números inteiros de 1 a 9")
                continue

                #print("Este espaço não existe!! Tente números inteiros de 1 a 9")

            try: #verifica se o espaço escolhido está dentro do escopo do tabuleiro.
                if boardRows[x][y] == "X": #sequência de IFs para verificar a disponibilidade do espaço escolhido.
                    print("Espaço ocupado!!")
                elif boardRows[x][y] == "O":
                    print("Espaço ocupado!!")
                else:
                    boardRows[x][y] = "O"
                    board()
                    break
            except IndexError:
                print("Este espaço não existe!! Tente números inteiros de 1 a 9")
                continue

        if check() == "Win": #verifica se o jogador marcou uma sequência.
            print("Parabéns, você ganhou!!")
            playerWin += 1
            break

        print("O turno é do oponente")
        time.sleep(3)

        while True: #turno do oponente onde o espaço será escolhido aleatóriamente.
            pc_move = randrange(1,10) #variável que determina a escolha do oponente.
            move(pc_move)

            if boardRows[x][y] == "X":  # sequência de IFs para verificar a disponibilidade do espaço escolhido.
                continue
            elif boardRows[x][y] == "O":
                continue
            else:
                print("O oponente escolheu: ", pc_move)
                boardRows[x][y] = "X"
                board()
                break

        if check() == "Loss": #verifica se o oponente marcou uma sequência.
            print("Desculpe, você perdeu.")
            botWin += 1
            break
        else:
            print(check()) #o jogo pode continuar

        count -= 1 #controla o número de rodadas restantes.
        if count <= 0: #verifica se o jogo pode continuar.
            print("Sem espaços livres. Empate!!")
            draw += 1
            break

    print("O Placar está:\n"
          "Seu total de vitórias:", playerWin, "\n"
          "Vitórias do oponente:", botWin, "\n"
          "O Total de empates:", draw, "\n"
          "Jogue outra partida!!") #mensagem de fim de jogo.

    while True:
        playAgain = input("Gostaria de jogar novamente? \n Escolha 'S' ou 'N' >>").upper()
        if playAgain == 'S' or playAgain == 'N':
            break
        print("Desculpe, valor inválido")

    if playAgain == 'S': #continua o loop de jogo.
        boardRows = [ #retorna o tabuleiro ao estado original.
            [1, 2, 3],
            [4, "X", 6],
            [7, 8, 9]
        ]
        continue
    elif playAgain == 'N': #encerra o loop de jogo e termina o programa.
        print("Fim de jogo!") #mensagem de fim do programa.
        break