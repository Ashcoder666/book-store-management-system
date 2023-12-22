#show all  books
import json

def booksOptions():
    ["Show All Books", "Add New Book" , "Edit A Book" , "Delete A Book"]


def show_all_books():
    file = open("./data/books.json",'r')
    normalizedFile = json.loads(file.read())
    for f in normalizedFile:
        print(f"Book Title : {f["book_name"]}")
        print(f"Stock : {f["stock"]}")
        print(f"Price : {f["price"]}")
        print("-----------------------------")
    


#add one book
#finish this by tomorrow and start node js repo style stealing

# edit book


# delete book