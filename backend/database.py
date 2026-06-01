import sqlite3 
from datetime import date
from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "game.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS words (
    id INTEGER PRIMARY KEY,
    word TEXT NOT NULL,
    date TEXT NOT NULL
    );
        """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS guesses (
    id INTEGER PRIMARY KEY,
    word TEXT NOT NULL,
    score REAL NOT NULL,
    timestamp TEXT NOT NULL
    );            
        """)
    
    conn.commit()
    conn.close()    


def get_daily_word():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    Today = str(date.today())
    cursor.execute("SELECT word FROM words where date = ?", (Today,))
    row = cursor.fetchone()
    if row:
        conn.close()    
        return row[0]   
    else:
        conn.close()    
        return None

def save_guess(word , score):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    wordDate = str(datetime.now())
    cursor.execute("INSERT INTO guesses (word, score, timestamp) VALUES (?,?,?)",
                (word, score, wordDate))
    conn.commit()
    conn.close()    

def set_daily_word(word ,overwrite=False):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    today = str(date.today())

    cursor.execute("SELECT word FROM words WHERE date = ?", (today,))
    existing = cursor.fetchone()

    if not existing:
        cursor.execute("INSERT INTO words (word, date) VALUES (?, ?)", (word, today))
        conn.commit()
    elif existing and overwrite:
        cursor.execute("UPDATE words SET word = ? WHERE date = ?", (word, today))
        conn.commit()
    conn.close()

def check_word(word):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT score FROM guesses WHERE word = ?" , (word,))
    existing = cursor.fetchone()
    if existing:
        conn.close()
        return existing[0]
    else:
        conn.close()
        return None

def clear_guesses():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM guesses;")
    conn.commit()
    conn.close()
    print("Guesses table cleared.")

init_db()
print("Database ready")
print("Today's word:", get_daily_word())