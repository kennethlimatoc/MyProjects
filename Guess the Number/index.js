let randomNumber;
let attempts = 0;


const guessInput = document.getElementById('guess-input');
const guessButton = document.getElementById('guess-btn');
const message = document.getElementById('message');
const attemptsDisplay = document.getElementById('attempts');
const resetButton = document.getElementById('reset-btn');


function startNewGame() {
  randomNumber = Math.floor(Math.random() * 100) + 1; 
  attempts = 0;
  attemptsDisplay.textContent = attempts;
  message.textContent = '';
  guessInput.value = '';
  resetButton.style.display = 'none';
  guessButton.disabled = false;
}


guessButton.addEventListener('click', () => {
  const userGuess = Number(guessInput.value);

  if (!userGuess || userGuess < 1 || userGuess > 100) {
    message.textContent = 'Please enter a number between 1 and 100.';
    return;
  }

  attempts++;
  attemptsDisplay.textContent = attempts;

  if (userGuess === randomNumber) {
    message.textContent = `Congratulations! You've guessed the right number: ${randomNumber}.`;
    guessButton.disabled = true;
    resetButton.style.display = 'block'; 
  } else if (userGuess < randomNumber) {
    message.textContent = 'Too low! Try again.';
  } else {
    message.textContent = 'Too high! Try again.';
  }
});


resetButton.addEventListener('click', () => {
  startNewGame();
});


startNewGame();
