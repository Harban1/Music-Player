import csv
import os
from datetime import datetime

class MusicLibrary:
    def __init__(self):
        self.libraryFile = "library.csv"
        self.playlist = "playlist.csv"
        self.createFiles()

    def createFiles(self):
        if not os.path.exists(self.libraryFile):
            with open(self.libraryFile, "w", newline = "") as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "Title", "Artist", "Album", "Year", "Genre", "Duration"])

        if not os.path.exists(self.playlist):
            with open(self.playlist, "w", newline = "") as file:
                writer = csv.writer(file)
                writer.writerow(["playlist", "SongID", "dateAdded"])

    def generateID(self):
        try:
            with open(self.libraryFile, "r") as file:
                reader = csv.reader(file)
                next(reader)
                id = [int(row[0]) for row in reader if row]
                return max(id) + 1 if id else 1
        except (FileNotFoundError, ValueError):
            return 1
        
    
    def addSong(self):
        print("Adding new song: ")
        try:
            title = input("Enter song title: ").strip()
            if not title:
                print("Please enter a title")
                return
            
            artist = input("Enter song artist: ").strip()
            if not artist:
                print("Please enter an artist")
                return
            
            album = input("Enter song album: ").strip()
            if not album:
                print("Please enter an album")
                return
            
            while True:
                yearInput = input("year: ").strip()
                if yearInput.isdigit() and len(yearInput) == 4:
                    year = int(yearInput)
                    break
                else:
                    print("Please enter a valid year")

            genre = input("Enter song genre: ").strip()
            if not genre:
                print("Please enter a genre")
                return
            
            duration = input("Enter song duration: ").strip()
            if not duration:
                print("Please enter a duration")
                return
                    
            
            songid = self.generateID()

            with open(self.libraryFile, "a", newline = "") as file:
                writer = csv.writer(file)
                writer.writerow([songid, title, artist, album, year, genre, duration])

            print("song added successfully")

        except (FileNotFoundError, ValueError):
                return 1



    def viewlibrary(self):

        print("Display library: ")

        try:
            with open(self.libraryFile, "r") as file:
                reader = csv.reader(file)
                header = next(reader)  # stores first line and goes to next line

                songs = list(reader)
                if not songs:
                    print("You have no songs in your library. ")
                    return
                
                # print("header", header)
                print(" | ".join(header))
                print("-" * 90)


                # print ID, title, ... under 20 characters
                for row in reader:
                    if len(row) > 20:
                        row = row[:20] + "..."
                    print(" | ".join(row))
                     
                    
               
        except (FileNotFoundError, ValueError):
            return 1
            
            
    def searchSong(self):

        print("Searching song ")

        searchBy = int(input("Do you want to search by artist (type '1') or genre (type '2') ? : "))

        # if user doesnt enter 1 or 2, message 
        # if 1 then input artist name
        # else input genre name

        if searchBy == "1" or searchBy == "2":
            if searchBy == "1":
                artistname = input("Enter artist name: ")
            else:
                genretype = input("Enter genre type: ")
        else:
            print("Please only enter either 1 or 2.")
            self.searchSong()

    

        try:
            with open(self.libraryFile, "r") as file:
                reader = csv.reader(file)
                header = next(reader)
                
                foundSongs = []
                artistsongs = []

                for row in reader:
                    if searchBy == "1":
                        artist = row[2]
                        if artist == artistname:
                            foundSongs.append(row)
                    else:
                        genre = row[5]
                        if genre == genretype:
                            foundSongs.append(row)

                if foundSongs:
                    if searchBy == "1":
                        print(f"Found {len(foundSongs)} songs with '{artistname}' artist")
                    else:
                        print(f"Found {len(foundSongs)} songs with '{genretype}' genre")

                else:
                    print("Found no songs with your search")

        except FileNotFoundError:
            print("No music library found.")
        
        except Exception as e :
            print(f"error searching: {e}")

    
    def deleteSong(self):

        """ delete songs from library """

        try:
            deleteSongID = int(input("Enter the ID of the song you want to delete: ")).strip()
            with open(self.libraryFile, "r") as file:
                reader = csv.reader(file)
                header = next(reader)

                songs = [header]
            
                for row in reader:
                    id = int(row[0])
                    if id == deleteSongID:

                        deletesonginput = input(f"Do you want to delete '{row[1]}' by {row[2]}? y/n").lower()
                        if deletesonginput == "n":
                            print("delete cancelled.")
                            songs.append(row)

                        elif deletesonginput == "y":
                            print(f"The song '{row[1]}' by '{row[2]}' has been deleted")
                    else:
                        songs.append(row)

                with open(self.library, "w", newline = "") as file:
                    writer = csv.writer(file)
                    writer.writerow(songs)

        # write exceptions

    # def create playlist
    # print "create playlist"
    # ask playlist name plus strip
    # if user doesnt enter anything print playlist name cant be empty and return
    # print add songs to playlist
    # enter the song ids and press enter when done
    # while loop while true
    # input list songID
    # enter song id or press enter to finish + strip
    # if input is empty then break
    # if valid song id exists
    # assume "songexists" func
    # if songexists(songid)
    # then append songID to list Song ID
    # print song id added to playlist
    # else song id not found
    # open playlist file and append song
    # csv.writer
    # for loop for songid in songids
    # playlist name, song id, current date, current time
    # print(playlist created with (no of songs) songs)
    # expections




















                            
                        
                




            