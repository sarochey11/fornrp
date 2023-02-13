const difficultyLevels = {
    easy: {
        maxNumber: 10,
        maxGuesses: 6
    },
    medium: {
        maxNumber: 50,
        maxGuesses: 4
    },
    hard: {
        maxNumber: 100,
        maxGuesses: 3
    }
};
let secretNumber,maxGuesses,player1,player2,currentPlayer,difficulty;

function generateRandomNumber(max) {
    return Math.floor(Math.random() * max) + 1;
};

function generateRandomWord() {
    const words = ['apple', 'banana', 'cherry', 'date', 'elderberry'];
    const randomIndex = Math.floor(Math.random() * words.length);
    return words[randomIndex];
};

function switchPlayer() {
    currentPlayer = currentPlayer === player1 ? player2 : player1;
};

function startGame() {
    // Get player names
    player1 = prompt("Player 1, what's your name?");
    player2 = prompt("Player 2, what's your name?");
    currentPlayer = player1;
    // Get difficulty level
    let userDifficulty = prompt("What difficulty do you want to play on? (easy, medium, hard)").toLowerCase();
    if (!difficultyLevels[userDifficulty]) {
        userDifficulty = Object.keys(difficultyLevels)[Math.floor(Math.random() * 3)];
        console.log(`difficulty level not found, difficulty level set to ${userDifficulty}`);
    }
    difficulty = userDifficulty;
    const difficultySettings = difficultyLevels[difficulty];
    maxGuesses = difficultySettings.maxGuesses;
    if (difficulty === "easy") {
        secretNumber = generateRandomNumber(difficultySettings.maxNumber);
        console.log(`${currentPlayer}, your turn to guess the ${difficulty} secret number! You have ${maxGuesses} attempts.`);
    } else {
        secretNumber = generateRandomWord();
        console.log(`${currentPlayer}, your turn to guess the ${difficulty} secret word! You have ${maxGuesses} attempts.`);
    }
};

function guess() {
    let guess = prompt(`${currentPlayer}, please enter your guess:`);
    if (guess === secretNumber) {
        console.log(`Congratulations, ${currentPlayer}! You guessed the ${difficulty} secret number or word correctly!`);
    } else {
        maxGuesses--;
        if (maxGuesses === 0) {
            console.log(`Sorry, ${currentPlayer}. You have no more attempts left. The ${difficulty} secret number or word was ${secretNumber}.`);
        } else {
            console.log(`Sorry, ${currentPlayer}. That is not correct. You have ${maxGuesses} attempts left.`);
            switchPlayer();
            guess();
        }
    }
};