import random

def get_user_choice():
    # Get the user's choice
    user_choice = input("Enter choice (rock, paper, or scissors): ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        user_choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()
    return user_choice

def get_ai_choice():
    # Get AI's random choice
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, ai_choice):
    # Determine the winner
    if user_choice == ai_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and ai_choice == 'scissors') or \
         (user_choice == 'scissors' and ai_choice == 'paper') or \
         (user_choice == 'paper' and ai_choice == 'rock'):
        return "You win!"
    else:
        return "AI wins!"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    
    # Main game loop
    while True:
        user_choice = get_user_choice()
        ai_choice = get_ai_choice()
        print(f"AI chose: {ai_choice}")
        
        result = determine_winner(user_choice, ai_choice)
        print(result)
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()