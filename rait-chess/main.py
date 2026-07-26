from fastapi import FastAPI
from coach_test import get_coaching_feedback, stockfish_engine, maia_engine, client #i.e using the coach_test.py here for the functions we've built!!!

#Now the actual part:
from pydantic import BaseModel
class MoveRequest(BaseModel):
    fen: str
    user_move: str

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Rait Chess backend is running"}
@app.post("/analyze-move")
def analyze_move(request: MoveRequest):
    result = get_coaching_feedback(request.fen, request.user_move, stockfish_engine, maia_engine, client)
    return {"coaching": result}