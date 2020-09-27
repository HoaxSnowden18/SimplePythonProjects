import time
from os import system, name

board = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]


def sleep():
    time.sleep(0.5)


def screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def displayBoard(bo):
    print("Welcome to TicTacToe Game\n")
    sleep()
    for count, row in enumerate(bo):
        print(" ", f"{row[0]} | {row[1]} | {row[2]}")
        if count == 2:
        	pass
        else:
        	print(" ", "----------")

def board_check(bo):
    l = []
    m = []
    n = []
    # Checks each row
    if set(bo[0]) == {"X"}:
        print(f"{player1} Wins!")
        return True
    elif set(bo[1]) == {"X"}:
        print(f"{player1} Wins!")
        return True
    elif set(bo[2]) == {"X"}:
        print(f"{player1} Wins!")
        return True
    elif set(bo[0]) == {"X"}:
        print(f"{player1} Wins!")
        return True
    elif set(bo[1]) == {"X"}:
        print(f"{player1} Wins!")
        return True
    elif set(bo[2]) == {"X"}:
        print(f"{player1} Wins!")
        return True
    else:
        print("", end="")

    if set(bo[0]) == {"O"}:
        print(f"{player2} Wins!")
        return True
    elif set(bo[1]) == {"O"}:
        print(f"{player2} Wins!")
        return True
    elif set(bo[2]) == {"O"}:
        print(f"{player2} Wins!")
        return True
    elif set(bo[0]) == {"O"}:
        print(f"{player1} Wins!")
        return True
    elif set(bo[1]) == {"O"}:
        print(f"{player1} Wins!")
        return True
    elif set(bo[2]) == {"O"}:
        print(f"{player1} Wins!")
        return True
    else:
        print("", end="")

    # Checks each column
    for i in range(len(board)):
        vert = board[i][0]
        if vert == "X" or vert == "O":
            l.append(vert)
        else:
            l.append("")

    if set(l) == {"X"}:
        print(f"{player1} Wins!")
        return True
    elif set(l) == {"O"}:
        print(f"{player2} Wins!")
        return True
    else:
        print("", end="")

    for i in range(len(board)):
        vert = board[i][1]
        if vert == "X" or vert == "O":
            m.append(vert)
        else:
            m.append("")

    if set(m) == {"X"}:
        print(f"{player1} Wins!")
        return True
    elif set(m) == {"O"}:
        print(f"{player2} Wins!")
        return True
    else:
        print("", end="")

    for i in range(len(board)):
        vert = board[i][2]
        if vert == "X" or vert == "O":
            n.append(vert)
        else:
            n.append("")

    if set(n) == {"X"}:
        print(f"{player1} Wins!")
        return True
    elif set(n) == {"O"}:
        print(f"{player2} Wins!")
        return True
    else:
        print("", end="")

    # Checks diagonals
    e = []
    for count, row in enumerate(bo):
        if row[count] == "X" or row[count] == "O":
            e.append(row[count])
        else:
            e.append(" ")
    if set(e) == {"X"}:
        print(f"{player1} Wins!")
        return True
    elif set(e) == {"O"}:
        print(f"{player2} Wins!")
        return True
    else:
        print("")
    f = []
    for count, row in enumerate(bo):
        if row[~count] == "X" or row[~count] == "O":
            f.append(row[~count])
        else:
            f.append(" ")
    if set(f) == {"X"}:
        print(f"{player1} Wins!")
        return True
    elif set(f) == {"O"}:
        print(f"{player2} Wins!")
        return True
    else:
        print("")


displayBoard(board)
sleep()

player1 = input("What is your name player 1?: ")
sleep()
player2 = input("What is your name player 2?: ")
sleep()
x = True


def xans(bo):
    global x
    try:
        useri = int(input("Where do you want to put the X on? "))
    except BaseException:
        print("Enter Number")
    if useri == 1 and bo[0][0] != "X":
        bo[0][0] = "X"
    elif useri == 2 and bo[0][1] != "X":
        bo[0][1] = "X"
    elif useri == 3 and bo[0][2] != "X":
        bo[0][2] = "X"
    elif useri == 4 and bo[1][0] != "X":
        bo[1][0] = "X"
    elif useri == 5 and bo[1][1] != "X":
        bo[1][1] = "X"
    elif useri == 6 and bo[1][2] != "X":
        bo[1][2] = "X"
    elif useri == 7 and bo[2][0] != "X":
        bo[2][0] = "X"
    elif useri == 8 and bo[2][1] != "X":
        bo[2][1] = "X"
    elif useri == 9 and bo[2][2] != "X":
        bo[2][2] = "X"
    else:
        print("Invalid Input, enter 1-9 or There is already a mark there")
    screen()
    displayBoard(bo)
    x = False


def oans(bo):
    global x
    try:
        useri = int(input("Where do you want to put the O on? "))
    except BaseException:
        print("Enter Number")
    if useri == 1 and bo[0][0] != "O":
        bo[0][0] = "O"
    elif useri == 2 and bo[0][1] != "O":
        bo[0][1] = "O"
    elif useri == 3 and bo[0][2] != "O":
        bo[0][2] = "O"
    elif useri == 4 and bo[1][0] != "O":
        bo[1][0] = "O"
    elif useri == 5 and bo[1][1] != "O":
        bo[1][1] = "O"
    elif useri == 6 and bo[1][2] != "O":
        bo[1][2] = "O"
    elif useri == 7 and bo[2][0] != "O":
        bo[2][0] = "O"
    elif useri == 8 and bo[2][1] != "O":
        bo[2][1] = "O"
    elif useri == 9 and bo[2][2] != "O":
        bo[2][2] = "O"
    else:
        print("Invalid Input, enter 1-9 or There is already a mark there")
    screen()
    displayBoard(board)
    x = True


count = 0
while count != 9:
    if x:
        xans(board)
        count += 1
        if board_check(board):
            break
    else:
        oans(board)
        count += 1
        if board_check(board):
            break
else:
    print("You are out of moves")
