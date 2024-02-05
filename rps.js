const DOMSelectors = {
    form: document.querySelector("#form"),
    input: document.querySelector("#input"),
    button: document.getElementById("btn"),
    history: document.querySelector("#history"),
    restart: document.querySelector("#restart"),
    gameMessages: document.querySelector("#game-messages"),
};

let gameArray = [];

function displayMessage(message){
    DOMSelectors.gameMessages.insertAdjacentHTML("beforeend", `<div>${message}</div>`);
}

DOMSelectors.form.addEventListener("submit", function(event) {
    event.preventDefault();
}); 

DOMSelectors.button.addEventListener("click", function() {
    let gameResponse;
    const randomNumber = Math.floor(Math.random() * 3) + 1;
    if (randomNumber === 1) {
        gameResponse = "Rock";
    } else if (randomNumber === 2) {
        gameResponse = "Paper";
    } else if (randomNumber === 3) {
        gameResponse = "Scissors";
    }
    displayMessage("Opponent chose: " + gameResponse)
    const userChoice = DOMSelectors.input.value.toLowerCase();
    if ((userChoice === 'rock' && gameResponse === 'Paper') ||
        (userChoice === 'paper' && gameResponse === 'Scissors') ||
        (userChoice === 'scissors' && gameResponse === 'Rock')) {
        displayMessage('You lose');
        gameArray.push(' Lost');
    } else if ((userChoice === 'scissors' && gameResponse === 'Paper') ||
        (userChoice === 'rock' && gameResponse === 'Scissors') ||
        (userChoice === 'paper' && gameResponse === 'Rock')) {
        displayMessage('You won');
        gameArray.push(' Win');
    } else if (userChoice === gameResponse.toLowerCase()) {
        displayMessage('You draw');
        gameArray.push(' Tie');
    } else {
        displayMessage('Error, check your spelling and put in lower case');
    }

    DOMSelectors.input.value = "";
});
DOMSelectors.history.addEventListener("click", function() {
    displayMessage("Your game history: ")
    displayMessage(gameArray)
})

DOMSelectors.restart.addEventListener("click", function() {
    gameArray = [];
    DOMSelectors.gameMessages.innerHTML = '';
})