const submitBtn = document.getElementById("submitBtn");
const guessInput = document.getElementById("guessInput");
const resultsDiv = document.getElementById("results");

submitBtn.addEventListener("click", async function() {
    const word = guessInput.value.trim();
    
    if (word === "") return;
    
    const response = await fetch("http://127.0.0.1:8000/api/guess", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({word: word})
    });
    
    const data = await response.json();
    
    const p = document.createElement("p");
    p.textContent = `${word} → ${data.score} → ${data.rank}`;
    resultsDiv.appendChild(p);
    
    guessInput.value = ""; 
});