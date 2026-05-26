from fastapi import FastAPI 
from similarity import get_similarity, score_to_rank

app = FastAPI() 
DailyWord = "king"

@app.post("/api/guess")
# endpoint function - things should run every request 
def guess(data : dict):
    word = data["word"]
    word = word.lower()
    score = get_similarity(DailyWord ,word )
    rank = score_to_rank(score)
    return {"score": score, "rank": rank}


