import chess
import chess.engine

STOCKFISH_PATH = r"d:\stockfish\stockfish-windows-x86-64-avx2.exe"
#MAIN

board = chess.Board()
print("\nStarting position:")
print(board)
print()

engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)

info = engine.analyse(board, chess.engine.Limit(time=0.5))

print("Evaluation:", info["score"])
print("Best line (principal variation):", info["pv"])

result = engine.play(board, chess.engine.Limit(time=0.5))
print("Best move:", result.move)

engine.quit()

