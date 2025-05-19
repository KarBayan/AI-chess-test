from enum import Enum
from openai import OpenAI
from dotenv import load_dotenv
import chess
import chess.pgn
import os

# Load environment variables from .env file
load_dotenv()

# Define an Enum for API key types
class APIType(Enum):
    OPENAI = "OpenAI"
    GOOGLE = "Gemini"

# Define AIConfig class to combine client creation and model
class AI:
    def __init__(self, key_type: APIType, model: str):
        self.model = model
        # Map key type to environment variable
        env_var_map = {
            APIType.OPENAI: "OPENAI_API_KEY",
            APIType.GOOGLE: "GEMINI_API_KEY"
        }
        # Get API key from environment based on key_type
        api_key = os.getenv(env_var_map[key_type])
        if not api_key:
            raise ValueError(f"Environment variable {env_var_map[key_type]} not set")
       
        if APIType.GOOGLE == key_type:
            self.client = OpenAI(
                api_key=api_key,
                base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
            )
        else:
            self.client = OpenAI(api_key=api_key)


# Function that handles a chat turn
def get_gpt_move(ai_config, board):
    gpt_move = None
    fen = board.fen()

    try:
        response = ai_config.client.chat.completions.create(
            model=ai_config.model,
            messages=[
                {
                    "role": "system",
                    "content": "You're in a chess competition. "
                               "Given a FEN, reply with the best move in algebraic notation only. "
                               "Just respond with the move notation — no explanation, no commentary, no extra text."
                },
                {
                    "role": "user",
                    "content": fen
                }
            ],
            #use default temperature 1 for balanced "creative" response
            temperature=0  # Ensure deterministic output
        )
        gpt_move = response.choices[0].message.content.strip()
    except Exception as e:
        print("Error during response: ", e)

    return gpt_move

# --- Main program ---
def main():
    # Define models
    model1 = AI(key_type=APIType.OPENAI, model="gpt-4.1-nano")
    model2 = AI(key_type=APIType.GOOGLE, model="gemini-2.5-pro-preview-05-06")        
    model2 = AI(key_type=APIType.GOOGLE, model="gemini-2.5-flash-preview-04-17")    

    gpt_white = model2
    gpt_black = model2

    # Initialize chess board
    board = chess.Board()
    game = chess.pgn.Game()
    game.setup(board)
    node = game    

    # Play game
    while not board.is_game_over():
        print(board)
        move = chess.Move.null()

        current_config = gpt_white if board.turn == chess.WHITE else gpt_black
        gpt_move = get_gpt_move(current_config, board)
        print(f"{current_config.model}'s move: {gpt_move}")
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
    with open(f"{current_config.model}.pgn", "w") as pgn_file:
        print(game, file=pgn_file)

if __name__ == "__main__":
    main()
    print("The End")