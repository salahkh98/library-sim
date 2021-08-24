from book import Book
from author import Author
from database import Data


data = Data()

class Library:

    def show_info(self):
        for a in data.authors:
            print(f"ID: {a.id}         Name: ({a.name})           Phone: ({a.phone})          Email: ({a.email})")
            print()
        print("------------------------------------------------------------------------------------------------------------------------------")
        for d in data.books:
            print(f"ID: {d.id}         Title: ({d.title})          Publishing date: ({d.publishing_date})           Version: ({d.version})          Author: ({d.author.name})")
            print()



    def add_author(self):
        id = int(input("enter the id: "))
        for author in data.authors:
            if id == author.id:
                print("this id already taken......try again")
                return

        name = input("enter the name: ")
        phone = input("enter the phone number: ")
        email = input("enter the email: ")

        author = Author(id , name , phone , email)
        data.authors.append(author)


    def remove_author(self):
        id = int(input("enter the id of author to remove: "))
        for author in data.authors:
            if author.id == id:
                data.authors.remove(author)
                return
        print("\nthe author with id" , id , "its not found!")
        print("--------------------")


    def print_author(self):
        id = int(input("enter the id for specific author: "))
        for author in data.authors:
            if author.id == id:
                print("id: " + str(id))
                print("name: " + str(author.name))
                print("phone: " + str(author.phone))
                print("email: " + str(author.email))
                return

        print("\nauthor with id" , id ,  "its not found!")
        print("------------------")


    def print_author_book(self):
        id = int(input("enter the id of author: "))
        is_exist = False
        author_name = ""
        for author in data.authors:
            if author.id == id:
                is_exist = True
                author_name = author.name
                break

        if is_exist == False:
            print("author with id" , id , "its not found!")
            print("---------------------")
            return

        print("\nauthor " + str(author_name) + " books: ")
        for book in data.books:
            if book.author.name == author_name:
                print(str(book.title))
        print("--------------")
        

    def add_book(self):
        id = int(input("enter the id for the book: "))
        for book in data.books:
            if id == book.id:
                print("this id already taken.....try again!!")
                return

        title = input("enter the title for the book: ")
        publishing_date = input("enter the publishing date: ")
        version = int(input("enter the version number: "))
        author_id = int(input("enter the author id: "))
        for author in data.authors:
            if author_id == author.id:
                author_id = author
                break
    
        book = Book(id , title , publishing_date , version , author_id)        
        data.books.append(book)
    

    def remove_book(self):
        id = int(input("enter the id for the book: "))
        for book in data.books:
            if book.id == id:
                data.books.remove(book)
                return
        print("this book with id" , id , " is not found!!")


    def print_book(self):
        id = int(input("enter the id of the book: "))
        for book in data.books:
            if book.id == id:
                print("\nBook with id" , id , "info:")
                print("Title: " + str(book.title))
                print("Publishing date: " + str(book.publishing_date))
                print("Version: " + str(book.version))
                print("Author: " + str(book.author.name))
                print("-------------------")
                return

        print("Book with id" , id , "is not found!")
        print("---------------------")