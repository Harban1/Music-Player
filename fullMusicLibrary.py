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



        def viewlibrary():

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
            
            
            
            