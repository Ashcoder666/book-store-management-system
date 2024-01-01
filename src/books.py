import json


#show all  books
def booksOptions():
    ["Show All Books", "Add New Book" , "Edit A Book" , "Delete A Book"]


def show_all_books():
    file = open("./data/books.json",'r')
    normalizedFile = json.loads(file.read())
    for f in normalizedFile:
        print("-----------------------------")
        print(f"Book Title : {f["book_name"]}")
        print(f"Stock : {f["stock"]}")
        print(f"Price : {f["price"]}")
        print("-----------------------------")
    file.close()


#add one book
def createBook(book_name,language,price,stock):
    file = open("./data/books.json",'r')
    
#finish this by tomorrow and start node js repo style stealing



# delete book