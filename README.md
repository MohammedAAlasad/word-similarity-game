Word Similarity Game

-- What is this?
A word guessing game where you try to find a secret daily word.
You type a guess and the game tells you how close 
your word is to the secret word.

-- Requirements
Python 
pip

-- How to install
1. Clone this repository
2. Create a virtual environment:
   python3 -m venv venv
   source venv/bin/activate
3. Install dependencies:
   pip install -r requirements.txt

-- How to run
1. Start the backend server:
   cd backend
   uvicorn main:app --reload
2. Open frontend/index.html in your browser
3. Type a word and click Submit

-- How it works
The game uses a Sentence Transformers NLP model to convert 
words into vectors (embeddings). It then computes 
the similarity between your guess and the secret word.

