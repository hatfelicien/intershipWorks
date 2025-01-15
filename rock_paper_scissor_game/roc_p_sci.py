import random
#list of possible hands
hands = ["Rock", "Scissors", "Paper"]
#creating dictionary
results = {"win": "You win!", "lose": "You lose!", "draw": "It's a draw!"}
#displaying a start message to the user
def start_message():
    print("Rock-Paper-Scissors Game Start!")
#validating the input
def is_hand(string):
    if string.isdigit():
        number = int(string)
        return 0 <= number <= 2
    return False
#getting player's choice
def get_player():
    print("Choose your hand:")
    # Create the input prompt dynamically
    input_message = ", ".join([f"{i}:{hand}" for i, hand in enumerate(hands)])
    print(input_message)
    while True:
        player = input("Enter your choice: ")
        #validate the input
        if is_hand(player):
            return int(player) #return input as integer
        #if an input is invalid user has to try again
        print("Invalid input. Please try again.")
#getting a random coice from computer randomly
def get_computer():
    return random.randint(0, 2)
# function to display Choices
def view_hand(player, computer):
    print(f"You chose: {hands[player]}")
    print(f"Computer chose: {hands[computer]}")
#function to get result from game based on differences
def get_result(player, computer):
    hand_diff = player - computer
    if hand_diff == 0: # Same hand equal to Draw
        return "draw"
    elif hand_diff == -1 or hand_diff == 2:
        return "win" # player win
    else:
        return "lose" # player loses
# Function to display the result of the game
def view_result(result):
    print(results[result])

def play():
    #get player's hand
    player = get_player()
    #get computer's hand
    computer = get_computer()
    # display hands
    view_hand(player, computer)
    # calculating difference
    result = get_result(player, computer)
    #displaying the result
    view_result(result)
    if result == "draw":
        play()

start_message()
play()