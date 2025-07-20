name = input("Enter a name: ")

with open("names.txt", "a", encoding= "utf-8") as file:
    file.write(f"{name}\n")

