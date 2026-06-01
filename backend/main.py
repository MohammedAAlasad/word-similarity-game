from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from similarity import get_similarity, score_to_rank
from database import get_daily_word , save_guess , init_db ,check_word , set_daily_word , clear_guesses

import random


app = FastAPI()
init_db()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class GuessRequest(BaseModel):
    word: str
    
WORD_LIST = ["ocean", "forest", "castle", "dragon", "river", 
             "mountain", "thunder", "silver", "garden", "winter"]

@app.on_event("startup")
def startup():
    init_db()
    if get_daily_word() is None:
        word = random.choice(WORD_LIST)
        clear_guesses()
        set_daily_word(word , overwrite=False)
        print(f"Today's word set to: {word}")

@app.post("/api/admin/set-word")
def set_word(data: dict):
    word = data["word"].lower()
    clear_guesses()
    set_daily_word(word, overwrite=True)
    return {"message": f"Daily word set to: {word}"}

@app.post("/api/guess")
def guess(data: GuessRequest):
    daily_word = get_daily_word()
    if daily_word is None:
        return {"error": "No word set for today"}

    user_word = data.word.lower()
    
    checked_score = check_word(user_word)
    if checked_score is not None:
        score = checked_score
        rank = score_to_rank(score)
        return {"score": score, "rank": rank}
    else:
        score = get_similarity(daily_word, user_word)
        rank = score_to_rank(score)
        save_guess(user_word,score)
        return {"score": score, "rank": rank}
