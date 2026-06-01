
from sentence_transformers import SentenceTransformer
from sentence_transformers import util

model = SentenceTransformer("all-MiniLM-L6-v2")



def get_similarity(word1, word2):
    word1Vector = model.encode(word1)
    word2Vector = model.encode(word2)
    score = util.cos_sim(word1Vector,word2Vector).item()
    score = round(min(1.0, max(0.0, score)), 4)
    
    return score 

def score_to_rank(score):
    if score is None:
        return 'unknown word' 
    elif score == 1:
        return 'Exactly'
    elif score >= 0.5:
        return 'Burning hot'
    elif score >= 0.35:
        return 'Very warm'
    elif score >= 0.25:
        return 'warm'
    elif score >= 0.15:
        return 'Cold'
    else :
        return 'Freezing'
    


