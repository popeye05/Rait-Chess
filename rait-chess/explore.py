#So, Here's a script, First I used the Python chess Library
import chess
import chess.engine

STOCKFISH_PATH = r"d:\stockfish\stockfish-windows-x86-64-avx2.exe"
#MAIN
'''
The python chess is not an engine, it just works for us, 
i.e. in simpler words it knows the UCI rules and can give inputs to Stockfish on behalf of us
whereas, this stockfiah is a C++ Engine.
'''
board = chess.Board()
print("\nStarting position:")
print(board)
print()
#popen: process open, i.e creates a process, within which the python chess handles it
engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)

info = engine.analyse(board, chess.engine.Limit(time=0.5))

print("Evaluation:", info["score"])
print("Best line (principal variation):", info["pv"])

result = engine.play(board, chess.engine.Limit(time=0.5))
print("Best move:", result.move)
#Finally Quit
engine.quit()

