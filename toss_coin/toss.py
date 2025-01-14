import random
# List of possible sides
sides = ["head", "tail"]
# Function to display start message
def start_message():
    print("toss coin game start")
# Function to validate input
def is_toss(string):
    if string.isdigit():  # Check if the input is a digit
        number = int(string)
        return 0 <= number <= 1  # Check if the number is valid (0 or 1)
    return False  # Return False for invalid input
# Function to get player's choice
def toss_choice():
    print("Choose your side")
    print("0:head, 1:tail")
    while True:
        player = input("enter your choice: ")
        # Validate the input
        if is_toss(player):
            return int(player)  # Return input as integer
        print("invallid please try again")  # Prompt again for invalid input
# Function to get computer's choice
def get_computer():
    return random.randint(0, 1)  # Randomly generate 0 or 1
# Function to display choices
def view_side(player, computer):
    print(f"My bet is {sides[player]}")
    print(f"Coin is {sides[computer]}")
# Function to compare result and return outcome
def get_result(player, computer):
    return "win" if player == computer else "lose"
# Function to display the result
def view_result(result):
    print(result)
# Main function to play the game
def play():
    # Get player's choice
    player = toss_choice()
    # Get computer's random choice
    computer = get_computer()
    # Display both choices
    view_side(player, computer)
    # Determine the result
    result = get_result(player, computer)
    # Display the result
    view_result(result)
# Start the game
start_message()
play()