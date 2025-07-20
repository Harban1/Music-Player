def addFavourite():
    favSong = input("Enter your favourite song: ")
    Artist = input("Enter the artist: ")

    with open("favourites.txt", "a", encoding = "utf-8") as file:
        file.write(f"{favSong} by {Artist}\n")

    print("Your song has been added to favourites.")

def viewFavourite():
    try: 
        with open("favourites.txt", "r", encoding= "utf-8") as file:
            favourites = file.read()
            print("Here are your favourite songs:")
            print(favourites)

    
    except FileNotFoundError:
        print("Couldn't find 'favourites.txt'")

def main():
    option = input("Would you like to add a new favourite song (enter 1) or view all your favourites (enter 2): ")
    if option == "1":
        addFavourite()
    elif option == "2":
        viewFavourite()
    else:
        print("Sorry please either press 1 or 2")
        main()

main()