from fastapi import FastAPI
from pydantic import BaseModel
from similarity import get_similarity, score_to_rank

app = FastAPI()
DAILY_WORD = "king"

class GuessRequest(BaseModel):
    word: str

@app.post("/api/guess")
def guess(data: GuessRequest):
    word = data.word.lower()        
    score = get_similarity(DAILY_WORD, word)
    rank = score_to_rank(score)
    return {"score": score, "rank": rank}