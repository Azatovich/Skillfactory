def greet(): # Приветсвие
    print(" Игра в крестики нолики ")
    print("   Формат ввода: x и y  ")
    print("   x - номер строки     ")
    print("   y - номер столбца    ")
    
greet()

filed = [[" "] * 3 for i in range(3) ]

def show(): # Создаем поля для игры.
    print()
    print("   | 0 | 1 | 2 |")
    print("   -------------")
    for i, row in enumerate(filed):
        row_str = f" {i} | {' | '.join(map(str, row))} | "
        print(row_str)
        print("  --------------")
    print()

def ask (): # Ввод координат.
    while True:
        cords = input("       Ваш ход: ").split()
        if len(cords)!= 2:
            print(" Введите 2 координаты! ")
            continue
        x,y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа!: ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Коорнинаты не верны! ")
            continue
        if filed[x][y]!= " ":
            print("Клетка занята!")

        return x, y
def chek_win(): # Выйгрышные комбинации
    win_cord = (((0, 0), (0, 1),(0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(filed[c[0]][c[1]])
        if symbols == ["x", "x", "x "]:
            print("Выйграл X! ")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выйграл 0! ")
            return True
    return False

num = 0
while True:
    num += 1
    show()
    if num % 2 == 1:
        print("Ходит крестик! ")
    else:
        print("Ходит нолик! ")

    x, y = ask()

    if num % 2 == 1:
        filed[x][y] = "X"
    else:
        filed[x][y] = "0"

    if chek_win():
        break
    if num == 9: # Проверка на ничью!
        break
        print("Ничья! ")



