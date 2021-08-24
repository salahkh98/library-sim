from database import Data
from book import Book
from author import Author
from library import Library

data = Data()
library = Library()

run = True
while run:

    input("\npress enter to show all the books and authors in the library: ")
    library.show_info()


    print("----------------------")
    print("1--> add author")
    print("2--> remove author")
    print("3--> print author")
    print("4--> print author books")
    print("5--> add books")
    print("6--> remove books")
    print("7--> print books")
    print("----------------------")


    choice = int(input("enter your choice: "))
    while choice > 7 or choice < 0:
        print("this choice not in the list........try again")
        choice = int(input("enter your choice: "))


    if choice == 1:
        library.add_author()


    elif choice == 2:
        library.remove_author()

    elif choice == 3:
        library.print_author()

    elif choice == 4:
        library.print_author_book()

    elif choice == 5:
        library.add_book()

    elif choice == 6:
        library.remove_book()

    elif choice == 7:
        library.print_book()