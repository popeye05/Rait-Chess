#Imports:
import os
from dotenv import load_dotenv
import chess
import chess.engine
from groq import Groq
#Loading env + creating board + opening engine
load_dotenv()
STOCKFISH_PATH = r"d:\stockfish\stockfish-windows-x86-64-avx2.exe"
#now activating this engine
engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)
#also created this client for the groq server
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

board = chess.Board()
board.push_san("e4")
board_string = str(board)
info = engine.analyse(board, chess.engine.Limit(time=0.5))
raw_score = info["score"].white().score()
print("Raw score:", raw_score)
best_move = board.san(info["pv"][0])

print("Best move (SAN):", best_move)
print(info)

#THis is the Step 3 part, Describe eval function
def describe_eval(raw_score):
    if(abs(raw_score) < 20 ):
        return "Roughly equal"
    elif(raw_score < 0 ):
        side = "Black"
    else:
        side = "White"
    if(abs(raw_score) < 100):
        return f"{side} has slight advantage"
    elif(abs(raw_score) < 300):
            return f"{side} has clear advantage"
    else:
         return f"{side} is completely winning"
    
#This is the last Part
prompt = f"I'm a RAIT CHESS, I'm an AI Chess coach talking to a beginner. In this position, the best move is {best_move}, and {describe_eval(raw_score)}. Explain in one encouraging sentence why {best_move} is a good move here, without mentioning centipawns, evaluations, or engine terminology."

#This is justt integrating the groq part, i did this in step 1
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="llama-3.3-70b-versatile",
)
print(chat_completion.choices[0].message.content)

#Phase 2 Completion marks here with quitting the ngine yaaaaahhhhhh
engine.quit()