import os
from dotenv import load_dotenv
load_dotenv()
from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "I'm a chess coach. A player just played the move e4 as White. Explain in one encouraging sentence why this is a solid opening move, without mentioning centipawns or engine evaluations.",
        }
    ],
    model="llama-3.3-70b-versatile",
)

print(chat_completion.choices[0].message.content)