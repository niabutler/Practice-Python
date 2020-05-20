

def adding(a,b):
    my_sum = a+b
    my_string = "{} + {} = {}".format(a,b,my_sum)
    print(my_string)
    

def subtract(a,b):
    my_sum = a-b
    my_string = "{} - {} = {}".format(a,b,my_sum)
    print(my_string)

def multiply(a,b):
    my_product = a*b
    my_string = "{} * {} = {}".format(a,b,my_product)
    print(my_string)


def divide(a,b):
    my_product = a/b
    my_string = "{} / {} = {}".format(a,b,my_product)
    print(my_string)


def get_integer(m):
    my_number = int(input(m))
    return my_number
    

def menu():
    num_one = get_integer("Please enter your first number: ")
    num_two = get_integer("Please enter your second number: ")
    my_menu = '''
    1 : add
    2 : subtract
    3 : multiply
    4 : divide
    0 : quit
    '''
    print(my_menu)
    choice = get_integer("Please enter your choice from the menu: ")
    if choice ==1:
        adding(num_one, num_two)
    elif choice ==2:
        subtract(num_one, num_two)
    elif choice ==3:
        multiply(num_one, num_two)
    elif choice ==4:
        divide(num_one, num_two)
    elif choice ==0:
        print("Thank you")
    else:
              print("Unrecognised entry")
    

 
#adding(3,5)
#subtract(8,5)
#multiply(3,4)
#divide(35,7)
menu()
    
