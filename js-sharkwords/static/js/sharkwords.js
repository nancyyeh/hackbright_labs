const ALPHABET = 'abcdefghijklmnopqrstuvwxyz';
const WORDS = [
  'strawberry', 'orange', 'apple', 'banana', 'pineapple', 'kiwi',
  'peach', 'pecan', 'eggplant', 'durian', 'peanut', 'chocolate'
];


let numWrong = 0;


// Loop over the chars in `word` and create divs.
//
const createDivsForChars = (word) => {
  for (const char in word){
    $('#word-container').append(`<div class="letter-box ${word[char]}"></div>`);
  }
};


// Loop over each letter in `ALPHABET` and generate buttons.
//
const generateLetterButtons = () => {
  // Replace this with your code
  for (const letter in ALPHABET){
    $('#letter-buttons').append(`<button>${ALPHABET[letter]}</button>`)
  }
};


// Set the `disabled` property of `buttonEl` to `true.
//
// `buttonEl` is an `HTMLElement` object.
//
const disableLetterButton = (buttonEl) => {
  // Replace this with your code
  const button = $(buttonEl);

  button.prop('disabled', true);

};


// Return `true` if `letter` is in the word.
//
const isLetterInWord = (letter) => {
  // Replace this with your code
  const char = $(`div.${letter}`);

  return char[0] !== undefined;

};


// Called when `letter` is in word. Update contents of divs with `letter`.
//
const handleCorrectGuess = (letter) => {
  // Replace this with your code
  // console.log(isLetterInWord)
  if (isLetterInWord){
     $(`div.${letter}`).append(letter)     
   }
};


// Called when `letter` is not in word.
//
// If the shark gets the person, disable all buttons and show the "play again"
// message. Otherwise, increment `numWrong` and update the shark image.
//
const handleWrongGuess = () => {
  // Replace this with your code
  
  numWrong += 1;
  const sharkPhoto = document.querySelector('img');
  const play = document.querySelector('#play-again');
  const allButtons = $('button');

  if (numWrong === 5){
    play.setAttribute('style', '');
    allButtons.prop('disabled', true);

  } else {
    
    sharkPhoto.setAttribute('src', `/static/images/guess${numWrong}.png`)
  }
  console.log(numWrong)

};


// Reset game state. Called before restarting the game.
//
const resetGame = () => {
  // Replace this with your code
  numWrong = 0

  const sharkPhoto = document.querySelector('img');
  sharkPhoto.setAttribute('src', `/static/images/guess0.png`)

  const play = document.querySelector('#play-again');
  play.setAttribute('style', 'display: none');

  const allButtons = $('button');
  allButtons.prop('disabled', false);

  for (const element of $('#word-container').children()) {
    element.remove();
  }

  for (const element of $('#letter-buttons').children()) {
    element.remove();
  }


};


// This is like if __name__ == '__main__' in Python
//
(function startGame() {
  // For now, we'll hardcode the word that the user has to guess.
  const word = 'hello';

  createDivsForChars(word);
  generateLetterButtons();

  $('button').on('click', (evt) => {
    const clickedBtn = $(evt.target);
    disableLetterButton(clickedBtn);

    const letter = clickedBtn.html();

    if (isLetterInWord(letter)) {
      handleCorrectGuess(letter);
    } else {
      handleWrongGuess(letter);
    }
  });

  $('#play-again').on('click', () => {
    resetGame();
    startGame();
  });
})();
