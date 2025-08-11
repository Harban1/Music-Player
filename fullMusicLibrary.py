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

        except Exception as e:
            print(f"Error deleting song: {e}")

    # def create playlist
    def createPlaylist(self):
        """creating new playlist """
        print("\nCreate playlist: ")

        playlistName = input("Enter the name of your new playlist: ").strip()
        if not playlistName:
            print("Your name cannot be empty.")
            return
        
        print("Add songs to playlist:")
        print("Enter song IDs of your songs then press enter or leave blank to end.")

        songIDs = []
        while True:
            songID = input("Enter song ID: ").strip()
            if not songID:
                break

            if self.songExists(songID):
                songIDs.append(songID)
                print(f"The song id {songID} is added to {playlistName}")
            else:
                print("This song doesnt exist.")
                return

        if songIDs: 

            try:     
                with open(self.playlist, "a", newline = "") as file:
                    writer = csv.writer(file)
                    
                    for songs in songIDs:
                        writer.writerow([playlistName,songs,datetime.now().strftime("%d-%m-%Y")])
                        print(f"'{playlistName}' is created with {len(songID)} songs.")

            except Exception as e:
                print(f"Playlist couldn't be made due to {e}")
        
        else:
            print("There is nothing in your playlist")
            return



    def songExists(self, songID):
        """check if song id is in library"""

        try:
            with open(self.libraryFile, "r") as file:
                reader = csv.reader(file)
                next(reader)

                for row in reader:
                    ids = row[0]
                    if ids == songID:
                        return True
                    
                return False
        
        except:
            return False

