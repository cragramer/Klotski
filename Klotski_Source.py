import random

print("""Welcome to zzy's game! The board has an empty space where 
an adjacent tile can be slid to.The objective of the game 
is to rearrange the tiles into a sequential order by their
numbers (left to right, top to bottom) by repeatedly making
sliding moves (left, right, up or down).""")
# Ask the player to enter the nth puzzle which he or her want to learn.
while True:
    g_dimension = input('enter the dimension you want to play(3-10)>')
    if g_dimension.isdigit() and (2 < int(g_dimension) < 11):  # check whether it is a correct number
        g_dimension = int(g_dimension)
        break
    else:
        print('Invaild input! Please check your input.')
# Allow the player to define the letter to control the move
while True:
    g_define = input(
        'Enter the four letters used for left, right, up and down directions>')
    g_define = list(g_define.split())  # split the letter
    # make a new list to check if there exist repeat number
    g_define_lst = set(g_define)
    if ((len(g_define_lst) == len(g_define)) and len(g_define) == 4
            and all([word in [chr(i) for i in range(97, 123)] for word in g_define])):  # check whether the input is lowcase letters
        break
    else:
        print('Invaild input! Please check your input.')
# define the direction order
g_right = g_define[1]
g_left = g_define[0]
g_up = g_define[2]
g_down = g_define[3]
g_times = 0            # Create a variable to track the times that player try.
# Make a empty list in order to put numbers and space in a random order.
g_numbers = []
# Make a empty list in order to put numbers and space in the correct order.
g_numbers_sorted = []
# put the numbers in two lists in correct order.
for g_number in range(1, g_dimension**2):
    g_numbers.append(g_number)
    g_numbers_sorted.append(g_number)
# put the space in two list
g_numbers.append(' ')
g_numbers_sorted.append(' ')


def create_random_rumber():  # mess up the order of first list of number
    while True:
        random.shuffle(g_numbers)
        position = g_numbers.index(' ')
        if g_dimension % 2 == 1 and get_inversion_number() % 2 == 0 \
                and g_numbers != g_numbers_sorted:
            output_number()  # if the dimension is odd, the inversion number must be even
            break
        elif (g_dimension % 2 == 0 and (position//g_dimension +
              get_inversion_number()) % 2 == 1 and g_numbers != g_numbers_sorted):
            output_number()  # if the dimension is even, deviation of the dimension and the space line,inversion number must be even or odd together
            break


def get_inversion_number():  # figure out the inversion number of the ramdom list
    inversion_number = 0
    position = g_numbers.index(' ')
    del g_numbers[position]
    #  figure out the inversion number
    for i in range(0, (g_dimension**2-2)):
        for m in range(i+1, g_dimension**2-1):
            if g_numbers[i] > g_numbers[m]:
                inversion_number += 1
    g_numbers.insert(position, ' ')
    return inversion_number


def output_number():  # print out the number and space in the right formula
    for n in range(1, g_dimension+1):
        line_n = g_numbers[(n-1)*g_dimension: n*g_dimension]
        for i in range(0, g_dimension):  # print the number line by line
            # if the number<10 or a space, print two space in order to align
            if line_n[i] == ' ' or int(line_n[i]) < 10:
                print(line_n[i], end=(' '*2))
            else:
                # for the number biger than 10, print with one space
                print(line_n[i], end=(' '))
        print('')  # lastly print a empty thing to make a new line.


def input_order():  # allow the player to enter the direction to move
    while True:
        # find the position which the space lie in, and make a list of vaild order
        position = g_numbers.index(' ')
        order_list = ['Enter your move(', 'left-', g_left, ', right-',
                      g_right, ', up-', g_up, ', down-', g_down, ')>']
        # delete the invalid order
        if -1 < position < g_dimension:
            order_list.remove(', down-')
            order_list.remove(g_down)
        if position % g_dimension == 0:
            order_list.remove(', right-')
            order_list.remove(g_right)
        if (position+1) % g_dimension == 0:
            order_list.remove('left-')
            order_list.remove(g_left)
        if ((g_dimension-1)*g_dimension) <= position <= g_dimension**2:
            order_list.remove(', up-')
            order_list.remove(g_up)
        if (position+1) % g_dimension != 0:  # if the left order is vaild, just print the list
            for order_l in order_list:
                print(order_l, end='')
        else:  # if the left order is invaild, we need to delete ', ' from the first vaild order
            order_list[1] = order_list[1][2:]
            for order_l in order_list:
                print(order_l, end='')
        order = input()  # allow player to enter the order
        # create a list to restore the vaild order to make sure that player put the right order
        correct_input = []
        for x in range(1, len(order_list)):
            if x % 2 == 0:
                correct_input.append(order_list[x])  # restore the vaild order
        if order not in correct_input:  # if the player enter a invaild order, remind him or her
            print('Invaild input! Please check your input.')
            continue
        return order


def move():  # follow the player's order to make a move.
    order = input_order()
    # find the position of space before this move
    position = g_numbers.index(' ')
    # exchange the position of space and surrounding number
    if order == g_left:
        g_numbers[position], g_numbers[position + 1] = \
            g_numbers[position+1], g_numbers[position]
    elif order == g_right:
        g_numbers[position-1], g_numbers[position] = \
            g_numbers[position], g_numbers[position-1]
    elif order == g_up:
        g_numbers[position], g_numbers[position + g_dimension] = \
            g_numbers[position+g_dimension], g_numbers[position]
    elif order == g_down:
        g_numbers[position-g_dimension], g_numbers[position] = \
            g_numbers[position], g_numbers[position-g_dimension]
    output_number()  # print the list of numeber in correct order


def contine_the_game():  # the main proccess of the game
    create_random_rumber()  # create a solvable number list
    while True:
        global g_times
        # if the player solve the puzzle ssuccessfully, end the loop
        if g_numbers == g_numbers_sorted and g_times != 1:
            print('Congratulations! You solve the puzzle in ' +
                  str(g_times) + ' moves.')
            break
        elif g_numbers == g_numbers_sorted and g_times == 1:
            print('Congratulations! You solve the puzzle in ' +
                  str(g_times) + ' move.')
            break
        # if the puzzle cannot be solved yet, track the times players use and continue
        else:
            move()
            g_times += 1


contine_the_game()  # begin the game

while True:  # if the player finish the game, ask the player whether want to player again.
    q_or_n = input(
        'Enter ‘n’ to start a new game or enter ‘q’ to end the game >')
    if q_or_n == 'n':
        g_times = 0  # restart g_times
        contine_the_game()
    elif q_or_n == 'q':  # withdraw from the program
        exit()
    else:  # if player enter something else, give him or her a reminder.
        print('Invaild input! Please check your input.')
