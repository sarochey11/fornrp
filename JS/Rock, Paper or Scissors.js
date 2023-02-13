const getUserChoice = userInput => {
    userInput = userInput.toLowerCase();
    if (userInput === 'rock' || userInput === 'paper' || userInput === 'scissors' || userInput === 'bomb') {
        return userInput;
    } else {
        console.log('Error: Please enter rock, paper or scissors');
    }
}

const getComputerChoice = () => {
    const randomNumber = Math.floor(Math.random() * 3);
    switch (randomNumber) {
        case 0:
            return 'rock';
        case 1:
            return 'paper';
        case 2:
            return 'scissors';
    }
}

const determineWinner = (userChoice, computerChoice) => {
    if (userChoice === computerChoice) {
        return 'It is a tie';
    } else if (userChoice === 'rock') {
        if (computerChoice === 'paper') {
            return 'Computer wins';
        } else {
            return 'User wins';
        }
    } else if (userChoice === 'paper') {
        if (computerChoice === 'scissors') {
            return 'Computer wins';
        } else {
            return 'User wins';
        }
    } else if (userChoice === 'scissors') {
        if (computerChoice === 'rock') {
            return 'Computer wins';
        } else {
            return 'User wins';
        }
    } else if (userChoice === 'bomb') {
        return 'User wins';
    }
}

function playGame() {
    const userChoice = getUserChoice('bomb');
    const computerChoice = getComputerChoice();
    console.log('You chose: ' + userChoice);
    console.log('Computer chose: ' + computerChoice);
    console.log(determineWinner(userChoice, computerChoice));
}

playGame();