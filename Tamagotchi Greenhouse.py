#Tamagotchi plant, import time.
import time
def tamagotchi_plant():
    print("🌱 Welcome to your Tamagotchi Greenhouse! 🌻✨")

    name = input("What would you like to name your plant-pet?: ")
    stages = ["Seed 🌱", "Sprout 🌿", "small plant 🌸", "Blooming flower 🌺"]
    current_stage = 0 
    water =50 
    happiness = 50

    while True:
        print(f"\n--- {name}'s Status ---")
        print(f"Form: {stages[current_stage]}")
        print(f"Water Level: {water}/100")
        print(f"Happiness Level: {happiness}/100\n")

        print("What do you want to do?")
        print("1. Water yourbuddy 💧")
        print("2. Give it some sunlight ☀️")
        print("3. sing or play with it 🎶")
        print("4. Check status")
        print("5. Exit ❌")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            water += 10
            happiness += 5
            print(f"\n💧 you watered {name}. Water and happiness increased!")
            time.sleep(4)

            if water >= 80 and current_stage < len(stages) - 1:
                current_stage += 1
                water = 40 
                print(f" 🌱Groth milestone reached! {name} evolved into a {stages[current_stage]}! 🌸✨")
                time.sleep(4)

        elif choice == "2":
            happiness += 20 
            water -= 10
            print(f"\n🌟 {name} soaked up the warm rays! Happiness is up, but it got a bit thirsty 🐳.")
            time.sleep(4)

        elif choice == "3":
            happiness += 15
            print(f"\n 🎊 You played music for {name}. it's glowing with joy!🦝")
            time.sleep(4)

        elif choice == "4":
            print(f"\n--- {name}'s Status ---")
            print(f"Form: {stages[current_stage]}")
            print(f"Water Level: {water}/100")
            print(f"Happiness Level: {happiness}/100\n")

        elif choice == "5":
            print(f"\n👋 Goodbye, {name}! You took great care of your plant-pet!🐱")
            break
            time.sleep(10)

        else:
            print("\n ❌ That's not a valid choice. try again 😓")

tamagotchi_plant()
