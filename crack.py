# Define the correct answer
correct_answer = [0, 4, 2]

# Define the hints with numbers and clues
hints = [
    ([6, 8, 2], "one number is correct and well placed"),
    ([6, 1, 4], "one number is correct but wrongly placed"),
    ([2, 0, 6], "Two numbers are correct but wrongly placed"),
    ([7, 3, 8], "Nothing is correct"),
    ([7, 8, 0], "one number is correct but wrongly placed")
]

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
        return "Congratulations! You unlocked the lock!"
    else:
        # Check the guess against each hint
        for hint_data in hints:
            hint_guess, hint_text = hint_data
            if check_hint(guess, hint_text, ans):
                return f"Hint matched: {hint_text}"
        return "Try again!"

# Start the game loop
def start_game():
    print("Welcome to the Numeric Lock Game!")
    print("You need to guess the 3-digit numeric code.")
    print("Hints will guide you. Good luck!")
    
    while True:
        # Get user input
        user_input = input("Enter your 3-digit guess (e.g., 123): ")
        
        # Convert the input into a list of integers
        try:
            guess = [int(x) for x in user_input]
            if len(guess) != 3:
                print("Please enter exactly 3 digits.")
                continue
        except ValueError:
            print("Invalid input! Please enter numeric digits only.")
            continue
        
        # Validate the guess
        result = validate_guess(guess, hints, correct_answer)
        print(result)
        
        # End game if correct guess
        if guess == correct_answer:
            break

# Run the game
start_game()
