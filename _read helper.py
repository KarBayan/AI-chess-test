import chess
import chess.pgn
import os

# Initialize chess board
board = chess.Board()
game = chess.pgn.Game()
game.setup(board)
node = game    

move = chess.Move.null()

with open("o3.txt", 'r') as file:
    counter = 0
    for line in file:
        counter += 1
        #print(f"Reading line: {line}")  # Debug print
        if counter % 9 == 0 :
            result = line.split("o3's move: ")
            san = result[1].strip()
            print(san)
            move = board.push_san(san)
            node = node.add_variation(move)

# Write PGN to file
with open("o3 vs o3.pgn", "w") as pgn_file:
    print(game, file=pgn_file)
