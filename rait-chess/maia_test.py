import chess
import chess.engine
LC0_PATH = r"d:\Leela Chess Zero\lc0.exe"

#MAIN
'''AGain, Python Chess, is not an engine...
i.e. in simpler words it knows the UCI rules and can give inputs to Leela on behalf of us
whereas, leela zero, a ML Chess Engine, weree moving from then stockfish to lc0 due to our objective was making a
human like chess coach
'''
board = chess.Board()
print("\nStarting position:")
print(board)
print()
#popen: process open, i.e creates a process, within which the python chess handles it

engine = chess.engine.SimpleEngine.popen_uci(LC0_PATH)
engine.configure({"WeightsFile": r"D:\Leela Chess Zero\ckpt-40-400000.pb.gz"})
board = chess.Board()

info = engine.analyse(board, chess.engine.Limit(time=0.5))
print("Evaluation:", info["score"])
print("Best line (principal variation):", info["pv"])

maia_move = board.san(info["pv"][0])
print("Maia's predicted move:", maia_move)

engine.quit()