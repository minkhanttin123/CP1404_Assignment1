'''Min Khant Tin
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
    
    
items_list = []
get_items()

#This is going to check the valid input to be lower and changer to lower case if not
def change_lower(valid_input):
    word = input(">>>").lower()
    if word not in valid_input:
        word = input(">>>").lower()
    return change_lower()
