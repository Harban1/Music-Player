fileName = "hello.txt"
try:
    with open(fileName, "r", encoding = "utf-8") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print(f"{fileName} does not exist")