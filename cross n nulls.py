# board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
board = [[1, 0, 1], [-1, 1, 1], [-1, -1, 0]]


def display():
    global board
    print("  0 1 2")
    for i, line in enumerate(board):
        s = str(i) + " "
        for j, row in enumerate(line):
            if row == 1:
                s += "x"
            elif row == -1:
                s += "o"
            elif row == 0:
                s += "-"
            s += " "
        print(s)


def who_is_winner():
    global board
    sum_di_left = 0
    sum_di_right = 0
    for x in range(3):
        sum_line = sum(board[x])
        sum_row = 0
        sum_di_left += board[x][x]
        for y in range(3):
            sum_row += board[y][x]

        if sum_line == 3 or sum_row == 3:
            return "x"
        elif sum_line == -3 or sum_row == -3:
            return "o"

    if sum_di_left == 3 or sum_di_right == 3:
        return "x"
    elif sum_di_left == -3 or sum_di_right == -3:
        return "o"
    return False


display()
who_is_winner()