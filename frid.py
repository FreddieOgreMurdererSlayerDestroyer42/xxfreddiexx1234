try:
    with open ("freddie.txt", "x") as file:
        print("File created successfully.")
        file.write("Freddie laban sa lahat\n")
except FileExistsError:
    print("File already exists.")

    while True:
        print("\n=== MINI LIBRARY ===\n")
        print("1. Add a book")
        print("2. View All Books")
        print("3. Update a Book")
        print("4. Exit the program...")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            title = input("Enter the book title: ")
            author = input ("Enter the book author: ")

            with open ("freddie.txt", "a") as file:
                file.write(f"{title} by {author}\n")

            print ("\n BOOK ADDED SUCCESSFULLY!!")
        
        elif choice == "2":
            print("\n=== LIST OF BOOKS ===\n")
            try:
                with open("freddie.txt", "r") as file:
                    books = file.readlines()
                    if books:
                        for book in books:
                            print(book.strip())
                    else:   
                        print("No books found.")
            except FileNotFoundError:
                print("File not found.")

        if choice == "3":
            print("\n === UPDATE A BOOK === \n")

            try:
                with open("freddie.txt", "r") as file:
                    books = file.readlines()

                if not books:
                    print("No Books to Update")
                    continue

                for i, book in enumerate(books):
                    print(f"{i+1}, {book.strip()}")

                num = int(input('Enter book number to update: '))

                if 1 <= num <= len(books):
                    new_title = input("Enter New Title: ")
                    new_author = input("Enter New Author")

                    books[num-1] = f"{new_title} by {new_author}\n"

                    with open("freddie.txt", "w") as file:
                        file.writelines(books)

                    print("Book Updated Succesfully")
                else:
                    print("Invalid Number!")

            except FileNotFoundError:
                print("File not Found.")
            except ValueError:
                print("Invalid Input!")
   
        elif choice == "4":
            print("EXITING PROGRAM!!!")
            break