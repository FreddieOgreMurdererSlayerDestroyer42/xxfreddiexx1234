try:
    with open ("freddie.txt", "x") as file:
        print("File created successfully.")
        file.write("Freddie laban sa lahat")
except FileExistsError:
    print("File already exists.")

    while True:
        print("\n=== MINI LIBRARY ===\n")
        print("1. Add a book")
        print("2. Exit the program")

        choice = input("\nEnter your choice:\n ")

        if choice == "1":
            title = input("Enter the book title: ")
            author = input ("Enter the book author: ")

            with open ("freddie.txt", "a") as file:
                file.write(f"{title} by {author}\n")

            print ("\n BOOK ADDED SUCCESSFULLY!!")
        
        
        elif choice == "2":
            print("EXITING PROGRAM!!")
            break

        else:
            print("INVALID INPUT! PLEASE TRY AGAIN!")