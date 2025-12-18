Project repository:
https://github.com/Shivanjali13/Number-Guess

https://roadmap.sh/projects/number-guessing-game

Number Guess Game

It is beginner friendly python command line game where the computer randomly selects an number and the user hast to guess it within the allowed attempts as per the difficulty level of the game the user chooses.

Features-
->There are three levels :
Easy(10 attempts)
Medium(7attempts)
Hard(3 attempts)

->Random number generation
->Hints after each wrong guess(Too low/Too high)
->Input validation
->Time tracking for each game
->High score tracking using file storage

Game Rules-
1. The computer selects a random number between 1 to 100
2. The player selects difficulty level
3. The player has limited attempts based on difficulty level 
4. After each wrong guess, a hint is given
5. Game ends when:
    - The user guesses the correct number (Win)
    - The user runs out of attempts (Lose)

Project Structure 

Number-Guess/
│
├── src/
│ ├── game.py
│ └── high_score.txt
│
├── README.md
└── .gitignore

#How to run
1. Clone the repository:
'''bash
git clone https://github.com/Shivanjali13/Number-Guess.git

2. Navigate to project directory:
cd Number-Guess

3. Run the game 
python src/game.py

Technologies used
* Python 3
* Standard Python Libraries(random,time)
* Git & GitHub

Future improvemnets
* Replay option
* GUI version 
* Web version using Flask
* UNit testing with pytest

Author 
Shivanjali13
