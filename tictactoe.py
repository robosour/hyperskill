c = [" ", " ", " ", " ", " ", " ", " ", " ", " "]


def print_table():
    print(f"""
    ---------
    | {c[0]} {c[1]} {c[2]} |
    | {c[3]} {c[4]} {c[5]} |
    | {c[6]} {c[7]} {c[8]} |
    --------- """)


def get_coords():
    print("Enter the coordinates:")
    check = input().split()
    try:

        x = int(check[0])
        y = int(check[1])
        if x > 3 or x < 1 or y > 3 or y < 0:
            print("Coordinates should be from 1 to 3!")
            get_coords()

        else:
            coords = [int(x) for x in check]
            empty = [i for i, e in enumerate(c) if e == " "]
            make_change(coords, empty, toggle)

    except ValueError:
        print("You should enter numbers!")
        get_coords()


def make_change(coords, empty, tog):
    if coords[0] == 1:
        if coords[1] == 1:
            if 0 in empty:
                c[0] = tog
            else:
                print("This cell is occupied! Choose another one!")
                get_coords()
        elif coords[1] == 2:
            if 1 in empty:
                c[1] = tog
            else:
                print("This cell is occupied! Choose another one!")
                get_coords()
        elif coords[1] == 3:
            if 2 in empty:
                c[2] = tog
            else:
                print("This cell is occupied! Choose another one!")
                get_coords()
    elif coords[0] == 2:
        if coords[1] == 1:
            if 3 in empty:
                c[3] = tog
            else:
                print("This cell is occupied! Choose another one!")
                get_coords()
        elif coords[1] == 2:
            if 4 in empty:
                c[4] = tog
            else:
                print("This cell is occupied! Choose another one!")
                get_coords()
        elif coords[1] == 3:
            if 5 in empty:
                c[5] = tog
            else:
                print("This cell is occupied! Choose another one!")
                get_coords()
    elif coords[0] == 3:
        if coords[1] == 1:
            if 6 in empty:
                c[6] = tog
            else:
                print("This cell is occupied! Choose another one!")
                get_coords()
        elif coords[1] == 2:
            if 7 in empty:
                c[7] = tog
            else:
                print("This cell is occupied! Choose another one!")
                get_coords()
        elif coords[1] == 3:
            if 8 in empty:
                c[8] = tog
            else:
                print("This cell is occupied! Choose another one!")
                get_coords()


def xwin():
    line_one = [c[0], c[3], c[6]]
    line_two = [c[1], c[4], c[7]]
    line_three = [c[2], c[5], c[8]]
    row_one = [c[0], c[1], c[2]]
    row_two = [c[3], c[4], c[5]]
    row_three = [c[6], c[7], c[8]]
    diag_one = [c[0], c[4], c[8]]
    diag_two = [c[2], c[4], c[6]]
    x_win = ['X', 'X', 'X']
    if line_one == x_win or line_two == x_win or line_three == x_win \
            or diag_one == x_win or diag_two == x_win or row_two == x_win \
            or row_three == x_win or row_one == x_win:
        return True


def owin():
    line_one = [c[0], c[3], c[6]]
    line_two = [c[1], c[4], c[7]]
    line_three = [c[2], c[5], c[8]]
    row_one = [c[0], c[1], c[2]]
    row_two = [c[3], c[4], c[5]]
    row_three = [c[6], c[7], c[8]]
    diag_one = [c[0], c[4], c[8]]
    diag_two = [c[2], c[4], c[6]]
    o_win = ['O', 'O', 'O']
    if line_one == o_win or line_two == o_win or line_three == o_win \
            or diag_one == o_win or diag_two == o_win or row_two == o_win \
            or row_three == o_win or row_one == o_win:
        return True


def outcome():
    if not xwin() and not owin():
        if " " not in c:
            print("Draw")
            exit()

    elif owin():
        print("O wins")
        exit()
    elif xwin():
        print("X wins")
        exit()


print_table()
while True:
    toggle = "X"
    get_coords()
    print_table()
    outcome()
    toggle = "O"
    get_coords()
    print_table()
    outcome()
