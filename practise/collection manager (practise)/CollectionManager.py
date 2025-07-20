import csv

def addSong():
    song = input("Enter the song name: ")
    artist = input("Enter the artist: ")
    genre = input("Enter the genre of this song: ")
    album = input("Enter the albulm this song is in: ")
    year = input("Enter the year this song was released: ")

    with open("Collection.csv", "a", newline = "") as file:
        writer = csv.writer(file)
        writer.writerow([song, artist, genre, album, year])
    
    print("Song added successfully.")

def viewCollection():
    try:
        with open("Collection.csv", "r") as file:
            reader = csv.reader(file)
            print(f"Song | Artsit | Genre | Album | Year ")
            print("-" * 40)
            for row in reader:
                print(" | ".join(row))

    except FileNotFoundError:
        print("You don't have a music collection yet.")

while True:
    userInput = input("To add a song press 1 \nTo view your collection press 2 \nTo quit press 3 \n")
    if userInput == "1":
        addSong()

    elif userInput == "2":
        viewCollection()

    elif userInput == "3":
        break
    
    else:
        print("Please only enter 1, 2 or 3")
