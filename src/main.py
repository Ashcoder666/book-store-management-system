from books import show_all_books

categories = ["Books","Users","Orders"]

operations = ["Show All","Add","Delete"]


for index,cat in enumerate(categories):
    print(f"{index} : {cat}")
    
    
userInput = int(input("Input Enter your choice "))


print(f"your choice is {categories[userInput]}")

if userInput == 0:
    for index,op in enumerate(operations):
     print(f"{index} : {op}")
    
    userInput2 = int(input("Input Enter your choice "))
    if userInput2 == 0:
        show_all_books()



