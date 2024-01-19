#Daniel, Bakari, Jonathan
# Period 4
#To Do List
#1/10/24

x=["Fight Club", "Strike 4", "Road to El Dorado", "Creed III", "It", "Karate Kid", "John Wick"]
3

#Displays a list of movies and allows user to amend and mark movies as seen
def menu():
    global list
    global watchmovie
    global moviewatched
    global x
    while True:
        print("Welcome to the movie watch list")
        print("Please select an option using 1-5")
        print("1. Add a movie to the list \n2. View the current watchlist \n3. Mark a movie as watched \n4. Remove a movie from the watchlist \n5. Exit the Program \n6. Clear List \n7. display number of movies in list \n8. Sort list alphabetically")
        option = int(input("option: "))
        if option==8:
            list=sorted(x)
            print(list)
        if option==6:
            x.clear()
        if option==7:
            list=len(x)
            print(list)
        if option == 5:
            quit()
        if option == 1:
            x.append(input("what movie would you like to add?"))
        if option == 2:
            print(x)
        if option == 3:
            watchmovie = str((input("What movie did you watch?")))
            moviewatched = x.index(watchmovie)
            x[moviewatched] = (watchmovie + " X")
        if option == 4:
            x.remove(input("What movie do you want to remove?"))
menu()