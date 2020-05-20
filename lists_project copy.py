
def get_integer(m):
    my_integer = int(input(m) )
    return my_integer

def get_string(m):
    my_string = input(m)
    return my_string

def add_name_age(N,A):
    count = get_integer("How many people would you like to add to the list? -> ")
    for i in range (0, count):
        # get name and age to add to the list
        name = get_string("Please enter a name: -> ")
        age = get_integer("Please enter {}'s age: -> ".format(name))
        N.append(name)
        A.append(age)
        print("."*50)
        my_string = ("{}, age {} has been added to the list".format(name, age))
        print(my_string)
        print("."*50)

    
def review(N, A):
    if len(N) == len(A):
        for i in range(0, len(A)):
            output = "{} is {} years old".format(N[i], A[i])
            print(output)
        print("." * 50)
    else:
        print("List one doesn't have same number of elements as list two")

    
 

def menu():
    name = []
    age = []
    my_menu ='''
    A: Add
    B: Review
    Q: Quit
    '''
    run = True
    while run == True:
        print(my_menu)
        choice = get_string("Please select your option: -> ").upper()
        print("."*50)
        if choice == "A":
            add_name_age(name, age)
        elif choice == "B":
            review(name, age)
        elif choice == "Q":
            print("Thank you!")
            run = False    
        else:
            print("Invalid entry")
            
            


#add_name_age()
menu()
