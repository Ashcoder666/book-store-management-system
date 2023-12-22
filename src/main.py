from books import show_all_books

categories = ["Books","Users","Orders"]

operations = ["Add","Update" , "Delete"]


for index,cat in enumerate(categories):
    print(f"{index} : {cat}")
    
    
userInput = int(input("Input Enter your choice "))


print(f"your choice is {categories[userInput]}")

show_all_books()