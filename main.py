def check(ch_row, ch_col):
    symbol = field[ch_row][ch_col]
    win_con_row = 0
    win_con_col = 0
    for i in range(row):
        if field[i][ch_col] == symbol:
            win_con_row += 1

    for i in range(col):
        if field[ch_row][i] == symbol:
            win_con_col += 1

    if win_con_col == 3 or win_con_row == 3:
        return True
    else:
        return False


def move():
    x, y = list(map(int, input("Enter your move in format: row col").split()))
    while not (0 <= x < row and 0 <= y < col):
        x, y = list(map(int, input("Incorrect data, try again").split()))

    return x, y


def show():
    print(" | ".join(field[0]) + " |")
    print("-" * (row + 1) * 4)
    for i in range(1, row + 1):
        print(" | ".join(field[i]) + " |")
        print("-" * (row + 1) * 4)


row = col = 3
field = [[" " for _ in range(col)] for _ in range(row)]
field.insert(0, list(map(str, range(-1, col))))
field[0][0] = " "
for i in range(row):
    field[i + 1].insert(0, str(i))

move_counter = 1
flag = " "
show()
while True:
    symbol = "X" if move_counter % 2 else "O"
    x, y = move()
    if move_counter == 1:
        while x != row // 2 + 1 or y != col // 2 + 1:
            print("The first move should be at the center of a field")
            x, y = move()
    if check(x, y):
        if symbol == "X":
            flag = "X"
        else:
            flag = "O"
        break
    field[x][y] = symbol
    move_counter += 1
    show()

if flag == "X":
    print("1p wins")
else:
    print("2p wins")
