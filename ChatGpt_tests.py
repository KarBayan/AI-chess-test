from openai import OpenAI
from dotenv import load_dotenv

import chess
import chess.pgn
import os

# Load environment variables from .env file
load_dotenv()

# Function that handles a chat turn
def get_gpt_move(client, model, board):

    gpt_move = None
    fen = board.fen()

    try:
        response = client.responses.create(
            model=model,
            instructions="You're in a chess competition. "
                         "Given a FEN, reply with the best move in algebraic notation only. "
                         "Just respond with the move notation — no explanation, no commentary, no extra text.",
            input=fen,
            store=False  # No memory on the backend
        )
        gpt_move = response.output_text.strip()
    except Exception as e:
        print("Error during response: ", e)

    return gpt_move

# --- Main program ---
def main():
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    # #get models that are allowed for me
    # models = client.models.list()
    # for model in models.data:
    #     print(model.id)

    # --- quick failures test
    gpt = "gpt-4.1-nano"
    # --- success
    #gpt = "o3"            
    #gpt = "gpt-4.5-preview"        

    gpt_white = gpt
    gpt_black = gpt

    # Initialize chess board
    board = chess.Board()
    game = chess.pgn.Game()
    game.setup(board)
    node = game    

    # Play game
    while not board.is_game_over():
        print(board)
        move = chess.Move.null()

        current_model = gpt_white if board.turn == chess.WHITE else gpt_black
        gpt_move = get_gpt_move(client, current_model, board)
        print(f"{current_model}'s move: {gpt_move}")
        try:
            move = board.parse_san(gpt_move)
        except ValueError:
            print("Move is illegal and/or unable to parse!")            
            break

        move = board.push_san(gpt_move)
        node = node.add_variation(move)

        if board.is_game_over():
            break

    # Game over
    print("Game over!")
    print(board.result())

    # Write PGN to file
    with open(f"{current_model}.pgn", "w") as pgn_file:
        print(game, file=pgn_file)

if __name__ == "__main__":
    main()
    print("The End")