movie1 = input("Please, enter the 1st movie: ")
movie2 = input("Please, enter the 2nd movie: ")
movie3 = input("Please, enter the 3rd movie: ")
movie4 = input("Please, enter the 4th movie: ")
movie5 = input("Please, enter the 5th movie: ")
movie6 = input("Please, enter the 6th movie: ")
movie7 = input("Please, enter the 7th movie: ")
movie8 = input("Please, enter the 8th movie: ")

movies_quarterfinals = [movie1, movie2, movie3, movie4, movie5, movie6, movie7, movie8]

import random

random.shuffle(movies_quarterfinals)

movie_quarterfinals1 = movies_quarterfinals[0]
movie_quarterfinals2 = movies_quarterfinals[1]
movie_quarterfinals3 = movies_quarterfinals[2]
movie_quarterfinals4 = movies_quarterfinals[3]
movie_quarterfinals5 = movies_quarterfinals[4]
movie_quarterfinals6 = movies_quarterfinals[5]
movie_quarterfinals7 = movies_quarterfinals[6]
movie_quarterfinals8 = movies_quarterfinals[7]

choice1_quarterfinals = input(f"Choose the winner of this matchup by entering (1) for {movie_quarterfinals1} or (2) for {movie_quarterfinals2}: ")

if choice1_quarterfinals == "1":
    winner1_quarterfinals = movie_quarterfinals1
    print(f"The winner is {movie_quarterfinals1}!")
elif choice1_quarterfinals == "2":
    winner1_quarterfinals = movie_quarterfinals2
    print(f"The winner is {movie_quarterfinals2}!")
else:
    print("Invalid choice.")

choice2_quarterfinals = input(f"Choose the winner of this matchup by entering (1) for {movie_quarterfinals3} or (2) for {movie_quarterfinals4}: ")

if choice2_quarterfinals == "1":
    winner2_quarterfinals = movie_quarterfinals3
    print(f"The winner is {movie_quarterfinals3}!")
elif choice2_quarterfinals == "2":
    winner2_quarterfinals = movie_quarterfinals4
    print(f"The winner is {movie_quarterfinals4}!")
else:
    print("Invalid choice.")

choice3_quarterfinals = input(f"Choose the winner of this matchup by entering (1) for {movie_quarterfinals5} or (2) for {movie_quarterfinals6}: ")

if choice3_quarterfinals == "1":
    winner3_quarterfinals = movie_quarterfinals5
    print(f"The winner is {movie_quarterfinals5}!")
elif choice3_quarterfinals == "2":
    winner3_quarterfinals = movie_quarterfinals6
    print(f"The winner is {movie_quarterfinals6}!")
else:
    print("Invalid choice.")

choice4_quarterfinals = input(f"Choose the winner of this matchup by entering (1) for {movie_quarterfinals7} or (2) for {movie_quarterfinals8}: ")

if choice4_quarterfinals == "1":
    winner4_quarterfinals = movie_quarterfinals7
    print(f"The winner is {movie_quarterfinals7}!")
elif choice4_quarterfinals == "2":
    winner4_quarterfinals = movie_quarterfinals8
    print(f"The winner is {movie_quarterfinals8}!")
else:
    print("Invalid choice.")

movies_semifinals = [winner1_quarterfinals, winner2_quarterfinals, winner3_quarterfinals, winner4_quarterfinals]

random.shuffle(movies_semifinals)

movie_semifinals1 = movies_semifinals[0]
movie_semifinals2 = movies_semifinals[1]
movie_semifinals3 = movies_semifinals[2]
movie_semifinals4 = movies_semifinals[3]

choice1_semifinals = input(f"Choose the winner of this matchup by entering (1) for {movie_semifinals1} or (2) for {movie_semifinals2}: ")

if choice1_semifinals == "1":
    winner1_semifinals = movie_semifinals1
    print(f"The winner is {movie_semifinals1}!")
elif choice1_semifinals == "2":
    winner1_semifinals = movie_semifinals2
    print(f"The winner is {movie_semifinals2}!")
else:
    print("Invalid choice.")

choice2_semifinals = input(f"Choose the winner of this matchup by entering (1) for {movie_semifinals3} or (2) for {movie_semifinals4}: ")

if choice2_semifinals == "1":
    winner2_semifinals = movie_semifinals3
    print(f"The winner is {movie_semifinals3}!")
elif choice2_semifinals == "2":
    winner2_semifinals = movie_semifinals4
    print(f"The winner is {movie_semifinals4}!")
else:
    print("Invalid choice.")

movies_final = [winner1_semifinals, winner2_semifinals]

random.shuffle(movies_final)

movie_final1 = movies_final[0]
movie_final2 = movies_final[1]

choice_final = input(f"Choose the winner of this movie tournament by entering (1) for {movie_final1} or (2) for {movie_final2}: ")

if choice_final == "1":
    winner_final = movie_final1
    print(f"The winner of this movie tournament is {movie_final1}! Enjoy the movie!")
elif choice_final == "2":
    winner_final = movie_final2
    print(f"The winner of this movie tournament is {movie_final2}! Enjoy the movie!")
else:
    print("Invalid choice.")
