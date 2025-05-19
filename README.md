# AI chess test, May 2025
## Motivation

I tried to play chess with ChatGPT in its UI, but it turned out to be problematic. ChatGPT does not carry the board's state; instead, it makes "story-based" deductions from the conversation history. It starts to alter position between moves and makes illegal moves around the 10th turn.

## Solution

I wrote a python code [ChatGpt_tests.py](./ChatGpt_tests.py) that carries the board between moves and makes stateless api requests to OpenAI. Only 2 most advanced models were able to survive without illegal moves and hallucinations until ~20+ turns, see [gpt-4.5-preview.pgn](./gpt-4.5-preview.pgn) and [reasoning model] [o3.pgn](./o3.pgn). Both models failed, eventually responding with a counter check while under a check.

## Brilliant Idea

I hoped to have a tournament between ChatGPT and Gemini via api calls, see [Tournament.py](./Tournament.py). However, it turned out that the two most advanced models of Gemini started making illegal moves at ~10th turn, see [gemini-2.5-flash-preview-04-17.pgn](./gemini-2.5-flash-preview-04-17.pgn) and [reasoning model] [gemini-2.5-pro-preview-05-06.pgn](./gemini-2.5-pro-preview-05-06.pgn). Gemini is too weak to compete against ChatGPT.

---

## Notes

* `pip install chess` and see documentation at <https://python-chess.readthedocs.io/en/latest/>
* **upload and view PGN files** using free online GUIs <https://www.chess.com/analysis>, <https://lichess.org/analysis>, or <https://www.openingtree.com> (some limited free **PGN analysis with AI explanations** is offered via <https://decodechess.com>)
* at chess.com one can play **other variants** of chess, such as, Chess960 (aka Fischer Random Chess, 1996), Suicide/Giveaway, Atomic, King of the Hill, Racing Kings, Horde, Three-check, Crazyhouse, **4-people versions**, and even **configure ones own chess variant**

Finally, the idea of bots playing chess was implemented, see hilarious [Chatbot Chess Championship 2025](https://www.youtube.com/playlist?list=PLBRObSmbZluRddpWxbM_r-vOQjVegIQJC) by GothamChess at YouTube (or this [article detailing the tournament](https://decrypt.co/301127/chatgpt-demolished-in-ai-chess-tournament)). ChatGPT succeeds in reaching the finals, only to lose to Stockfish. The drama centered on the fact that all AIs were allowed to hallucinate and make illegal moves, and the only chess engine, Stockfish, was abiding by the rules.


