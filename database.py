from book import Book
from author import Author

class Data:


    author1 = Author(1 , "Mhamad", "+96170123456", "mhamad@gmail.com")
    author2 = Author(2 , "Salem",  "+9664021833",  "salem@gmail.com")
    author3 = Author(3 , "Rola",   "+9631249392",  "rola@gmail.com")

    book1 = Book(11 , "Learn Java", "12-20-2019", 1, author1)
    book2 = Book(12 , "Learn HTML", "8-5-2018", 3, author1)
    book3 = Book(13 , "PHP for beginners", "10-2-2019", 1, author2)
    book4 = Book(14 , "C# for dummies", "12-20-2019", 1, author3)

    books = [book1 , book2 , book3 , book4]
    authors = [author1 , author2 , author3]
