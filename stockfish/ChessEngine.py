import sys
sys.path.insert(0, './')
from stockfishEngine import Stockfish


stockfish = Stockfish("C:\\Users\\janni\\Desktop\\stockfish_20090216_x64.exe",
                      parameters={'Threads': 16,
                                  'Write Debug Log': True})

print(stockfish.get_parameters())

i = 0
moves = [stockfish.get_best_move()]
while i < 50:
    stockfish.set_position(moves)
    moves.append(stockfish.get_best_move())
    print(stockfish.get_board_visual())
    print(stockfish.get_fen_position())
    print(stockfish.get_stockfish_evaluation())
    i += 1