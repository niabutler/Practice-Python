# test file

def get_integer(m):
    my_integer = int(input(m) )
    return my_integer

def get_string(m):
    my_string = input(m)
    return my_string


def double_loop_print():
    for i in range(0, len(L)):
        output = "{}:{}".format(i, L[i])
        print(output)
        for j in range (0, len(L[i])):
            output = "{}:{}".format(j,L[i][j])
            print(output)


def main():
    people = [
        ["Nia", "Blonde", 16],
        ["Tommi", "Blonde", 16],
        ["Grace", "Brown", 16],
        ["Rebecca", "Black", 16],
        ["Paige", "Brown", 16]
    ]
    # print(my_list)
    for i in range(0, len(people)):
        # creates column structure
        # < or > makes left/right align
        output = "{:10} --- {:10} --- {:<10}".format(people[i][0], people[i][1], people[i][2])
        print(output)



main()