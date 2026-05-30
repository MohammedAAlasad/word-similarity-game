from fastapi import FastAPI
from pydantic import BaseModel
from similarity import get_similarity, score_to_rank
from database import get_daily_word , save_guess , init_db ,check_word
from fastapi.middleware.cors import CORSMiddleware

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

@app.post("/api/guess")
def guess(data: GuessRequest):
    daily_word = get_daily_word()
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
