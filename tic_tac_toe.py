def check_win(row, col):
    symbol = field[row][col]
    win_con_row = 0
    win_con_col = 0
    win_con_diag = 0

    if row == col:
        for i in range(1, ROW + 1):
            if field[i][i] == symbol:
                win_con_diag += 1
        if win_con_diag == 3:
            return True
        win_con_diag = 0
    if ROW == row + col - 1:
        for i in range(1, ROW + 1):
            if field[i][ROW + 1 - i] == symbol:
                win_con_diag += 1
        if win_con_diag == 3:
            return True

    for i in range(1, ROW + 1):
        if field[i][col] == symbol:
            win_con_row += 1

    for i in range(1, COL + 1):
        if field[row][i] == symbol:
            win_con_col += 1

    if win_con_col == 3 or win_con_row == 3:
        return True
    else:
        return False


def validate(data):
    if len(data) != 2:
        return "Incorrect data, try again"
    if not (data[0].isdigit() and data[1].isdigit()):
        return "Incorrect data, try again"
    data = list(map(int, data))
    if not (0 <= data[0] < ROW and 0 <= data[1] < COL):
        return "Coordinates out of range"
    if field[data[0] + 1][data[1] + 1] != " ":
        return "Field is already taken"
    return ""


def move():
    data = input("Make your move in format: row col ").split()
    message = validate(data)
    while message:
        data = input(message).split()
        message = validate(data)
    x, y = list(map(int, data))
    x += 1
    y += 1

    return x, y


def show():
    print(" | ".join(field[0]) + " |")
    print("-" * (ROW + 1) * 4)
    for i in range(1, ROW + 1):
        print(" | ".join(field[i]) + " |")
        print("-" * (ROW + 1) * 4)


ROW = COL = 3
field = [[" " for _ in range(COL)] for _ in range(ROW)]
field.insert(0, list(map(str, range(-1, COL))))
field[0][0] = " "
for i in range(ROW):
    field[i + 1].insert(0, str(i))

move_counter = 1
flag = " "
show()
while move_counter != 10:
    symbol = "X" if move_counter % 2 else "O"
    x, y = move()
    if move_counter == 1:
        while x != ROW // 2 + 1 and y != COL // 2 + 1:
            print("The first move should be at the center of a field")
            x, y = move()
    field[x][y] = symbol
    if check_win(x, y):
        if symbol == "X":
            flag = "X"
        else:
            flag = "O"
        break
    move_counter += 1
    show()

if flag == "X":
    print("1p wins")
elif flag == "O":
    print("2p wins")
else:
    print("draw")
