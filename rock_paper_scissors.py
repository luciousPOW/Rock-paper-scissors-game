from getpass import getpass

def determine_winner(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return "It's a tie! 🤝"
    elif (
        (player1_choice == 'R' and player2_choice == 'S') or
        (player1_choice == 'S' and player2_choice == 'P') or
        (player1_choice == 'P' and player2_choice == 'R')
    ):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

# Get user input for Player 1 using getpass
player1_choice = getpass("Player 1, choose 'R' for Rock, 'P' for Paper, or 'S' for Scissors: ").upper()

# Validate player 1's input
while player1_choice not in ['R', 'P', 'S']:
    print("Invalid input! Please choose 'R', 'P', or 'S'.")
    player1_choice = getpass("Player 1, choose 'R' for Rock, 'P' for Paper, or 'S' for Scissors: ").upper()

# Get user input for Player 2 using getpass
player2_choice = getpass("Player 2, choose 'R' for Rock, 'P' for Paper, or 'S' for Scissors: ").upper()

# Validate player 2's input
while player2_choice not in ['R', 'P', 'S']:
    print("Invalid input! Please choose 'R', 'P', or 'S'.")
    player2_choice = getpass("Player 2, choose 'R' for Rock, 'P' for Paper, or 'S' for Scissors: ").upper()

# Determine the winner
result = determine_winner(player1_choice, player2_choice)

# Display the result
print(result)
