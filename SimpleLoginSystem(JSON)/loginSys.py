import json
import datetime
import time
import random
from os import system, name
import getpass
import os.path
import hashlib


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


def register():
    fname = input("Please enter your first name: ")
    lname = input("Please enter your last name: ")
    uname = input("Please enter your username (That will be used when you log in): ")
    while True:
        upass = getpass.getpass("Please enter your pass: ")
        upassVerify = getpass.getpass("Please enter your password again: ")
        if upass == upassVerify:
            break
        elif upass != upassVerify:
            print("Passwords do not match, try again..")
            continue
    upass = hashlib.sha256(upass.encode())
    datereged = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")

    data = dict()

    user = dict()
    user["fname"] = fname
    user["lname"] = lname
    user["uname"] = uname
    user["upass"] = upass.hexdigest()
    user["dateregistered"] = datereged

    data[user["uname"]] = user

    if os.path.isfile("users.json"):
        with open("users.json", "r+") as file:
            dataF = json.load(file)
            dataF.update(data)
            file.seek(0)
            json.dump(dataF, file, indent=2)
    else:
        with open("users.json", "w") as f:
            json.dump(data, f, indent=2)

    print("Data Registered, you can now login!")
    passi = input("Press enter to continue")
    sleep(0.6)
    clear()
    mainPrompt()


def login():
    sleep(0.5)
    clear()
    with open("users.json") as f:
        data = json.load(f)

    print("Please login")
    while True:
        uname = input("Enter username: ")
        upass = getpass.getpass("Enter password: ")
        upass = hashlib.sha256(upass.encode())
        if uname in data and data[uname]["upass"] == upass.hexdigest():
            print("Logged in, please wait")
            sleep(1)
            clear()
            loginRights(uname, upass)
            break
        else:
            print("Wrong username or password, or account not exists")
            continue


def loginRights(uname, upass):
    with open("users.json") as f:
        data = json.load(f)
    print(f"Welcome back {data[uname]['uname']} \n")
    print("What do you want to do:")
    print("1. See your info")
    print("2. Rename Account")
    print("3. Delete Account")
    print("4. Change Password")
    print("5. Logout")
    while True:
        userIn = input(">>> ")
        if userIn == "1":
            print("Wait gathering info...\n")
            sleep(0.5)
            print(f"Your first name is: {data[uname]['uname']}")
            print(f"Your last name is: {data[uname]['lname']}")
            print(f"Your account username is: {data[uname]['uname']}")
            print(f"Your account is created at: {data[uname]['dateregistered']}")
            print("Data Gathered..")
            passer = input("Press enter to continue: ")
            sleep(0.5)
            clear()
            loginRights(data[uname]["uname"], data[uname]["upass"])
        elif userIn == "2":
            newUserName = input("Enter your new username: ")
            data[uname]["uname"] = newUserName
            data[newUserName] = data.pop(uname)
            uname = newUserName
            sleep(0.5)
            print("Renamed Succesfully")
            passer = input("Press enter to continue")
            sleep(0.5)
            clear()
            with open("users.json", "w") as f:
                json.dump(data, f, indent=2)
            loginRights(data[uname]["uname"], data[uname]["upass"])
            break
        elif userIn == "3":
            with open("users.json", "r") as f:
                data = json.load(f)
            print("Deleting Account..")
            sleep(0.8)

            del data[uname]

            with open("users.json", "w") as f:
                json.dump(data, f, indent=2)

            print("Deleted!")
            passer = input("Please press enter to continue..")
            sleep(0.5)
            clear()
            mainPrompt()
            break
        elif userIn == "4":
            with open("users.json") as f:
                data = json.load(f)

            while True:
                newPass = getpass.getpass("Please enter your new password: ")
                newPassVerify = getpass.getpass("Please enter your password again: ")
                if newPass == newPassVerify:
                    print("Changing password...")
                    sleep(0.5)
                    newPass = hashlib.sha256(newPass.encode())
                    data[uname]["upass"] = newPass.hexdigest()
                    upass = newPass

                    with open("users.json", "w") as f:
                        json.dump(data, f, indent=2)
                    clear()
                    loginRights(data[uname]["uname"], data[uname]["upass"])
                else:
                    print("Passwords do not match, try again")
                    continue

        elif userIn == "5":
            print("Logging out")
            sleep(0.1)
            # passer = input("Logged out, press enter to continue")
            sleep(0.5)
            clear()
            mainPrompt()
            break
        else:
            print("Invalid input, please type (1/2/3/4) only!")
            continue
