import sqlite3
import random
conn = sqlite3.connect("card.s3db")

cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS card(id INTEGER PRIMARY KEY AUTOINCREMENT, number TEXT, pin TEXT, balance INTEGER DEFAULT 0);""")
whole_num = None
card_id = 0

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
        pin_num = str("{:04d}".format(random.randint(1000, 9999)))
        cur.execute("""INSERT INTO card (number, pin) VALUES (?, ?);""", (whole_num, pin_num))
        conn.commit()
        print("Your card has been created\nYour card number:")
        cur.execute("""SELECT number FROM card WHERE number = {};""".format(whole_num))
        print(cur.fetchone()[0])
        print("Your card PIN")
        cur.execute("""SELECT pin FROM card WHERE pin = {};""".format(pin_num))
        print(cur.fetchone()[0])
        print()
    elif operator == "2":
        print()
        card_inp = input("Enter your card number\n")
        pin_inp = input("Enter your card number\n")
        print()
        cur.execute("""SELECT number FROM card WHERE number = {};""".format(card_inp))
        op_1 = cur.fetchone()
        cur.execute("""SELECT pin FROM card WHERE pin = {};""".format(pin_inp))
        op_2 = cur.fetchone()

        if bool(op_1) and bool(op_2):
            print("You have successfully logged in!")
            print()

            option = input("1. Balance\n2. Log out\n0. Exit\n")
            print()
            if option == "1":
                cur.execute("""SELECT balance FROM card WHERE number = card_inp;""")
                bal = cur.fetchone()
                print("Balance: " + str(bal))
                print()
            elif option == "2":
                print("You have successfully logged out!")
                print()
            elif option == "0":
                print("Bye!")
                break
        else:
            print("Wrong card number or PIN!")
            print()
    elif operator == "0":
        print()
        print("Bye!")
        break