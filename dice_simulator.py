import random

# ASCII art for dice faces with different symbols
dice_faces = [
    '''
    -------
    |     |
    |  o  |
    |     |
    ------- 
       1''',
    '''
    -------
    | o   |
    |     |
    |   o |
    ------- 
       2''',
    '''
    -------
    | o   |
    |  o  |
    |   o |
    ------- 
       3''',
    '''
    -------
    | o o |
    |     |
    | o o |
    ------- 
       4''',
    '''
    -------
    | o o |
    |  o  |
    | o o |
    ------- 
       5''',
    '''
    -------
    | o o |
    | o o |
    | o o |
    ------- 
       6'''
]

def roll_dice():
    return random.randint(1, 6)

def main():
    print("Welcome to the Dice Simulator!")
    while True:
        input("Press Enter to roll the dice... (Press q to quit)")
        roll_result = roll_dice()
        print("You rolled:")
        print(dice_faces[roll_result - 1])  # Adjust index to match dice numbering
        user_input = input("Roll again? (y/n): ").lower()
        if user_input == 'n':
            break
        elif user_input == 'q':
            print("Exiting the Dice Simulator.")
            break

if __name__ == "__main__":
    main()
