# Python

A project for learning the basics of **Python** programming language. My purpose is to learn best practices for writing—in theory—production-grade **Python** that is clean, efficient, and maintainable.


## Table of Contents

- [Software Installation and Setup](https://github.com/Pece17/Python?tab=readme-ov-file#software-installation-and-setup)
- [Creating a Movie Tournament Program](https://github.com/Pece17/Python/blob/main/README.md#creating-a-movie-tournament-program)
- [Refining the Movie Tournament Program](https://github.com/Pece17/Python/blob/main/README.md#refining-the-movie-tournament-program)
    - [Tackling Redundancy](https://github.com/Pece17/Python/blob/main/README.md#tackling-redundancy)
    - [Replay the Tournament with Previously Entered Movies](https://github.com/Pece17/Python/tree/main?tab=readme-ov-file#replay-the-tournament-with-previously-entered-movies)
    - [Change Entered Movies Before Starting the Tournament](https://github.com/Pece17/Python/tree/main?tab=readme-ov-file#change-entered-movies-before-starting-the-tournament)


## Software Installation and Setup

First I need to set up the environment where I'll be writing **Python** codes and programs. Many people on **Reddit** suggest **Visual Studio Code**/**VS Code**, and it should do fine for simple programs at this stage. My antique desktop PC is still running **Windows 7** so I'll need a legacy **VS Code** version that supports it. A quick **Google** search reveals that **version 1.70** is what I'm looking for.

I go to https://code.visualstudio.com/updates/v1_70 and download the **x64** version. I go through the installation, use the default settings, after which **VS Code** launches.

**ChatGPT** says I should install **Python extension for Visual Studio Code**, so I select the **Extensions** icon on the left sidebar in **VS Code**, write **Python** on the search bar, and select **Install Release Version**.

After the installation is complete, I click **Create Python File** and save the file as **Hello_World.py**.

At this point I need to actually install **Python** on my computer, so I go to https://www.python.org/downloads/windows/, find version **3.8.6** (the latest compatible version with **Windows 7**), and download **Windows x86 executable installer**.

After downloading, I right-click on **python-3.8.6.exe**, select **Run as administrator**, unselect **Install launcher for all users (recommended)**, and click **Install Now**. I check that **Python** has been installed by opening **cmd.exe**/**Windows Command Prompt** and entering command ```py --version```. The terminal outputs ```Python 3.8.6```, so we're good to go.

Now I go back to **VS Code** and **Hello_World.py** file, and write a very simple program:

```
print("Hello, World!")
```

I try to run the code in **VS Code** by clicking the ▶️ (play) button, but get an error and a button saying **Select Python Interpreter**. I click on it, type **Python: Select Interpreter** on the search bar as per **ChatGPT**'s instructions, and paste the path of the **python.exe** file on my PC. In my case it is: ```C:\Users\Business\AppData\Local\Programs\Python\Python38-32\python.exe```. Now I run the file again, and get the following output:

```
Windows PowerShell
Copyright (C) 2009 Microsoft Corporation. All rights reserved.

PS C:\Users\Business> & C:/Users/Business/AppData/Local/Programs/Python/Python38-32/python.exe c:/Users/Business/Hello_World.py
Hello, World!
PS C:\Users\Business>
```

**VS Code** and **Python** seem to work correctly, so I can move on to more complex exercises.


## Creating a Movie Tournament Program

I've been learning the basics of **Python** for a few days now mainly via [W3Schools](https://www.w3schools.com/python/), and I'm interested in trying to create a small and relatively simple program. I often have a hard time decising a movie to watch from my watchlist, so I'm thinking a movie tournament **Python** program could be a fun and even useful idea.

The idea is to have 8 or 16 movies that are first entered into the program by typing or by retrieving from a list, and then they're randomly paired into 4 or 8 pairs. There will be:

- Round of 16 (if there are 16 movies)
- Quarterfinals
- Semifinals
- Final

The user will choose the winner from each pair by selecting **1** or **2** until there are only 2 movies left, after which the winner is declared. After this, the program should ask the user whether they want to create another tournament or to terminate the program. I start by creating **movie_tournament.py** file in **VS Code**. This is apparently the correct syntax for **Python** programs, using all-lowercase with optional underscores for readability.

To make it simpler, I'm going to make the tournament for only 8 movies at first. I can scale up later if necessary. This is the starting point for the code, 8 **variables** for 8 movies with **input functions**:

```
movie1 = input("Please, enter the 1st movie: ")
movie2 = input("Please, enter the 2nd movie: ")
movie3 = input("Please, enter the 3rd movie: ")
movie4 = input("Please, enter the 4th movie: ")
movie5 = input("Please, enter the 5th movie: ")
movie6 = input("Please, enter the 6th movie: ")
movie7 = input("Please, enter the 7th movie: ")
movie8 = input("Please, enter the 8th movie: ")
```

The code works as intended, and the output looks like this:

```
PS C:\Users\Business> & C:/Users/Business/AppData/Local/Programs/Python/Python38-32/python.exe c:/Users/Business/movie_tournament.py
Please, enter the 1st movie: The Last Samurai
Please, enter the 2nd movie: The Informant
Please, enter the 3rd movie: 
```

Though, this is probably not the most elegant way to code, especially if there would be many more **variables** to input. A some kind of dynamic method might be ideal, but this will do for this program.

Now we need to somehow shuffle/randomize the 8 movies into 4 pairs. I **Google** this problem and find the following method:

```
import random

mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)

print(mylist)
```

Based on that, I make the following additions to my code:

```
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
```

I ask **ChatGPT** advice about how to fetch the **shuffled** movies without printing them, and learn the following method:

```
movie_quarterfinals1 = movies_quarterfinals[0]
movie_quarterfinals2 = movies_quarterfinals[1]
movie_quarterfinals3 = movies_quarterfinals[2]
movie_quarterfinals4 = movies_quarterfinals[3]
movie_quarterfinals5 = movies_quarterfinals[4]
movie_quarterfinals6 = movies_quarterfinals[5]
movie_quarterfinals7 = movies_quarterfinals[6]
movie_quarterfinals8 = movies_quarterfinals[7]
```

Next I learn the method for creating matchups between 2 **variables**. We use ```f``` to format strings like this: ```print(f"The winner is {movie_quarterfinals1}!")```. Otherwise the output would literally show ```The winner is movie_quarterfinals1!```.:

```
choice1_quarterfinals = input(f"Choose the winner of this matchup by entering (1) for {movie_quarterfinals1} or (2) for {movie_quarterfinals2}: ")

if choice1_quarterfinals == "1":
    print(f"The winner is {movie_quarterfinals1}!")
elif choice1_quarterfinals == "2":
    print(f"The winner is {movie_quarterfinals2}!")
else:
    print("Invalid choice.")
```

At this point I don't yet know a more sophisticated method for handling all these matchups, so I'm just literally copy-pasting the code above and changing the **variable** names. Now the whole code looks as follows:

```
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
    print(f"The winner is {movie_quarterfinals1}!")
elif choice1_quarterfinals == "2":
    print(f"The winner is {movie_quarterfinals2}!")
else:
    print("Invalid choice.")

choice2_quarterfinals = input(f"Choose the winner of this matchup by entering (1) for {movie_quarterfinals3} or (2) for {movie_quarterfinals4}: ")

if choice2_quarterfinals == "1":
    print(f"The winner is {movie_quarterfinals3}!")
elif choice2_quarterfinals == "2":
    print(f"The winner is {movie_quarterfinals4}!")
else:
    print("Invalid choice.")

choice3_quarterfinals = input(f"Choose the winner of this matchup by entering (1) for {movie_quarterfinals5} or (2) for {movie_quarterfinals6}: ")

if choice3_quarterfinals == "1":
    print(f"The winner is {movie_quarterfinals5}!")
elif choice3_quarterfinals == "2":
    print(f"The winner is {movie_quarterfinals6}!")
else:
    print("Invalid choice.")

choice4_quarterfinals = input(f"Choose the winner of this matchup by entering (1) for {movie_quarterfinals7} or (2) for {movie_quarterfinals8}: ")

if choice4_quarterfinals == "1":
    print(f"The winner is {movie_quarterfinals7}!")
elif choice4_quarterfinals == "2":
    print(f"The winner is {movie_quarterfinals8}!")
else:
    print("Invalid choice.")
```

I'm new to **Python**, but I can already tell that this is not the ideal way to code. There's a lot of redundancy when you could definitely make the code more dynamic. However, we can refine the code later on. What's important is that the code works, and I get the following output:

```
PS C:\Users\Business> & C:/Users/Business/AppData/Local/Programs/Python/Python38-32/python.exe c:/Users/Business/movie_tournament.py
Please, enter the 1st movie: volvo
Please, enter the 2nd movie: lancia
Please, enter the 3rd movie: mersu
Please, enter the 4th movie: volkkari
Please, enter the 5th movie: ferrari
Please, enter the 6th movie: lambo
Please, enter the 7th movie: porsche
Please, enter the 8th movie: maybach
Choose the winner of this matchup by entering (1) for maybach or (2) for porsche: 1
The winner is maybach!
Choose the winner of this matchup by entering (1) for lancia or (2) for mersu: 1
The winner is lancia!
Choose the winner of this matchup by entering (1) for ferrari or (2) for volvo: 1
The winner is ferrari!
Choose the winner of this matchup by entering (1) for volkkari or (2) for lambo: 2
The winner is lambo!
PS C:\Users\Business> 
```

We need a way to store the winners of the quarterfinals, so I ask **ChatGPT** to explain the method. I make the following additions to all the quarterfinals:

```
if choice1_quarterfinals == "1":
    winner1_quarterfinals = movie_quarterfinals1
    print(f"The winner is {movie_quarterfinals1}!")
elif choice1_quarterfinals == "2":
    winner1_quarterfinals = movie_quarterfinals2
    print(f"The winner is {movie_quarterfinals2}!")
else:
    print("Invalid choice.")
```

Now I use the same logic for semifinals as I did for quarterfinals. We don't need to ```import random``` module again, though.

```
movies_semifinals = [winner1_quarterfinals, winner2_quarterfinals, winner3_quarterfinals, winner4_quarterfinals]

random.shuffle(movies_semifinals)

movie_semifinals1 = movies_semifinals[0]
movie_semifinals2 = movies_semifinals[1]
movie_semifinals3 = movies_semifinals[2]
movie_semifinals4 = movies_semifinals[3]
```

Once again, we just copy-paste the matchup logic of the quarterfinals for the semifinals:

```
choice1_semifinals = input(f"Choose the winner of this matchup by entering (1) for {movie_semifinals1} or (2) for {movie_semifinals2}: ")

if choice1_semifinals == "1":
    winner1_semifinals = movie_semifinals1
    print(f"The winner is {movie_semifinals1}!")
elif choice1_semifinals == "2":
    winner1_semifinals = movie_semifinals2
    print(f"The winner is {movie_semifinals2}!")
else:
    print("Invalid choice.")
```

Next we shuffle the winners of the semifinals by using the previous logic, though this is not really necessary because there are only 2 movies left:

```
movies_final = [winner1_semifinals, winner2_semifinals]

random.shuffle(movies_final)

movie_final1 = movies_final[0]
movie_final2 = movies_final[1]
```

Lastly, I use the previous matchup logic for the grand final:

```
choice_final = input(f"Choose the winner of this movie tournament by entering (1) for {movie_final1} or (2) for {movie_final2}: ")

if choice_final == "1":
    winner_final = movie_final1
    print(f"The winner of this movie tournament is {movie_final1}! Enjoy the movie!")
elif choice_final == "2":
    winner_final = movie_final2
    print(f"The winner of this movie tournament is {movie_final2}! Enjoy the movie!")
else:
    print("Invalid choice.")
```

Here's the whole shebang:

```
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
```

The program works as intended, and here's the proof from the ouput:

```
PS C:\Users\Business> & C:/Users/Business/AppData/Local/Programs/Python/Python38-32/python.exe c:/Users/Business/movie_tournament.py
Please, enter the 1st movie: The Last Samurai
Please, enter the 2nd movie: Mr. Baseball
Please, enter the 3rd movie: You've Got Mail
Please, enter the 4th movie: The Informant
Please, enter the 5th movie: The Natural
Please, enter the 6th movie: The Truman Show
Please, enter the 7th movie: Benjamin Button
Please, enter the 8th movie: your name.
Choose the winner of this matchup by entering (1) for The Truman Show or (2) for Mr. Baseball: 2
The winner is Mr. Baseball!
Choose the winner of this matchup by entering (1) for your name. or (2) for The Natural: 2
The winner is The Natural!
Choose the winner of this matchup by entering (1) for The Last Samurai or (2) for Benjamin Button: 1
The winner is The Last Samurai!
Choose the winner of this matchup by entering (1) for The Informant or (2) for You've Got Mail: 2
The winner is You've Got Mail!
Choose the winner of this matchup by entering (1) for Mr. Baseball or (2) for The Last Samurai: 2
The winner is The Last Samurai!
Choose the winner of this matchup by entering (1) for The Natural or (2) for You've Got Mail: 2
The winner is You've Got Mail!
Choose the winner of this movie tournament by entering (1) for You've Got Mail or (2) for The Last Samurai: 2
The winner of this movie tournament is The Last Samurai! Enjoy the movie!
PS C:\Users\Business> 
```

A stunning success, though I already have a lot of ideas how to refine the code for the **2.0 version**.


## Refining the Movie Tournament Program

As it stands, the code of the movie tournament program is quite rudimentary. I have come up with the following ideas to make the program more sophisticated:

- make the matchups and the whole tournament less redundant and more dynamic to reduce the amount of unnecessary code ✅
- specify the stage of the tournament during each matchup, for example: ```Choose the winner of the 4th quarterfinal matchup by entering (1) for The Informant or (2) for You've Got Mail: ``` ✅
- loops to start the matchups again if the user enters a wrong input ✅
- an option to redo any matchup if the user makes a typing mistake or changes their mind
- the ability to go back in stages
- the ability to choose between 8 or 16 movies for the tournament
- being able to fetch movie lists from **.txt files**, **CSV files**, or other files
- the program shouldn't automatically terminate when a tournament is finished—it should ask whether to redo with the same movies, to start a completely new tournament, or to close the program ✅
- a better user interface instead of just command line
- general polishing at the very end of the project

Specifying the stage of the tournament during each matchup is simple enough, just changing what the **input** message says:

```
choice1_semifinals = input(f"Choose the winner of the 1st semifinal matchup by entering (1) for {movie_semifinals1} or (2) for {movie_semifinals2}: ")

if choice1_semifinals == "1":
    winner1_semifinals = movie_semifinals1
    print(f"The winner is {movie_semifinals1}!")
elif choice1_semifinals == "2":
    winner1_semifinals = movie_semifinals2
    print(f"The winner is {movie_semifinals2}!")
else:
    print("Invalid choice.")
```

The output of that looks like this:

```
Choose the winner of the 1st semifinal matchup by entering (1) for lancia or (2) for volvo: 1
The winner is lancia!
```

Next I ask **ChatGPT** for help about how to create loops withing matchups, so that the program will not advance until either **1** or **2** has been entered. The method is ```while True```. I also reduce complexity by changing the **variable** in ```print(f"The winner is {movie_quarterfinals1}!")``` to ```{winner1_quarterfinals}```, and apply the same logic to other matchups too. We use ```break``` statements to exit out of the loops. The matchups look like this now:

```
while True:
    choice1_quarterfinals = input(f"Choose the winner of the 1st quarterfinal matchup by entering (1) for {movie_quarterfinals1} or (2) for {movie_quarterfinals2}: ")

    if choice1_quarterfinals == "1":
        winner1_quarterfinals = movie_quarterfinals1
        print(f"The winner is {winner1_quarterfinals}!")
        break
    elif choice1_quarterfinals == "2":
        winner1_quarterfinals = movie_quarterfinals2
        print(f"The winner is {winner1_quarterfinals}!")
        break
    else:
        print("Invalid choice.")
```

For more complex features, I'll make subheadings in this **GitHub** page for better readability.


### Tackling Redundancy

Perhaps the biggest issue of the current code is its redundancy: for example, using the same block of code 4 times during the quarterfinals and 2 times during the semifinals. I want to learn a more elegant way to write **Python**. Again, I ask **ChatGPT** for help.

First on the chopping block are these 8 lines, because they are actually not needed:

```
movie_quarterfinals1 = movies_quarterfinals[0]
movie_quarterfinals2 = movies_quarterfinals[1]
movie_quarterfinals3 = movies_quarterfinals[2]
movie_quarterfinals4 = movies_quarterfinals[3]
movie_quarterfinals5 = movies_quarterfinals[4]
movie_quarterfinals6 = movies_quarterfinals[5]
movie_quarterfinals7 = movies_quarterfinals[6]
movie_quarterfinals8 = movies_quarterfinals[7]
```

Instead, we can just do the following to create **tuples** (immutable or unchangeable objects), and use them as matchups. Each **tuple** is one matchup, and they are randomized because of ```random.shuffle```:

```
quarterfinals = [
    (movies_quarterfinals[0], movies_quarterfinals[1]),
    (movies_quarterfinals[2], movies_quarterfinals[3]),
    (movies_quarterfinals[4], movies_quarterfinals[5]),
    (movies_quarterfinals[6], movies_quarterfinals[7])
]
```

The code before the matchups now looks like this:

```
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

quarterfinals = [
    (movies_quarterfinals[0], movies_quarterfinals[1]),
    (movies_quarterfinals[2], movies_quarterfinals[3]),
    (movies_quarterfinals[4], movies_quarterfinals[5]),
    (movies_quarterfinals[6], movies_quarterfinals[7])
]
```

We can also reduce redundancy by changing how the program collects the movies. I'll try to explain how this line of code works: **square brackets** ```[]``` immediately create a **variable** and a **list** called ```movies_quarterfinals```; within the **square brackets** there is ```input``` **function**, **parentheses** ```()```, **f-string** ```f``` for enabling **variables** and **expressions** inside **curly brackets** ```{}```, the written **string** inside **double quotes** ```""```, and ```{i+1}``` within the **string**. It is apparently common practice to use ```i``` for simple **loops** where the meaning is obvious. The ```+1``` is important because **Python** starts **lists** from **0**, and in this case we want a list between **1**–**8**. Lastly, the ```for``` **loop** lets **Python** repeat a block of code a fixed number of times, the ```i``` is our **variable** within this **loop**, ```in``` connects the **variable** to a sequence of values, and ```range(8)``` is the sequence of our chosen numbers (**0** to **7**). The user will see these from **1** to **8**.

```
movies_quarterfinals = [input(f"Please, enter movie No. {i+1}: ") for i in range(8)]
```

The beginning of the code now looks like this:

```
movies_quarterfinals = [input(f"Please, enter movie No. {i+1}: ") for i in range(8)]

import random

random.shuffle(movies_quarterfinals)

quarterfinals = [
    (movies_quarterfinals[0], movies_quarterfinals[1]),
    (movies_quarterfinals[2], movies_quarterfinals[3]),
    (movies_quarterfinals[4], movies_quarterfinals[5]),
    (movies_quarterfinals[6], movies_quarterfinals[7])
]
```

The code works as intended:

```
PS C:\Users\Business> & C:/Users/Business/AppData/Local/Programs/Python/Python38-32/python.exe c:/Users/Business/movie_tournament_v1.1.py
Please, enter movie No. 1: asd
Please, enter movie No. 2: asd
Please, enter movie No. 3: sad
Please, enter movie No. 4: asd
Please, enter movie No. 5: asd
Please, enter movie No. 6: asd
Please, enter movie No. 7: asd
Please, enter movie No. 8: asd
```

Next we initialize a ```winners_quarterfinals``` **list**, that will be used in the quarterfinals:

```
winners_quarterfinals = []
```

Next we need to create a new dynamic **loop** for all the quarterfinal matchups:

- ```for i``` creates a **for-loop**.
- ```(movie1, movie2)``` are the movies for each **tuple**—each **tuple** represents one matchup, as we learned previously.
- ```in``` connects the **loop** **variable** (```i```) to the **iterable** ```enumerate(quarterfinals, start=1)```. In **Python**, an **iterable** is any object that you can **loop** over (**list**, **tuple**, **string**, etc.).
- ```enumerate()``` adds a counter to your **iterable** and returns an **enumerable object** (**iterator**) that produces pairs of (**index**, **item**). Basically, ```enumerate()``` adds a number to each item while looping.
- ```quarterfinals``` is the list of matchups to loop over (**iterable**) and ```start=1``` sets the starting number for the **index** as **1**, because otherwise **Python** will set it as **0**.
- ```while True``` we have already covered previously. ```choice = input(f"Choose the winner of the quarterfinal matchup No. {i} by entering (1) for {movie1} or (2) for {movie2}: ")``` gets the matchup number dynamically, whereas before it was hardcoded.
- In ```winners_quarterfinals.append(movie1)```, ```append()``` adds an element (```movie1```) to the end of the list (```winners_quarterfinals```).
- ```break``` stops the current loop immediately. After ```break```, **Python** jumps to the code right after the loop.

We can use the same logic in the semifinals and the final too:

```
for i, (movie1, movie2) in enumerate(quarterfinals, start=1):
    while True:
        choice = input(f"Choose the winner of the quarterfinal matchup No. {i} by entering (1) for {movie1} or (2) for {movie2}: ")
        
        if choice == "1":
            winners_quarterfinals.append(movie1)
            print(f"The winner of the quarterfinal matchup No. {i} is {movie1}!")
            break
        
        elif choice == "2":
            winners_quarterfinals.append(movie2)
            print(f"The winner of the quarterfinal matchup No. {i} is {movie2}!")
            break
        
        else:
            print("Invalid choice. Please, enter (1) or (2).")
```

After this we **shuffle** the ```winners_quarterfinals``` **list**, create **tuples** (matchups) from the ```winners_quarterfinals``` **items**, and initialize the ```winners_semifinals``` **list**:

```
random.shuffle(winners_quarterfinals)

    semifinals = [
        (winners_quarterfinals[0], winners_quarterfinals[1]),
        (winners_quarterfinals[2], winners_quarterfinals[3])
    ]

    winners_semifinals = []
```

We use a similar **for-loop** with the semifinals as we did with the quarterfinals:

```
for i, (movie1, movie2) in enumerate(semifinals, start=1):
        while True:
            choice = input(f"Choose the winner of the semifinal matchup No. {i} by entering (1) for {movie1} or (2) for {movie2}: ")
            
            if choice == "1":
                winners_semifinals.append(movie1)
                print(f"The winner of the semifinal matchup No. {i} is {movie1}!")
                break
            
            elif choice == "2":
                winners_semifinals.append(movie2)
                print(f"The winner of the semifinal matchup No. {i} is {movie2}!")
                break
            
            else:
                print("Invalid choice. Please, enter (1) or (2).")
```

Next, we **shuffle** the winners of the semifinals (which is arguably not necessary for the final), create ```movie1``` and ```movie2``` **variables** from the ```winners_semifinals``` **list**, and use the same matchup-logic as previously:

```
random.shuffle(winners_semifinals)

    movie1, movie2 = winners_semifinals

    while True:
        choice = input(f"Choose the winner of the movie tournament by entering (1) for {movie1} or (2) for {movie2}: ")
            
        if choice == "1":
            winner_grandfinal = movie1
            print(f"The winner of the movie tournament is {movie1}! Enjoy the movie!")
            break
            
        elif choice == "2":
            winner_grandfinal = movie2
            print(f"The winner of the movie tournament is {movie2}! Enjoy the movie!")
            break
            
        else:
            print("Invalid choice. Please, enter (1) or (2).")
```

Finally, we create an infinite **loop** for the whole tournament, and the possibilities to either redo or exit the program:

- We give the **variable** ```running``` the **boolean** value ```True```. A **boolean** is a type of value in programming that can be only one of two states: ```True``` or ```False```.
- ```while running``` therefore behaves exactly like ```while True```.
- We also create a loop at the end of the code where entering **1** will start the program again and entering **2** will change the value of ```running``` as ```False```, terminating the program and printing a goodbye message.

```
running = True

while running:

    (code of the program)

    while True:
        again = input("Enter (1) to to create a new tournament or enter (2) to exit: ")

        if again == "1":
            break
        
        elif again == "2":
            print("Thanks for playing!")
            running = False
            break

        else:
            print("Invalid choice. Please, enter (1) or (2).")
```

The whole code now looks like this:

```
import random

running = True

while running:
    movies_quarterfinals = [input(f"Please, enter movie No. {i+1}: ") for i in range(8)]

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
            choice = input(f"Choose the winner of the quarterfinal matchup No. {i} by entering (1) for {movie1} or (2) for {movie2}: ")
            
            if choice == "1":
                winners_quarterfinals.append(movie1)
                print(f"The winner of the quarterfinal matchup No. {i} is {movie1}!")
                break
            
            elif choice == "2":
                winners_quarterfinals.append(movie2)
                print(f"The winner of the quarterfinal matchup No. {i} is {movie2}!")
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
            choice = input(f"Choose the winner of the semifinal matchup No. {i} by entering (1) for {movie1} or (2) for {movie2}: ")
            
            if choice == "1":
                winners_semifinals.append(movie1)
                print(f"The winner of the semifinal matchup No. {i} is {movie1}!")
                break
            
            elif choice == "2":
                winners_semifinals.append(movie2)
                print(f"The winner of the semifinal matchup No. {i} is {movie2}!")
                break
            
            else:
                print("Invalid choice. Please, enter (1) or (2).")

    random.shuffle(winners_semifinals)

    movie1, movie2 = winners_semifinals

    while True:
        choice = input(f"Choose the winner of the movie tournament by entering (1) for {movie1} or (2) for {movie2}: ")
            
        if choice == "1":
            winner_grandfinal = movie1
            print(f"The winner of the movie tournament is {movie1}! Enjoy the movie!")
            break
            
        elif choice == "2":
            winner_grandfinal = movie2
            print(f"The winner of the movie tournament is {movie2}! Enjoy the movie!")
            break
            
        else:
            print("Invalid choice. Please, enter (1) or (2).")

    while True:
        again = input("Enter (1) to create a new tournament or enter (2) to exit: ")

        if again == "1":
            break
        
        elif again == "2":
            print("Thanks for playing!")
            running = False
            break

        else:
            print("Invalid choice.")
```

The program works as intended (I really should finally watch **You've Got Mail**...):

```
PS C:\Users\Business> & C:/Users/Business/AppData/Local/Programs/Python/Python38-32/python.exe c:/Users/Business/movie_tournament_v1.1.py
Please, enter movie No. 1: The Truman Show
Please, enter movie No. 2: You've Got Mail
Please, enter movie No. 3: your name.
Please, enter movie No. 4: The Natural
Please, enter movie No. 5: The Informant
Please, enter movie No. 6: Kramer vs. Kramer
Please, enter movie No. 7: Mr. Baseball
Please, enter movie No. 8: Kenny
Choose the winner of the quarterfinal matchup No. 1 by entering (1) for Mr. Baseball or (2) for You've Got Mail: 2
The winner of the quarterfinal matchup No. 1 is You've Got Mail!
Choose the winner of the quarterfinal matchup No. 2 by entering (1) for The Truman Show or (2) for Kramer vs. Kramer: 1
The winner of the quarterfinal matchup No. 2 is The Truman Show!
Choose the winner of the quarterfinal matchup No. 3 by entering (1) for Kenny or (2) for The Informant: 2
The winner of the quarterfinal matchup No. 3 is The Informant!
Choose the winner of the quarterfinal matchup No. 4 by entering (1) for your name. or (2) for The Natural: 2
The winner of the quarterfinal matchup No. 4 is The Natural!
Choose the winner of the semifinal matchup No. 1 by entering (1) for The Truman Show or (2) for You've Got Mail: 2
The winner of the semifinal matchup No. 1 is You've Got Mail!
Choose the winner of the semifinal matchup No. 2 by entering (1) for The Informant or (2) for The Natural: 2
The winner of the semifinal matchup No. 2 is The Natural!
Choose the winner of the movie tournament by entering (1) for The Natural or (2) for You've Got Mail: 2
The winner of the movie tournament is You've Got Mail! Enjoy the movie!
Enter (1) to create a new tournament or enter (2) to exit: 3
Invalid choice.
Enter (1) to create a new tournament or enter (2) to exit: 2
Thanks for playing!
PS C:\Users\Business>
```

We have now succesfully made the program more dynamic and less redundant. Onto further improvements.


### Replay the Tournament with Previously Entered Movies

It is burdensome having to always enter the movies again if you want to replay the tournament. We need to add a way store the movies that were entered during the first playthrough, so that the user can choose to redo the tournament with said movies without further inputs.

First, let's add ```movies_quarterfinals = []``` at the beginning of the code. This stores the **list of movies** outside the **main loop** and gives the user the option to reuse it.

```
import random

running = True

movies_quarterfinals = []
```

Next we'll add ```if not movies_quarterfinals:```, where ```if``` checks whether the condition is **True** and ```not``` reverses the truth value of the **expression**. In this context it means that ```if not``` statement checks whether the ```movies_quarterfinals``` **list** is empty, and asks to input movies if the list *is* empty or skips the stage if the list *already has movies*.

```
while running:
    if not movies_quarterfinals:
        movies_quarterfinals = [input(f"Please, enter movie No. {i+1}: ") for i in range(8)]

    random.shuffle(movies_quarterfinals)

    quarterfinals = [
        (movies_quarterfinals[0], movies_quarterfinals[1]),
        (movies_quarterfinals[2], movies_quarterfinals[3]),
        (movies_quarterfinals[4], movies_quarterfinals[5]),
        (movies_quarterfinals[6], movies_quarterfinals[7])
    ]
```

Finally, we add another ```elif``` (**else if**) **clause** to the **statement** at the end of the code where ```movies_quarterfinals = []``` resets the **movie list** and creates a fresh tournament.

```
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
```

I run the program and the new feature seems to work, though the matchups are randomized again in the quarterfinals. I'm not sure if this is better vs. using the same matchups as in the first playthrough. It's a matter of opinion really—I'll leave the code as is for now.

```
PS C:\Users\Business> & C:/Users/Business/AppData/Local/Programs/Python/Python38-32/python.exe c:/Users/Business/movie_tournament_v1.1.py
Please, enter movie No. 1: It's a Wonderful Life
Please, enter movie No. 2: Failure to Launch
Please, enter movie No. 3: The Pursuit of Happyness
Please, enter movie No. 4: Mr. Baseball
Please, enter movie No. 5: The Natural
Please, enter movie No. 6: The Truman Show
Please, enter movie No. 7: Sleepless in Seattle
Please, enter movie No. 8: You've Got Mail
Choose the winner of the quarterfinal matchup No. 1 by entering (1) for Sleepless in Seattle or (2) for The Natural: 1
The winner of the quarterfinal matchup No. 1 is Sleepless in Seattle!
Choose the winner of the quarterfinal matchup No. 2 by entering (1) for It's a Wonderful Life or (2) for The Pursuit of Happyness: 2
The winner of the quarterfinal matchup No. 2 is The Pursuit of Happyness!
Choose the winner of the quarterfinal matchup No. 3 by entering (1) for You've Got Mail or (2) for Failure to Launch: 1
The winner of the quarterfinal matchup No. 3 is You've Got Mail!
Choose the winner of the quarterfinal matchup No. 4 by entering (1) for Mr. Baseball or (2) for The Truman Show: 1
The winner of the quarterfinal matchup No. 4 is Mr. Baseball!
Choose the winner of the semifinal matchup No. 1 by entering (1) for Sleepless in Seattle or (2) for The Pursuit of Happyness: 1
The winner of the semifinal matchup No. 1 is Sleepless in Seattle!
Choose the winner of the semifinal matchup No. 2 by entering (1) for Mr. Baseball or (2) for You've Got Mail: 2
The winner of the semifinal matchup No. 2 is You've Got Mail!
Choose the winner of the movie tournament by entering (1) for Sleepless in Seattle or (2) for You've Got Mail: 2
The winner of the movie tournament is You've Got Mail! Enjoy the movie!
Enter (1) to replay the tournament with the same movies, enter (2) to create a new tournament, or enter (3) to exit: 4
Invalid choice.
Enter (1) to replay the tournament with the same movies, enter (2) to create a new tournament, or enter (3) to exit: 1
Choose the winner of the quarterfinal matchup No. 1 by entering (1) for It's a Wonderful Life or (2) for You've Got Mail:
```

The whole code looks like this now:

```
import random

running = True

movies_quarterfinals = []

while running:
    if not movies_quarterfinals:
        movies_quarterfinals = [input(f"Please, enter movie No. {i+1}: ") for i in range(8)]

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
            choice = input(f"Choose the winner of the quarterfinal matchup No. {i} by entering (1) for {movie1} or (2) for {movie2}: ")
            
            if choice == "1":
                winners_quarterfinals.append(movie1)
                print(f"The winner of the quarterfinal matchup No. {i} is {movie1}!")
                break
            
            elif choice == "2":
                winners_quarterfinals.append(movie2)
                print(f"The winner of the quarterfinal matchup No. {i} is {movie2}!")
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
            choice = input(f"Choose the winner of the semifinal matchup No. {i} by entering (1) for {movie1} or (2) for {movie2}: ")
            
            if choice == "1":
                winners_semifinals.append(movie1)
                print(f"The winner of the semifinal matchup No. {i} is {movie1}!")
                break
            
            elif choice == "2":
                winners_semifinals.append(movie2)
                print(f"The winner of the semifinal matchup No. {i} is {movie2}!")
                break
            
            else:
                print("Invalid choice. Please, enter (1) or (2).")

    random.shuffle(winners_semifinals)

    movie1, movie2 = winners_semifinals

    while True:
        choice = input(f"Choose the winner of the movie tournament by entering (1) for {movie1} or (2) for {movie2}: ")
            
        if choice == "1":
            winner_grandfinal = movie1
            print(f"The winner of the movie tournament is {movie1}! Enjoy the movie!")
            break
            
        elif choice == "2":
            winner_grandfinal = movie2
            print(f"The winner of the movie tournament is {movie2}! Enjoy the movie!")
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
```

Moving on to other improvements.


### Change Entered Movies Before Starting the Tournament

Sometimes the user can make a mistake or change their mind when it comes to the movies that will participate in a tournament. There should be an ability to correct and change the entered movies before starting the tournament proper.

