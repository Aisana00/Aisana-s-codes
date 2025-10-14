import random

def guess_the_number():
   
    # Generate random number between 1 and 20
    secret_number = random.randint(1, 20)
    
    # Get player's name
    name = input("Hello! What is your name?\n")
    
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    
    guesses_taken = 0
    
    while True:
        # Get player's guess
        try:
            guess = int(input("Take a guess.\n"))
            guesses_taken += 1
            
            # Check the guess
            if guess < secret_number:
                print("Your guess is too low.")
            elif guess > secret_number:
                print("Your guess is too high.")
            else:
                print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
                break
                
        except ValueError:
            print("Please enter a valid number between 1 and 20.")

# Start the game
if __name__ == "__main__":
    guess_the_number()