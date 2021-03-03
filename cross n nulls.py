board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


# Отрисовывает поле
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


# Определяет победителя
def who_is_winner():
    global board
    sum_di_left = 0
    sum_di_right = 0
    for x in range(3):
        sum_line = sum(board[x])
        sum_row = 0
        sum_di_left += board[x][x]
        sum_di_right += board[x][-x - 1]

        for y in range(3):
            sum_row += board[y][x]

        if sum_line == 3 or sum_row == 3:
            return "Победил x"
        elif sum_line == -3 or sum_row == -3:
            return "Победил o"
    if sum_di_left == 3 or sum_di_right == 3:
        return "Победил x"
    elif sum_di_left == -3 or sum_di_right == -3:
        return "Победил o"
    if sum_di_right == 3 or sum_di_right == 3:
        return "Победил x"
    elif sum_di_right == -3 or sum_di_right == -3:
        return "Победил o"


def game_move_x():
    move_x = input("Введите координаты хода х-ом через пробел: ")
    x, y = map(int, move_x.split())

    if board[x][y] == 0:
        board[x][y] = 1
    display()
    if who_is_winner():
        print(who_is_winner())
    else:
        game_move_o()


def game_move_o():
    move_o = input("Введите координаты хода о-ом через пробел: ")
    i, j = map(int, move_o.split())
    if board[i][j] == 0:
        board[i][j] = -1
    display()
    if who_is_winner():
        print(who_is_winner())
    else:
        game_move_x()


display()
print(who_is_winner())
game_move_x()