import random
import sqlite3
import time
from os import system, name


letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
specialsym = r"@#$%&*-+()!\"':;/?{}[]=><\_^"

strong = letters + numbers + specialsym
medium = letters + numbers
weak = letters

conn = sqlite3.connect("password.db")
c = conn.cursor()


def createTable():
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS passLists(password TEXT, strength TEXT)
        """
    )


def insertData(password, strength):
    c.execute(
        "INSERT INTO passLists(password, strength) VALUES(?,?)", (password, strength)
    )
    conn.commit()


def getPass():
    c.execute("SELECT * FROM passLists")
    for row in c.fetchall():
        print(f"Pass: {row[0]}, Strength: {row[1]}")


def sleep(n):
    time.sleep(n)


def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


def askForDB(strength):
    if strength == "weak":
        c.execute('SELECT * FROM passLists WHERE strength = "weak"')
        for row in c.fetchall():
            print(f"Pass: {row[0]}, Strength: {row[1]}")
    elif strength == "medium":
        c.execute('SELECT * FROM passLists WHERE strength = "medium"')
        for row in c.fetchall():
            print(f"Pass: {row[0]}, Strength: {row[1]}")
    elif strength == "strong":
        c.execute('SELECT * FROM passLists WHERE strength = "strong"')
        for row in c.fetchall():
            print(f"Pass: {row[0]}, Strength: {row[1]}")
    elif strength == "all":
        getPass()


def generatepass(size):
    if size <= 8:
        return "".join(random.choice(letters) for i in range(size))
    elif size <= 15:
        return "".join(random.choice(medium) for i in range(size))
    else:
        return "".join(random.choice(strong) for i in range(size))


createTable()


def display():
    print("Welcome to Password Generator")
    print("Strong - 16-28 Characters, Using Letters, Numbers and Special Symbols")
    print("Medium - 9-15 Characters, Using Letters and Numbers")
    print("Weak - 4-8 Characters, Using Letters Only")
    print("SeePass - Lets You See the Saved Passwords You Made")
    print("Clear - Lets You Clear the Screen")
    print("Quit - Quits Program")


display()
isdone = False
while not (isdone):
    ask = input("\nStrong/Medium/Weak/SeePass/Clear or Quit?: ")
    if ask.lower() == "quit" or ask.lower() == "q":
        isdone = True
    elif ask.lower() == "strong" or ask.lower() == "s":
        a = generatepass(random.randint(16, 28))
        insertData(a, "strong")
        print(a)
    elif ask.lower() == "medium" or ask.lower() == "m":
        b = generatepass(random.randint(9, 15))
        insertData(b, "medium")
        print(b)
    elif ask.lower() == "weak" or ask.lower() == "w":
        c = generatepass(random.randint(4, 8))
        insertData(c, "weak")
        print(c)
    elif ask.lower() == "seepass" or ask.lower() == "sp":
        print("\nPlease wait... I'm Gathering Data")
        sleep(0.6)
        while True:
            uIn = input("Please Choose (Strong/Medium/Weak/All): ")
            if uIn.lower() == "strong" or uIn.lower() == "s":
                askForDB("strong")
                break
            elif uIn.lower() == "medium" or uIn.lower() == "m":
                askForDB("medium")
                break
            elif uIn.lower() == "weak" or uIn.lower() == "w":
                askForDB("weak")
                break
            elif uIn.lower() == "all" or uIn.lower() == "a":
                askForDB("all")
                break
            else:
                print("Invalid Input")
                continue
    elif ask.lower() == "clear" or ask.lower() == "c":
        print("Clearing Your Screen Please Wait")
        sleep(0.5)
        clear()
        display()
    else:
        print("Invalid Input")
