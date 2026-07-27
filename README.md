#  Rait Chess
 
**An AI chess coach that feels human — not just optimal.**
 
Most "AI chess coaches" are just a chess engine wrapped in a chat box: they tell you the objectively best move and an evaluation number. That's not coaching. Rait Chess is built around a different idea — a coach that reasons about what a player at *your* skill level would realistically see or miss, and explains moves the way a real coach would: in plain chess language, not centipawns.
 
---
## Screenshots
![Homepage](RC_Screenshots/homepage.png)
 
## Basially What Happens is:
 
A raw chess engine answers one question: *"what's the objectively best move?"*
A real coach answers a different, more useful question: *"what should **you** have seen here, and why?"*
 
Rait Chess is built around three specialized systems, each doing one job well, instead of one model trying to do everything:

 1. STOCKFISH : Thsi is a CPP Chess Engine which provides Best Moves
 2. MAIA: Neural Netwrk Weights
 3. LC0: Actual Chess Engine which works on ML, and thats what we use and compare with
 
By comparing what the **user** played against what **Maia** predicts a human would play and what **Stockfish** says is objectively best, Rait Chess can tell the difference between:
## **Flow for every move:**
1. User drags a piece on the board (frontend)
2. The pre-move position (FEN) + the move (SAN) are sent to `/analyze-move`
3. Backend validates the move is actually legal
4. **Stockfish** evaluates the position and finds the objectively best move
5. **Maia** predicts what a human at a given skill level would likely play
6. The backend compares: user's move vs. Maia's prediction vs. Stockfish's best move
7. That comparison is turned into a prompt and sent to an **LLM**, which generates natural-language coaching — grounded in chess concepts (center control, piece development, king safety), never in raw evaluation numbers
8. The response is displayed back on the frontend
