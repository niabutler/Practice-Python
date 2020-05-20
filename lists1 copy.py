
import random

def get_integer(m):
    my_integer = int(input(m) )
    return my_integer


def get_string(m):
    my_string = input(m)
    return my_string


def print_at_index(L):
    my_index = get_integer("Please enter an index number: -> ")
    output = "The value -{}- is at index -{}- in the list".format(L[my_index], my_index)
    print(output)
    print("."*50)


# print list
def print_list(L):
    for x in L:
        print(x)


# print indexes next to list items
def print_list_indexes(L):
    for i in range (0, len(L)):
        # i is the counter, L is value in the list
        print( "{} : {}".format(i, L[i]))


# adding to a list
def add_item(L):
    new_item = get_string("Please enter new item: -> ")
    L.append(new_item)
    print("."*50)


# changing values
def change_value(L):
    print_list_indexes(L)
    index_num = get_integer("Please choose the index number: -> ")
    new_value = get_string("Please enter new value: -> ")
    # we now have all the values we need
    old_value = L[index_num]
    L[index_num] = new_value
    output="The old value of {} is now changed to {}".format(old_value, L[index_num])
    print(output)


# find an item in a list
def find_item(L):
    item = get_string("Who do you want to find? -> ")
    if item in L:
        index_num = L.index(item)
        output ="{} has been found and is at index number {}".format(L[index_num], index_num)
        print(output)
        print("."*50)
    else:
        print("{} is not in the list".format(item))
        print("."*50)


# remove item from list
def remove_item(L):
    item = get_string("Who do you want to remove? -> ")
    if item in L:
            L.remove(item)
            output = "{} has been removed from the list".format(item)
            print(output)
            print("."*50)
    else:
        output = "{} could not be found in the list".format(item)
        print(output)
        print("."*50)


# sort the list in alphabetical order
def sort_list(L):
    L.sort()

# shuffle list 
def shuffle_list(L):
    random.shuffle(L)

    
# menu             
def menu():
    my_list1 = ["Mary", "Patsy", "Jean", "Constantine", "Pierre"]
    my_list2 = ["Bob", "Ron", "Max", "Joe", "Pat"]
    my_list = my_list2
    print("my_list is currently set to: {}".format(my_list))
    my_menu='''
    A: Print the list
    B: Print the list with indicies
    C: Add item to the list
    D: Print an index number
    E: Change value in the list
    F: Select List 1
    G: Select List 2
    H: Find an item in the list
    I: Remove item from the list
    J: Sort list alphabetically
    K: Shuffle list
    Q: Quit
    '''
    
    run = True
    while run == True:
        print(my_menu)
        choice = get_string("Please select your option: -> ").upper()                                                        
        print("."*50)
        if choice =="A":
            print_list(my_list)
            print("."*50)
        elif choice =="B":
            print_list_indexes(my_list)
        elif choice =="C":
            add_item(my_list)
        elif choice =="D":
           print_at_index(my_list)
        elif choice == "E":
            change_value(my_list)
        elif choice == "F":
            my_list = my_list1
            print("my_list ONE has been selected")
        elif choice == "G":
            my_list = my_list2
            print("my_list TWO has been selected")
        elif choice =="H":
            find_item(my_list)
        elif choice =="I":
            remove_item(my_list)
        elif choice =="J":
            sort_list(my_list)
        elif choice =="K":
            shuffle_list(my_list)
        elif choice =="Q":
            print("."*50)
            print("Thank you!")
            run = False
        else:
            print("Invalid entry")



                                                                  
menu()
                                                                                                                                                                                                                                                           
                                                                                                                              
                                                                
                                                                                                                              
                                                                
                                                           

