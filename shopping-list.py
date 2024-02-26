def add_item(shopping_list, item):
    if item in shopping_list:
        print(f"{item} is already in the list")
    else:
        shopping_list[item] = False

def remove(shopping_list, item):
    if item in shopping_list:
        del shopping_list[item]
    else:
        print(f"{item} is not in the list")

def check_off(shopping_list, item):
    if item in shopping_list:
        shopping_list[item] = True
    else:
        print(f"{item} is not in the list")


shopping_list = {}

while True:
    print("Options: ")
    print("1. Add Item: ")
    print("2. Remove Item: ")
    print("3. Check Item: ")
    print("4. View Items: ")

    comnd = int(input("Select option: "))
    if comnd == 1:
        item = input("ENter a item for add: ")
        add_item(shopping_list, item)
    elif comnd == 2:
        item = input("ENter a item for remove: ")
        remove(shopping_list, item)
    elif comnd == 3:
        item = input("Enter item for check off: ")
        check_off(shopping_list, item)
    elif comnd == 4:
        for item, value in shopping_list.items():
            print(f"{item}: {value}")

    

