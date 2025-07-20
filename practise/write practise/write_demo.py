fileName = "NewTExt.txt"

with open(fileName, "w", encoding = "utf-8") as file:
    file.write("hello world\n")

try :
    with open(fileName, "a", encoding = "utf-8") as file:
        file.write("NEW LINE")

except FileNotFoundError:
    print(f"{fileName} does not exist.")