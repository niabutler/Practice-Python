def get_integer(m):
    my_integer = int(input(m))
    return my_integer


def get_string(m):
    my_string = input(m)
    return my_string
    print("."*100)


def print_at_index(L):
    my_index = get_integer("Please enter index number: -> ")
    output = "The value -- {} -- is at index {} in the list".format(L[my_index], my_index)
    print(output)
    print("."*100)

    
# basic print list
def print_list(L):
    for x in L:
        print(x)
    print("."*100)


# print with index as 1
def print_list_indexes(L):
    for i in range(0, len(L)):
        # i is the counter, L is value in the list
        print( "{} : {}".format(i, L[i]))
    print("."*100)
        
def add_item(L):
    my_item = get_string("Please enter a new item: -> ")
    L.append(my_item)


def change_value(L):
    print_list_indexes(L)
    index_num = get_integer("Please choose the index number: -> ")
    new_value = get_string("Please enter new value: -> ")
    # we now have all the values we need
    old_value = L[index_num]
    L[index_num] = new_value
    output="The old value of {} is now changed to {}".format(old_value, L[index_num])
    print(output)
    

    
#function tests
#print_list_indexes(my_list)
#print_list(my_list)
#add_item(my_list)
#print_list(my_list)



# create a menu
# going to put new things in and it will enable much better management

def menu():
    my_list1 = ["Mary", "Patsy", "Jean", "Constantine", "Pierre"]
    my_list2 = ["Bob", "Ron", "Max", "Joe", "Pat"]
    my_list = my_list2
    print("my_list is currently set to: {}".format(my_list))
    my_menu = '''
            A: print the list
            B: print the list with indices
            C: add item to list
            D: print the value which is at a specific index number
            E: change value
            F: Choose list 1
            G: Choose list 2 
            Q: Quit
            '''
    run = True
    while run == True:
        print(my_menu)
        choice = get_string("Please select your option: -> ").upper()
        print("."*100)
        if choice == "A":
            print_list(my_list)
        elif choice == "B":
            print_list_indexes(my_list)
        elif choice == "C":
            add_item(my_list)
        elif choice == "D":
            print_at_index(my_list)
        elif choice == "E":
            change_value(my_list)
        elif choice == "F":
            my_list = my_list1
            print("my_list ONE has been selected")
        elif choice == "G":
            my_list = my_list2
            print("my_list TWO has been selected")
        elif choice == "Q":
            print("Thank you")
            run = False
            
        
menu()

