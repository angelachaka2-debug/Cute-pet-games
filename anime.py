def anime_watchlist():
    print("🎬 Welcome to your Anime Watchlist! 🍿\n")
    print("Let's keep track of the anime you want to watch! \n📺")

    # 1. A python list to store our anime titles using square brackets []
    watchlist = ["Attack on Titan", "Demon Slayer", "My Hero Academia" ]

    while True:
        print("\n--- Current Watchlist ---")
        # A loop to display every anime currently in the list
        for index, anime in enumerate(watchlist):
            print(f"{index + 1}. {anime}")

        print("\nWould you like to add a new anime to your watchlist or remove one?")
        print("1. Add a sick new anime to the list! ✨")
        print("2. Remove an anime from the list ❌")
        print("3. Quit watchlist 🏁")

        choice = input("choose your battle (1, 2, or 3): ")
        
        if choice == "1":
            new_anime = input("What kick ass anime would you like to add?: ")
            watchlist.append(new_anime) # .append() adds the new item to the end of the list
            print(f"🔥Awesome! '{new_anime}' is a great addition! 🔥")

        elif choice == "2":
            print("\nWhich number of the anime would you like to remove?")
            remove_index = input("Enter the number of the anime: ")

            # Convert user text into an integar (whole number) so Python can use it as a list pasition
            pos = int(remove_index) -1

            if 0 <= pos < len(watchlist):
                removed_anime = watchlist.pop(pos) # .pop() removes the items at that specific position
                print(f"🗑️ Removed '{removed_anime}'from your watchlist")
            else:
                print("❌ That number doesn't match any anime on your list!")
        elif choice == "3":
            print("\nHope you enjoy your anime marathon! Till next time! 👋")
            break
        else:
            print("\nThat's not a vaild choice, try again!")

anime_watchlist()