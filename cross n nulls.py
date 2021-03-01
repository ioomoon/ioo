import os
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


# Отрисовывает поле
def display():
    global board
    os.system('cls')
    print("*** Крестики-нолики ***")
    print("Поле 3x3. Для хода каждому игроку предлагается ввести координаты клетки (строка и столбец).")
    # Очищаем консоль
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
    # Диагонали
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


# Ход крестиком
def game_move_x():
    move_x = input("Введите координаты хода х-ом через пробел: ")
    x, y = map(int, move_x.split())
    try:
        if board[x][y] == 0:
            board[x][y] = 1
            display()
            if who_is_winner():
                print(who_is_winner())
            else:
                game_move_o()
        else:
            print("Занято. Попробуйте снова.")
            game_move_x()
    except (ValueError, IndexError):
        print("Вы ввели неверные координаты. Попробуйте снова.")
        game_move_x()


# Ход ноликом
def game_move_o():
    move_y = input("Введите координаты хода y-ом через пробел: ")
    i, j = map(int, move_y.split())
    try:
        if board[i][j] == 0:
            board[i][j] = -1
            display()
            if who_is_winner():
                print(who_is_winner())
            else:
                game_move_x()
        else:
            print("Занято. Попробуйте снова.")
            game_move_o()
    except (ValueError, IndexError):
        print("Вы ввели неверные координаты. Попробуйте снова.")
        game_move_o()



display()
print(who_is_winner())
game_move_x()