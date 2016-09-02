''''Min Khant Tin
    1/9/1016
    This a shopping list program which you can add, list, mark and see the items you need to shop
    https://github.com/minkhanttin123/CP1404_Assignment1'''


#This is going to welcome the user and show the title
print("Welcome to the Shopping List 1.0 by Min Khant Tin")

#This is going to show the menu
def show_menu():
    menu = '''
Menu:
R - List required items
C - List completed items
A - Add new item
M - Mark an item as completed
Q - Quit'''
    print(menu)



#I created a text file with the csv inside named 'items.txt and open it as read only file. For each items in file replace with new line and split with a comma
def get_items():
    file = open("items.txt", "r")
    for each in file:
        items_list.append(each.replace("\n", "").split(","))
    file.close()




#This is going to check the valid input to be lower and changer to lower case if not
def change_lower(valid_input):
    word = input(">>>").lower()
    if word not in valid_input:
        word = input(">>>").lower()
    return word


from operator import itemgetter

#This is going to sort & list the items in side the items_list with correct format(count, name, price and priority)
#If there is no item in the list (count = 0), then it will show "No required items"
#Or it will show the total price of all the item with dollar sign
def required_items():
    items_list.sort(key=itemgetter(2, 0))
    count = 0
    price = 0
    for a in items_list:
        if(a[3]== "r"):
            price += float(a[1])
            print("{}. {} ${} ({})".format(count, a[0], float(a[1]), a[2]))
        count += 1
    if count == 0:
        print("No required items")
    else:
        print("Total price ${}".format(price))




#This is going to list & sort the items that are already completed
#The completed items will be shown with correct format(count, name, price, priority)
#If the count = 0 or there is no completed items it will show "No items completed
#Or show the total price of the items inside the list
def complete_items():
    items_list.sort(key=itemgetter(2, 0))
    count = 0
    price = 0
    for b in items_list:
        if(b[3]=="c"):
            price += float(b[1])
            print("{}. {} ${} ({})".format(count, b[0], float(b[1]), b[2]))
            count += 1
    if count == 0:
        print("No items completed")
    else:
        print(print("Total price ${}".format(price)))



#First the is going to show the require_items and ask the user to input a number to mark
#The chosen one will be marked as complete and show the message that the item has been marked
def mark_item():
    required_items()
    x = []
    for i in items_list:
        if(i[3]== "r"):
            x.append(i)
    user_input = int(input("Enter the number of items to mark as completed"))
    count = 0
    for i in x:
        if (count == user_input):
            print("{} marked as complete".format(i[0]))
            i[3]="c"
        count += 1
        for i in x:
            if(i[3 == "c"]):
                for each in items_list:
                    if (each[0] == i[0]):
                        each[3] = "c"
                        break





#This will allow the user to add an item to the list
#Error check with blank, space, invalid numbers
def add_items():
    item = []
    while True:
        name = str(input("Item name: "))
        if  name ==" ":
            print("Input can not be blank")
            continue
        elif name =="":
            print("Input can not be blank")
            continue
        if name !=" ":
            item.append(name)
            break
    while True:
        try:
            iprice = int(input("Price: "))
        except ValueError:
            print("Invalid input; enter a valid number")
            continue
        if iprice <= 0:
            print ("Price must be >= $0")
            continue
        else:
            item.append(iprice)
            break
    while True:
        priority = input("Priority: ")
        try:
           int(priority)
        except ValueError:
            print("Invalid input; enter a valid number")
            continue
        if priority not in ('1', '2', '3'):
            print("Priority must be 1, 2 or 3 ")
        else:
            item.append(priority)
            item.append("r")
            break
    print("{}, ${} (priority {}) added to shopping list.".format(item[0], float(item[1]), item[2]))

    items_list.append(item)

items_list = []
get_items()


#This going to ask the user input
#User can add,
while True:
    show_menu()
    user_choice = change_lower(["r", "c", "a", "m", "q"])
    if user_choice == "q":
        print("Items has been saved to csv list \n Have a nice day!")
        break
    elif user_choice == "r":
        required_items()
    elif user_choice == "c":
        complete_items()
    elif user_choice == "a":
        add_items()
    elif user_choice == "m":
        mark_item()


