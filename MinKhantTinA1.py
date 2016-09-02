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
items_list = []
get_items()

#This is going to check the valid input to be lower and changer to lower case if not
def change_lower(valid_input):
    word = input(">>>").lower()
    if word not in valid_input:
        word = input(">>>").lower()
    return change_lower()
