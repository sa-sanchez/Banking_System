import sqlite3
import random
conn = sqlite3.connect("card.s3db")

cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS card(id INTEGER PRIMARY KEY AUTOINCREMENT, number TEXT, pin TEXT, balance INTEGER DEFAULT 0);""")
whole_num = None


def main(number):
    global control
    control = number


def login(card_inp):
    while True:
        option = input("1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit\n")
        print()
        if option == "1":
            cur.execute("""SELECT balance FROM card WHERE number = {};""".format(card_inp))
            bal = cur.fetchone()
            print("Balance: " + str(bal[0]))
            print()

        elif option == "2":
            income = int(input("Enter income:\n"))
            cur.execute("""SELECT balance FROM card WHERE number = {};""".format(card_inp))
            current_bal = int(cur.fetchone()[0])
            cur.execute("""UPDATE card SET balance = {} WHERE number = {};""".format((income + current_bal), card_inp))
            conn.commit()
            print("Income was added!")
            print()

        elif option == "3":
            card_number = input("Transfer\nEnter card number:\n")
            cur.execute("""SELECT number FROM card WHERE number = {};""".format(card_number))
            card_value = cur.fetchone()

            card_num_lst = [int(num) for num in card_number]
            card_num_sum = 0
            for i in range(0, len(card_num_lst), 2):
                card_num_lst[i] *= 2
            for i in range(len(card_num_lst) - 1):
                if card_num_lst[i] > 9:
                    card_num_lst[i] -= 9
            for i in range(len(card_num_lst) - 1):
                card_num_sum += card_num_lst[i]            

            if card_number == card_inp: # Same card
                print("You can't transfer money to the same account!")
                print()
            elif (card_num_sum + card_num_lst[15]) % 10 != 0: #Luhn algorithm
                print("Probably you made a mistake in the card number. Please try again!")
                print()            
            elif bool(card_value):
                money = int(input("Enter how much money you want to transfer:\n"))
                cur.execute("""SELECT balance FROM card WHERE number = {};""".format(card_inp))
                money_value = cur.fetchone()[0]
                if (money_value - money) >= 0:
                    left_money = money_value - money
                    cur.execute("""UPDATE card SET balance = {} WHERE number = {};""".format(left_money, card_inp))
                    conn.commit()
                    cur.execute("""UPDATE card SET balance = {} WHERE number = {};""".format(money, card_number))
                    conn.commit()
                    print("Success!")
                    print()
                else:
                    print("Not enough money!")
                    print()
            else:
                print("Such a card does not exist.")
                print()

        elif option == "4":
            cur.execute("""DELETE FROM card WHERE number = '{}'""".format(card_inp))
            conn.commit()
            print("The account has been closed!")
            main(1)
            print()
            break
        
        elif option == "5":
            print("You have successfully logged out!")
            print()
            break
        elif option == "0":
            print("Bye!")
            main(0)               
            break
            

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
        pin_inp = input("Enter your PIN number\n")
        print()
        cur.execute("""SELECT number FROM card WHERE number = {};""".format(card_inp))
        op_1 = cur.fetchone()
        cur.execute("""SELECT pin FROM card WHERE pin = {};""".format(pin_inp))
        op_2 = cur.fetchone()

        if bool(op_1) and bool(op_2):
            print("You have successfully logged in!")
            print()

            login(card_inp)
            if control == 0:
                break

        else:
            print("Wrong card number or PIN!")
            print()
    elif operator == "0":
        print()
        print("Bye!")
        break