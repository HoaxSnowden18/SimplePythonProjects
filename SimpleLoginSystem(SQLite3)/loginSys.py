import sqlite3
import datetime
import time
from os import system, name
import getpass
import hashlib


conn = sqlite3.connect("users.db")
c = conn.cursor()


def sleep(n):
    time.sleep(n)


def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


def greetUser():
    print("Welcome to the Login System! \n")


def mainPrompt():
    print("Do you want to login or register:")
    print('Type "1" to Login')
    print('Type "2" to Register \n')
    while True:
        userChoice = input(">>> ")
        if userChoice == "1":
            login()
            break
        elif userChoice == "2":
            register()
            break
        else:
            print("Wrong Input, please choose either 1 or 2 \n")


def createTable():
    c.execute(
        "CREATE TABLE IF NOT EXISTS usersLog(firstName TEXT, lastName TEXT, userName TEXT, userPass TEXT, dateRegistered TEXT)"
    )


def dataEntry(firstName, lastName, userName, userPass, dateRegistered):
    c.execute(
        "INSERT INTO usersLog (firstName, lastName, userName, userPass, dateRegistered) VALUES (?, ?, ?, ?, ?)",
        (firstName, lastName, userName, userPass, dateRegistered),
    )
    conn.commit()


def seeInfo(userName, userPass):
    global ufName
    global ulName
    global uuName
    global uuPass
    global dateReg
    c.execute(
        "SELECT * FROM usersLog WHERE userName = (?) AND userPass = (?)",
        (userName, userPass),
    )
    print("Gathering Info Please Wait... \n")
    sleep(0.5)
    for row in c.fetchall():
        ufName = f"Your first name is: {row[0]}"
        ulName = f"Your last name is: {row[1]}"
        uuName = f"Your account username is: {row[2]}"
        dateReg = f"Date Created: {row[4]}"


def delAccount(userName, userPass):
    c.execute(
        "DELETE FROM usersLog WHERE userName = (?) AND userPass = (?)",
        (userName, userPass),
    )
    print("Deleted Account Successfully")
    conn.commit()


def renameAccount(userName, userPass, newUserName):
    c.execute(
        "UPDATE usersLog SET userName = (?) WHERE userName = (?) AND userPass = (?)",
        (newUserName, userName, userPass),
    )
    sleep(0.5)
    print("Renamed account successfully")
    conn.commit()


def changePass(userName, userPass, newPass):
    c.execute(
        "UPDATE usersLog SET userPass = (?) WHERE userName = (?) AND userPass = (?)",
        (newPass, userName, userPass),
    )
    sleep(0.5)
    print("Password is changed!")
    conn.commit()


def selectUserFromDB(userName, userPass):
    c.execute(
        "SELECT * FROM usersLog WHERE userName = (?) AND userPass = (?)",
        (userName, userPass),
    )
    for row in c.fetchall():
        return row[2]


def selectPassFromDB(userName, userPass):
    c.execute(
        "SELECT * FROM usersLog WHERE userName = (?) AND userPass = (?)",
        (userName, userPass),
    )
    for row in c.fetchall():
        return row[3]


def register():
    fName = input("Enter your first name: ")
    lName = input("Enter your last name: ")
    uName = input("Enter your username(This will be used when you log in): ")
    while True:
        uPass = getpass.getpass("Enter your password: ")
        uPassVerification = getpass.getpass("Enter it again: ")
        if uPass != uPassVerification:
            print("They are not the same, please try again! \n")
            continue
        elif uPass == uPassVerification:
            break
    uPass = hashlib.sha256(uPass.encode())
    dateReged = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")

    print("\nThis are your infos:")
    print(f"Your first name is {fName}")
    print(f"Your last name is {lName}")
    print(f"Your account username is {uName}")
    print(f"Date and Time Registered: {dateReged} \n")

    print("Is this info correct?: ")
    print("Type (Yes or Y) if Correct")
    print("Type (No or N) if not")

    while True:
        userC = input(">>> ")
        if userC.lower() == "yes" or userC.lower() == "y":
            dataEntry(fName, lName, uName, uPass.hexdigest(), dateReged)
            print("Your info is registered  you can now login!")
            sleep(0.5)
            clear()
            mainPrompt()
            break
        elif userC.lower() == "no" or userC.lower() == "n":
            print("Okay, try again \n")
            sleep(0.5)
            clear()
            register()
            break
        else:
            print("You didn't entered Yes or No\n")
            continue


def login():
    global useName
    global usePass

    sleep(0.5)
    clear()
    print("Please login with your credentials \n")
    while True:
        useName = input("Please enter your username: ")
        usePass = getpass.getpass("Please enter your password: ")
        usePass = hashlib.sha256(usePass.encode())
        if useName == selectUserFromDB(
            useName, usePass.hexdigest()
        ) and usePass.hexdigest() == selectPassFromDB(useName, usePass.hexdigest()):
            sleep(0.5)
            clear()
            print("You are now logged in")
            sleep(0.5)
            loginRights(useName, usePass.hexdigest())
            break
        else:
            print("Username or password is Incorrect or you are still unregistered")
            continue


def loginRights(useName, usePass):
    clear()
    print(f"You are now logged in {selectUserFromDB(useName, usePass)}")
    print("What do you want to do?")
    print("1. See my info")
    print("2. Rename username")
    print("3. Delete this Account")
    print("4. Change password")
    print("5. Logout \n")

    while True:
        userWants = input(">>> ")
        if userWants == "1":
            seeInfo(useName, usePass)
            print(ufName)
            print(ulName)
            print(uuName)
            print(dateReg)
            print("\n")
            passin = input("Please press enter to continue")
            sleep(0.5)
            clear()
            loginRights(useName, usePass)
        elif userWants == "2":
            newName = input("Please enter your new username: ")
            renameAccount(useName, usePass, newName)
            sleep(0.5)
            somein = input("Please press enter to continue")
            clear()
            loginRights(newName, usePass)
        elif userWants == "3":
            sleep(1)
            delAccount(useName, usePass)
            passin = input("Please press Enter to Continue")
            sleep(0.5)
            clear()
            mainPrompt()
        elif userWants == "4":
            while True:
                newPass = getpass.getpass("Please enter your new password: ")
                newPassVerify = getpass.getpass(
                    "Please enter your new password again: "
                )
                if newPass == newPassVerify:
                    newPass = hashlib.sha256(newPass.encode())
                    changePass(useName, usePass, newPass.hexdigest())
                    sleep(0.5)
                    somein = input("Press enter to continue")
                    loginRights(useName, newPass.hexdigest())

        elif userWants == "5":
            print("Okay, logging out..")
            sleep(1.5)
            clear()
            mainPrompt()
        else:
            print("Wrong Input")
            continue
