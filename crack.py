import random
from colorama import Fore, Style, init

# Initialize colorama for cross-platform support
init(autoreset=True)

# Define the hints with numbers and clues (hints remain fixed)
hints = [
    ([6, 8, 2], "one number is correct and well placed"),
    ([6, 1, 4], "one number is correct but wrongly placed"),
    ([2, 0, 6], "Two numbers are correct but wrongly placed"),
    ([7, 3, 8], "Nothing is correct"),
    ([7, 8, 0], "one number is correct but wrongly placed")
]

# Function to generate a random 3-digit answer
def generate_random_answer():
    return [random.randint(0, 9) for _ in range(3)]

# Function to check each guess against the correct answer
def check_hint(guess, hint, ans):
    if hint == "one number is correct and well placed":
        return sum([guess[i] == ans[i] for i in range(3)]) == 1
    elif hint == "one number is correct but wrongly placed":
        return sum([guess[i] != ans[i] and guess[i] in ans for i in range(3)]) == 1
    elif hint == "Two numbers are correct but wrongly placed":
        return sum([guess[i] != ans[i] and guess[i] in ans for i in range(3)]) == 2
    elif hint == "Nothing is correct":
        return all([num not in ans for num in guess])
    else:
        return False

# Function to validate the user's guess
def validate_guess(guess, hints, ans):
    if guess == ans:
        return Fore.GREEN + "🎉 Congratulations! You unlocked the lock!"
    else:
        # Check the guess against each hint
        for hint_data in hints:
            hint_guess, hint_text = hint_data
            if check_hint(guess, hint_text, ans):
                return Fore.YELLOW + f"🔑 Hint matched: {hint_text}"
        return Fore.RED + "❌ Try again!"

# Function to prompt user if they want to play again
def ask_play_again():
    while True:
        play_again = input(Fore.CYAN + "Do you want to play again? (yes/no): ").lower()
        if play_again in ['yes', 'no']:
            return play_again == 'yes'
        print(Fore.RED + "Invalid input! Please type 'yes' or 'no'.")

# Start the game loop
def start_game():
    print(Fore.CYAN + Style.BRIGHT + "Welcome to the Numeric Lock Game!")
    
    # Loop to allow replay
    while True:
        # Generate a new random 3-digit answer for every round
        correct_answer = generate_random_answer()
        print("\nA new lock has been set. Guess the 3-digit numeric code.")
        
        # Allow user up to 5 attempts to guess
        attempts = 0
        max_attempts = 5

        # Game continues until user guesses correctly or exceeds 5 attempts
        while attempts < max_attempts:
            # Get user input
            user_input = input(Fore.CYAN + f"\nAttempt {attempts + 1}/{max_attempts}: Enter your 3-digit guess (e.g., 123): ")

            # Convert the input into a list of integers
            try:
                guess = [int(x) for x in user_input]
                if len(guess) != 3:
                    print(Fore.RED + "Please enter exactly 3 digits.")
                    continue
            except ValueError:
                print(Fore.RED + "Invalid input! Please enter numeric digits only.")
                continue

            # Validate the guess
            result = validate_guess(guess, hints, correct_answer)
            print(result)
            
            # If user guessed correctly, break and ask to play again
            if guess == correct_answer:
                break
            
            attempts += 1

        # If user fails after 5 attempts, reveal the correct answer
        if attempts == max_attempts and guess != correct_answer:
            print(Fore.RED + f"\n😔 Sorry, you've reached {max_attempts} attempts.")
            print(Fore.GREEN + f"The correct answer was: {''.join(map(str, correct_answer))}")

        # Ask the user if they want to play again
        if not ask_play_again():
            print(Fore.CYAN + "Thank you for playing! Goodbye!")
            break

# Run the game
start_game()
