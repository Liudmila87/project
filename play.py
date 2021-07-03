def greet():
    print("Приветствуем Вас в игре крестики-нолики")
    print("Первый ход - X")
    print("Чтобы сделать ход")
    print("укажите номер строки")
    print("укажите номер столбца")


greet()


field = [[" "] * 3 for i in range(3)]


def show():
    print()
    print("   | 0 | 1 | 2 | ")
    print(" --------------- ")
    for i, row in enumerate(field):
        rows = f" {i} | {' | '.join(row)} | "
        print(rows)
    print(" --------------- ")
    print()


show()


def input_check():
    while True:
        cord_str = input("Ведите координаты хода: ").split()
        if not cord_str:
            print("Вы ничего не ввели")
            continue
        if len(cord_str) != 2:
            print("Введите 2 координаты")
            continue
        x, y = cord_str
        if not (x.isdigit()) or not (y.isdigit()):
            print("Введите числа")
            continue
        x, y = int(x), int(y)
        if 0 <= x <= 2 and 0 <= y <= 2:
            if field[x][y] != " ":
                print("Клетка занята")
                continue
        else:
            print("Введены некорректные координаты. X и Y не могут быть меньше 0 или больше 2")
            continue
        return x, y


def win_check():
    win_cord = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2))]
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print(" ")
            print("Выиграл X")
            print(" ")
            return True
        if symbols == ["0", "0", "0"]:
            print(" ")
            print("Выиграл 0")
            print(" ")
            return True
    return False


count = 0
while True:
    count += 1
    show()
    if count % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")
    x, y = input_check()
    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if win_check():
        break

    if count == 9:
        print(" Ничья!")
        break


