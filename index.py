
import random

def welcome_message():
    print("\n````````````  🥌  🧻  ✂️   Welcome to Rock, Paper, Scissors!````````````")
    print()
    print("""
Winning Rules:
1. Paper vs Rock --> Paper wins
2. Scissors vs Paper --> Scissors win
3. Rock vs Scissors --> Rock win
4. Rock vs Rock --> Tie
5. Paper vs Paper --> Tie
6. Scissors vs Scissors --> Tie
""")

def get_user_choice():
    choices = ['rock', 'paper', 'scissors']
    while True:
        user_choice = input("Enter your choice: rock, paper, or scissors: ").lower()
        if user_choice in choices:
            return user_choice
        print("Invalid choice.📥 Try again!")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "⚖️ It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "🏆 You win!"
    else:
        return "💻 Computer wins!"

def play_game():
    welcome_message()  # Pehle welcome message show hoga

    while True:
        game = input("Would you like to play this interesting game ❓ (y/n): ").lower()
        if game == "y":
            print("\n 👍 Great! Let's start the game❗\n")
        else:
            print("\n Maybe next time. Have a great day! 😊")
            break  # Game exit karega agar user "n" kahe

        while True:
            user_choice = get_user_choice()
            computer_choice = get_computer_choice()

            print(f"\nYou chose: {user_choice}")
            print(f"Computer chose: {computer_choice}")

            result = determine_winner(user_choice, computer_choice)
            print(result)

            # Asking user if they want to play again
            play_again = input("\nDo you want to play again? (y/n): ").lower()
            if play_again != "y":
                print("\n🎉 Thanks for Playing! Hope you had fun! 😊")
                return  

if __name__ == "__main__":
    play_game()

