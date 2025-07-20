import os
folder = "music player eva"

for fileName in os.listdir(folder):
    print(fileName)

text_file = [f for f in os.listdir(folder) if f.lower().endswith(".txt")] 
print("text files found :", text_file)

# lists everything in the current folder (that ends with .txt)