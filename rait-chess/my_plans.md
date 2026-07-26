# Phase 1-3
## First I did everything with Stockfish
1.  Built the explore.py
2.  Then Read the docs of Groq API, and done the setup for llm test
3.  Then Built the Coach_test.py using Python Chess docs and the Groq Docs. This was real Time consuming, Did the entire coding on own, except Claude helped me in debugging , But everything was hardcoded
4.  Then finally tested

## Second , After testing with Stockfish, It was time to test with MAIA and LC0
1.  So again Built the maia_test.py
2.  Then Updated the Coach_test.py using Python Chess docs and the Groq Docs. Again hardcoded, only few helps in debugging was taken
4.  Then finally tested

## This is A Decision Tree (by Claude) which Helped Me:

1.  First check: does Maia's move == Stockfish's move? (Establishes whether there's a "human-findable best move" at all)
2.  Then check: does the user's move match that (shared) move? If yes → straightforward praise
3.  If Maia and Stockfish disagree with each other, and user matches Maia → also good, they played the human move
4.  If user matches neither, and Maia/Stockfish agreed with each other → this is your clearest "real, learnable mistake" case
5.  If user matches neither, and Maia/Stockfish also disagreed with each other → gentler tone, since even the "human standard" move wasn't obvious

## Adding the function get coaching feedback
This replaced the test moves with the actual ones, and thats it, and now I'll move to the next step, which is nothing but the Phase 4

# Phase 4: FastAPI
Ok, This was a little hard step, and a lot of things was unknown so I had to take the help of Claude, But thats sill me coding almost 80% of it... But Yeah.. took the help, and did it!
1. Imorted  FastAPI , with the obv boilerplate
2. Then referred the port to the backend, i.e. coach_test
3. Then in this phase i added the exception handling as well
4. finally The backend was run and also using /docs and POST method I Checked all the possibilities as well!
5. Finally all tests were donene

# Phase 5: Frontend(React)
### The One Part, in which Claude helped me the most, because idk React , because idk js at all
This is almost 70% AI Coded, because I am not interested in the frontend at all...
so its less ineresting for me, and here actually I used AI