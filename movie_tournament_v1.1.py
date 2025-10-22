import random

running = True

movies_quarterfinals = []

while running:
    if not movies_quarterfinals:
        movies_quarterfinals = [input(f"Please, enter movie No. {i+1}: ") for i in range(8)]

    confirmed = False

    while not confirmed:
        print("Your movies for the tournament:")
        for i, movie in enumerate(movies_quarterfinals, start=1):
            print(f"({i}) '{movie}'")

        change = input("Enter the number of a movie to change it or enter (c) to confirm and start the tournament: ")

        if change.lower() == "c":
            confirmed = True

        elif change.isdigit() and 1 <= int(change) <= 8:
            idx = int(change) - 1
            movies_quarterfinals[idx] = input(f"Correct or enter a new movie for position ({change}): ")
        
        else:
            print("Invalid input. Please, try again.")
    
    random.shuffle(movies_quarterfinals)

    quarterfinals = [
        (movies_quarterfinals[0], movies_quarterfinals[1]),
        (movies_quarterfinals[2], movies_quarterfinals[3]),
        (movies_quarterfinals[4], movies_quarterfinals[5]),
        (movies_quarterfinals[6], movies_quarterfinals[7])
    ]

    winners_quarterfinals = []

    for i, (movie1, movie2) in enumerate(quarterfinals, start=1):
        while True:
            choice = input(f"Choose the winner of the quarterfinal matchup No. {i} by entering (1) for '{movie1}' or (2) for '{movie2}': ")
            
            if choice == "1":
                winners_quarterfinals.append(movie1)
                print(f"The winner of the quarterfinal matchup No. {i} is '{movie1}'!")
                break
            
            elif choice == "2":
                winners_quarterfinals.append(movie2)
                print(f"The winner of the quarterfinal matchup No. {i} is '{movie2}'!")
                break
            
            else:
                print("Invalid choice. Please, enter (1) or (2).")

    random.shuffle(winners_quarterfinals)

    semifinals = [
        (winners_quarterfinals[0], winners_quarterfinals[1]),
        (winners_quarterfinals[2], winners_quarterfinals[3])
    ]

    winners_semifinals = []

    for i, (movie1, movie2) in enumerate(semifinals, start=1):
        while True:
            choice = input(f"Choose the winner of the semifinal matchup No. {i} by entering (1) for '{movie1}' or (2) for '{movie2}': ")
            
            if choice == "1":
                winners_semifinals.append(movie1)
                print(f"The winner of the semifinal matchup No. {i} is '{movie1}'!")
                break
            
            elif choice == "2":
                winners_semifinals.append(movie2)
                print(f"The winner of the semifinal matchup No. {i} is '{movie2}'!")
                break
            
            else:
                print("Invalid choice. Please, enter (1) or (2).")

    random.shuffle(winners_semifinals)

    movie1, movie2 = winners_semifinals

    while True:
        choice = input(f"Choose the winner of the movie tournament by entering (1) for '{movie1}' or (2) for '{movie2}': ")
            
        if choice == "1":
            winner_grandfinal = movie1
            print(f"The winner of the movie tournament is '{movie1}'! Enjoy the movie!")
            break
            
        elif choice == "2":
            winner_grandfinal = movie2
            print(f"The winner of the movie tournament is '{movie2}'! Enjoy the movie!")
            break
            
        else:
            print("Invalid choice. Please, enter (1) or (2).")

    while True:
        again = input("Enter (1) to replay the tournament with the same movies, enter (2) to create a new tournament, or enter (3) to exit: ")

        if again == "1":
            break
        
        elif again == "2":
            movies_quarterfinals = []
            break
        
        elif again == "3":
            print("Thanks for playing!")
            running = False
            break

        else:
            print("Invalid choice.")
