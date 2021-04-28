import random

data_dict = {"card_number":[], "pin_number": []}
whole_num = None

while True:

    print("1. Create an account\n2. Log into account\n0. Exit")
    operator = input()

    if operator == "1":
        print()
        card_num = "400000" + "{:09d}".format(random.randint(0, 999999999))
        card_num_lst = [int(num) for num in card_num]
        card_num_sum = 0
        for i in range(0, len(card_num_lst), 2):
            card_num_lst[i] *= 2
        for i in range(len(card_num_lst)):
            if card_num_lst[i] > 9:
                card_num_lst[i] -= 9
        for i in range(len(card_num_lst)):
            card_num_sum += card_num_lst[i]
        for i in range(9):
            if (card_num_sum + i) % 10 == 0:
                whole_num = card_num + str(i)
                i += 10
                int_whole_card_num = int(whole_num)
        pin_num = "{:04d}".format(random.randint(0, 9999))
        data_dict["card_number"].append(whole_num)
        data_dict["pin_number"].append(pin_num)
        print("Your card has been created\nYour card number:")
        print(int_whole_card_num)
        print("Your card PIN\n" + pin_num)
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