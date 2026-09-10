# game

def play_with_pet():
    # 1. Initialize pet stats and name
    name = input("What do you want to name your pet?: ")
    fullness = 50 # Let's track fullness instead of hunger 
    happiness = 50

    print(f"\nWelcome, {name} is happy to see you! 🐾")
    # 2. Keep the game running in a loop
    while True:
        print(f"--- {name}'s Stats ---")
        print(f"Fullness: {fullness}/100") # Higher is better!
        print(f"Happiness: {happiness}/100\n")


        print("What do you want to do?")
        print("1. Feed them 🍎")
        print("2. Play with them 🧶")
        print("3. Quit 🚪")
        choice = input("Enter your choice (1, 2, or 3): ")
        # 3. Handle user choices using conditional statements
        if choice == "1":
            fullness += 10 #now feeding them MAKES fullness go up!
        elif choice == "2":
            happiness = min(100, happiness + 15)
            print(f"Yay! You played with {name}! They look happier!\n")
        elif choice == "3":
            print(f"Goodbye! Take care of {name}! 🎉")
            break # This exits the loop and ends the program
        else:
            print("That's not a valid choice, try again!\n")

# Run the game function
play_with_pet()