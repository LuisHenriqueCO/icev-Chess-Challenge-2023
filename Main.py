import chess
import random

def print_board(board):
    print("="*20)
    print(board)
    print("="*20)

def user_move(board):
    legal_moves = [move for move in board.legal_moves]
    while True:
        user_input = input("Faça seu movimento: ")
        try:
            move = chess.Move.from_uci(user_input)
            if move in legal_moves:
                return move
            else:
                print("Movimento inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Tente novamente.")

def second_user_move(board):
    legal_moves = [move for move in board.legal_moves]
    while True:
        second_user_input = input("Faça seu movimento: ")
        try:
            move = chess.Move.from_uci(second_user_input)
            if move in legal_moves:
                return move
            else:
                print("Movimento inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Tente novamente.")

def ai_move(board):
    legal_moves = [move for move in board.legal_moves]
    return random.choice(legal_moves)

def main():
    board = chess.Board()

    while True:
        print("Insira uma opção de acordo com que você deseja:")
        print("1 - Jogar contra outro jogador")
        print("2 - Jogar contra IA")
        print("3 - Duas IAs uma contra a outra")
        print("4 - Sair")
        choice = int(input("->"))

        if choice == 1:
            while not board.is_game_over():
                print_board(board)

                if board.turn == chess.WHITE:
                    move = user_move(board)
                else:
                    move = second_user_move(board)

                board.push(move)

        if choice == 2:

            print("Qual 'cor' deseja ser?")
            print("1 - Brancas (Letras Maiusculas)")
            print("2 - Pretas(Letras Minúsculas)")
            color = int(input("->"))
            if color == 1:

                while not board.is_game_over():
                    print_board(board)

                    if board.turn == chess.WHITE:
                        move = user_move(board)
                    else:
                        move = ai_move(board)
                        while True:
                            proxima_rodada_ia = input("Clique ENTER para a próxima jogada")
                            if(proxima_rodada_ia == ""):
                                break

                    board.push(move)
                    
            elif color == 2:

                while not board.is_game_over():
                    print_board(board)

                    if board.turn == chess.WHITE:
                        move = ai_move(board)
                        while True:
                            proxima_rodada_ia = input("Clique ENTER para a próxima jogada")
                            if(proxima_rodada_ia == ""):
                                break
                    else:
                        move = user_move(board)

                    board.push(move)

            print("Fim de jogo.")
            print("Resultado:", board.result())
            print("Registro de jogadas:")

        elif choice == 3:
             while not board.is_game_over():
                print_board(board)

                if board.turn == chess.WHITE:
                    move = ai_move(board)
                    while True:
                        proxima_rodada_ia = input("Clique ENTER para a próxima jogada")
                        if(proxima_rodada_ia == ""):
                            break
                else:
                    move = ai_move(board)
                    while True:
                        proxima_rodada_ia = input("Clique ENTER para a próxima jogada")
                        if(proxima_rodada_ia == ""):
                            break

                board.push(move)

                print("Fim de jogo.")
                print("Resultado:", board.result())

        elif choice == 4:
            break

        else:
            print("Opção Inválida")


if __name__ == "__main__":
    main()