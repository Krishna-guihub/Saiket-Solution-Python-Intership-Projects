# Basic File Handling Program

filename = "sample.txt"

try:
    # open file in read mode
    file = open(filename, "r")
    data = file.read()
    file.close()

    print("File content before update:\n")
    print(data)

    old_word = input("\nEnter the word to replace: ")
    new_word = input("Enter the new word: ")

    if old_word in data:
        data = data.replace(old_word, new_word)

        # open file in write mode
        file = open(filename, "w")
        file.write(data)
        file.close()

        print("\nWord replaced successfully!")
    else:
        print("\nWord not found in file.")

except FileNotFoundError:
    print("Error: File does not exist.")

except Exception as e:
    print("Something went wrong:", e)
