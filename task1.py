try:
    with open("sample.txt", "r") as file:
        print("File Content:\n")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Error: 'sample.txt' does not exist.")

