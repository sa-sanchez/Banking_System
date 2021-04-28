import random

data_dict = {"card_number":[], "pin_number": []}

while True:

    print("1. Create an account\n2. Log into account\n0. Exit")
    operator = input()

    if operator == "1":
        print()
        card_num = "400000" + "{:010d}".format(random.randint(0, 9999999999))
        pin_num = "{:04d}".format(random.randint(0, 9999))
        data_dict["card_number"].append(card_num)
        data_dict["pin_number"].append(pin_num)
        print("Your card has been created\nYour card number:\n" + card_num + "\nYour card PIN\n" + pin_num)
        print()
    elif operator == "2":
        print()
        card_inp = input("Enter your card number\n")
        pin_inp = input("Enter your card number\n")
        print()
        if card_inp in data_dict["card_number"] and pin_inp in data_dict["pin_number"]:
            print("You have successfully logged in!")
            print()
            option = input("1. Balance\n2. Log out\n0. Exit\n")
            print()
            if option == "1":
                bal = 0
                print("Balance: " + str(bal))
                print()
            elif option == "2":
                print("You have successfully logged out!")
                print()
                break
            elif option =="0":
                print("Bye!")
                break
        else:
            print("Wrong card number or PIN!")
            print()
    elif operator == "0":
        print()
        print("Bye!")
        break