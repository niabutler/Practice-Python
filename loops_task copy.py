
def square_num(n):
    for i in range(0,n):
        my_square = i*i
        my_output = "{} squared = {}".format(i, my_square)
        print(my_output)
    print()

def cubed_num(n):
    for i in range(0,n):
        my_cube = i*i*i
        my_output = "{} cubed = {}".format(i, my_cube)
        print(my_output)
    print()
    
def menu():
    run = True
    while run == True:
        my_menu = '''
        A: Square number
        B: Cube number
        Q: Quit
        '''
        print("Welcome!")
        n = int(input("Please enter a number: -> "))
        print(my_menu)
        choice = input("Please choose an option: -> ")
        if choice == "A":
            square_num(n)
        elif choice == "B":
            cubed_num(n)
        elif choice == "Q":
            run = False
            print("Thanks for squaring and cubing!")
        else:
            print("Invalid entry")

menu()
        
        
    

