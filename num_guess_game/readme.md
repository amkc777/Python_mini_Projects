# Number Guessing Game

This Python script implements a simple number guessing game where the user has to guess a randomly generated integer within a specified range.

## Usage

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/amkc777/Python_mini_Projects.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Python_mini_Projects/num_guess_game
    ```

3. Run the script:

    ```bash
    python num_guess_game.py
    ```

4. Follow the instructions to input the lower and upper bounds for the range of integers, and start guessing!

## Description

The script prompts the user to input lower and upper bounds for the range of integers. It then generates a random number within this range using the `random.randint()` function from the `random` module.

The user is informed about the number of chances they have to guess the integer, which is calculated based on the logarithm of the range size.

The game proceeds with the user making guesses, and the script providing feedback on whether the guess is too high or too low. If the user guesses the correct number, the script congratulates them and displays the number of attempts taken.

If the user exhausts all their guesses without correctly guessing the number, the script reveals the correct number and encourages them to try again.

This script demonstrates basic usage of random number generation, user input handling, conditional statements, and looping in Python.
