try:
    # ask user to enter a note
    message = input("Enter a short note: ")

    # open file in write mode (creates/overwrites file)
    with open("notes.txt", "w") as file:
        file.write(message + "\n") # save note to file

    # open file in read mode to display content
    with open("notes.txt", "r") as file:
        print("\nFile Content:")
        print(file.read()) # show everything inside the file

    # ask user for another note
    new_message = input("\nEnter another note: ")

    # open file in append mode (adds w/o deleting old data)
    with open("notes.txt", "a") as file:
        file.write(new_message + "\n") # add new note

    # read again to show updated content
    with open("notes.txt", "r") as file:
        print("\nUpdated File Content:")
        print(file.read())

# if file is missing
except FileNotFoundError:
    print("Error: File not found.")

# if no permission to access file
except PermissionError:
    print("Error: Permission denied.")

# other error
except Exception as e:
    print("Error:", e)