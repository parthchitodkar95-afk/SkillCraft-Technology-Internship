# ============================================
#   SkillCraft Technology - Internship Task 02
#   Number Guessing Game
#   Author: Parth Jivan Chitodkar
# ============================================
 
import random
 
print("=" * 45)
print("   SkillCraft Technology - Task 02")
print("        Number Guessing Game")
print("=" * 45)
 
while True:
    print("\nSelect Difficulty Level:")
    print("  1. Easy   (1 - 50,  10 chances)")
    print("  2. Medium (1 - 100,  7 chances)")
    print("  3. Hard   (1 - 200,  5 chances)")
    print("  4. Exit")
    print("-" * 45)
 
    level = input("Enter your choice (1/2/3/4): ").strip()
 
    if level == '4':
        print("\nThanks for playing! SkillCraft Technology - Task 02 Complete!")
        break
 
    if level == '1':
        low, high, chances = 1, 50, 10
    elif level == '2':
        low, high, chances = 1, 100, 7
    elif level == '3':
        low, high, chances = 1, 200, 5
    else:
        print("Invalid choice! Please enter 1, 2, 3, or 4.")
        continue
 
    secret = random.randint(low, high)
    attempts = 0
 
    print(f"\nI have picked a number between {low} and {high}.")
    print(f"You have {chances} chances to guess it. Good luck!\n")
 
    while attempts < chances:
        remaining = chances - attempts
        try:
            guess = int(input(f"Attempt {attempts + 1}/{chances} - Enter your guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue
 
        attempts += 1
 
        if guess < low or guess > high:
            print(f"Out of range! Guess between {low} and {high}.")
 
        elif guess == secret:
            print("\n" + "=" * 45)
            print(f"  Correct! The number was {secret}!")
            print(f"  You guessed it in {attempts} attempt(s)!")
            if attempts == 1:
                print("  Wow, first try! You are a genius!")
            elif attempts <= chances // 2:
                print("  Excellent performance!")
            else:
                print("  Well done!")
            print("=" * 45)
            break
 
        elif guess < secret:
            print(f"  Too Low! Try a higher number. ({remaining - 1} chances left)")
 
        else:
            print(f"  Too High! Try a lower number. ({remaining - 1} chances left)")
 
    else:
        print("\n" + "=" * 45)
        print(f"  Game Over! You ran out of chances.")
        print(f"  The correct number was: {secret}")
        print("=" * 45)
 
    print("\nWant to play again?")
    play_again = input("Press Y to play again or any key to go to menu: ").strip().lower()
    if play_again != 'y':
        continue