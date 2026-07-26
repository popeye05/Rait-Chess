#Imports:
import os
from dotenv import load_dotenv
import chess
import chess.engine
from groq import Groq
#Loading env + creating board + opening engine
load_dotenv()
#1st the Stockfish
STOCKFISH_PATH = r"d:\stockfish\stockfish-windows-x86-64-avx2.exe"
#Now This is The MAIA one w/ LC0
LC0_PATH = r"d:\Leela Chess Zero\lc0.exe"
MAIA_WEIGHTS = r"D:\Leela Chess Zero\ckpt-40-400000.pb.gz"


#now activating this engine
stockfish_engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)
#Now MAIA
maia_engine = chess.engine.SimpleEngine.popen_uci(LC0_PATH)
maia_engine.configure({"WeightsFile": MAIA_WEIGHTS})


#also created this client for the groq server
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

board = chess.Board()
board.push_san("e4")
board_string = str(board)
info = stockfish_engine.analyse(board, chess.engine.Limit(time=0.5))
maia_info = maia_engine.analyse(board, chess.engine.Limit(time=0.5))

raw_score = info["score"].white().score()
print("Raw score:", raw_score)
best_move = board.san(info["pv"][0])
#MAIA move here
maia_move = board.san(maia_info["pv"][0])
print("Maia's predicted move:", maia_move)
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
    

#This is the Phase 3 Part:
user_move = "d5"
def compare_move():
     if user_move == best_move and maia_move == best_move:
        return f"You've Chosen The Ideal Move"
     elif user_move == best_move and maia_move != best_move:
        return f"You've Chosen The Best Move"
     elif user_move == maia_move and maia_move != best_move:
        return f"Good Move,Typical Human Move"
     elif user_move != maia_move and user_move!= best_move and maia_move != best_move:
        return f"Understandable Miss, No Worries"
     elif user_move != maia_move and user_move!= best_move and maia_move == best_move:
        return f"Learnable Mistake"
     else:
         return f"Error Occured"
#Now we use the function to compare(Phase 3 part)
comparison_result = compare_move()
print("Comparison result:", comparison_result)

#final Prompt part, below is the previous one, before adding MAIA
#prompt = f"I'm a RAIT CHESS, I'm an AI Chess coach talking to a beginner. In this position, the best move is {best_move}, and {describe_eval(raw_score)}. Explain in one encouraging sentence why {best_move} is a good move here, without mentioning centipawns, evaluations, or engine terminology."
prompt = f"I'm RAIT CHESS, an AI chess coach talking to a beginner. In this position, the best move is {best_move}, and {describe_eval(raw_score)}. The player played {user_move}. {comparison_result}. Explain in one or two encouraging sentences, referencing this specific situation, without mentioning centipawns, evaluations, or engine terminology."

#This is the last Part
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
stockfish_engine.quit()
#Time to Quit the MAIA engine too!
maia_engine.quit()
# So Adding the MAIA, i.e Updating the entire stockfish coach test file with lc0 and maia was a part of phase 3
