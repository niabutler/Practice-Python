#loops
#loops are repeated actions


# loop with a counter (will run a certain number of times)
def loop_with_counter(count):
    c = 0
    while c < count:
        print("hello c is now {}".format(c)    )
        # increment
        c += 1
    return None


# indefinite loop
def indefinite_loop():
    run = True
    while run == True:
        user_choice = input("Press 'n' to stop or anything else to stay in the loop: -> ")
        if user_choice == "n":
            print("Loop will stop")
            run = False
        else:
            print("You are still in the loop")

            
# in range loop
def for_in_range_loop():
    # this has a built in counter
    # can be anything but we generally use i or j or k
    # can add steps
    for i in range(3, 20, 5):
        print(i)


#double loop
def double_loop():
    for i in range(0,5):
        for j in range(0,6):
            print("({} , {}) ".format(j,i) , end = "" )
        print()

def menu():
    my_menu = '''
    1: while loop with counter
    2: while loop with quit
    3: for in range
    4: double loop
    0: quit
    '''
    print(my_menu)
    choice = int(input("choose your option: -> "))
    if choice is 1:
        amount = int(input("How many would you like: -> "))
        loop_with_counter(amount)
    elif choice is 2:
        indefinite_loop()
    elif choice is 3:
        for_in_range_loop()
    elif choice is 4:
        double_loop()
    elif choice is 5:
        print("Thank you")
        
                
            





# loop_with_counter()
# indefinite_loop()
# for_in_range_loop()
# double_loop()
menu() 
    
