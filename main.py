import datetime

# Creating path for transactions filterng
def trans_filtering(trans):
    for comment, amount in trans.items():
        yield comment, amount

# Realize logics for transactions filtering
# Work with path, created in "trans_filtering" function
def trans_filtering_logics(trans, filter_trans):
    for comment, amount in trans_filtering(trans):
        if amount >= filter_trans:
            print(comment + ": " + str(amount) + " rubl")

# new client creation procedure
def account_creation():
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    year_of_birth = int(input("Enter your year of birth: "))
    password = input("Enter your password: ")
    clientfout(name, surname, year_of_birth, password, 1_000, 0)  # 1000 - beginning limit.
    # 0 - beginning money balance
    print("Congratulation!!!\nYou have successfully created new account\n ")


# Money addition
def monyadd(money_func, bill_func, account_limit):
    if (money_func + bill_func) > account_limit:
        print("The limit on your account has been exceeded!\nOperation canceled")
    else:
        money_func += bill_func
        print("Account has been successfully added!\n")
        return money_func


# Money withdraw function
def monywithdr(money, withdraw_bill):
    print("Your current balance is: " + str(money))

    if (money - withdraw_bill) < 0:
        print("You do not have enough money\nto complete this operation")
    else:
        money -= withdraw_bill
        print("Withdrawal completed successfully")
        print("Your current balance is: " + str(money) + "\n")
        return money


# Apply transactions
def apply_trans(money, limit_account):
    for comment, amount in transactions.items():
        if (money + int(amount)) > limit_account:
                print("Transaction: " + comment + "\ncannot be applied (limit exceeded)\n")
        else:
            if int(transactions[comment]) > 0:
                money += int(amount)
                print("Transaction: " + comment + "\nsuccessfully applied\n")
                transactions[comment] = 0
    transactionfout(transactions)
    return money


# Writing information about client in to file
def clientfout(name_to_file, surname_to_file, year_of_birth_to_file, password_to_file, account_limit_to_file,
               money_to_file):
    with open('bank_client.txt', 'w') as fout:
        fout.write(name_to_file + '\n')
        fout.write(surname_to_file + '\n')
        fout.write(str(year_of_birth_to_file) + '\n')
        fout.write(password_to_file + '\n')
        fout.write(str(account_limit_to_file) + '\n')
        fout.write(str(money_to_file) + '\n')
    fout.close()


# Password checking
def pass_check(pswd_tmp, password_fail):
    if password_fail != pswd_tmp or not password_fail:
        print("Wrong password!")
        return False
    else:
        return True


# Reading client data from file to program
def client_from_file():
    try:
        with open('bank_client.txt') as clientfin:
            count = 0
            for line in clientfin:
                count = count + 1
                if count == 1:
                    name = line[:-1]
                elif count == 2:
                    surname = line[:-1]
                elif count == 3:
                    year_of_birth = int(line[:-1])
                elif count == 4:
                    password = line[:-1]
                elif count == 5:
                    account_limit = int(line[:-1])
                elif count == 6:
                    money_from_file = int(line[:-1])
    except FileNotFoundError:
        print("Your bank data is lost!\nPlease contact to the bank administration!")
        exit()
    clientfin.close()
    try:
        client_from_file_kortezh = (name, surname, year_of_birth, password, account_limit, money_from_file)
    except UnboundLocalError:
        print("Your bank data is lost!\nPlease contact to the bank administration!")
        exit()
    return (client_from_file_kortezh)


# Reading transaction from file to dictionary
def transaction_from_file():
    transactionstmp = {}
    count = 0
    with open('transactions.txt') as transfout:
        for line in transfout:
            count += 1
            if (count % 2) != 0:
                commenttmp = line[:-1]
            else:
                transactionstmp[commenttmp] = int(line[:-1])
    return transactionstmp


# Writing Transaction dictionary in to file
def transactionfout(trans):
    with open('transactions.txt', "w") as tranfout:
        for comment2, amount2 in trans.items():
            if amount2 > 0:
                tranfout.write(comment2 + '\n')
                tranfout.write(str(amount2) + '\n')



# Starting cycle of progamms
print("\n******************************************")
print("Welcome to the console banking application")
print("Version 3.0")
print("******************************************\n")

print("Hi! Friend!\nRestore data from file?")
choice = input("Y / N: ")
if choice == "Y" or choice == "y":
    count = 0
    client_restored = client_from_file()
    transactions = transaction_from_file()
    print("Your data are restored!\n")
else:
    client_restored = ("", "", 0, "", 0, 0)
    transactions = {}
    print("Your data isn`t restored!\n")
while True:
    print("What would you like to do?")
    print("1. Create a bank account")
    print("2. Put money into the account")
    print("3. Withdraw money")
    print("4. Display")
    print("5. Expected transactions")
    print("6. Account limit setting")
    print("7. Apply transactions")
    print("8. Statistic of expected transactions")
    print("9. Filtering of expected transactions")
    print("10. Exit\n")
    choice = int(input("Enter your choice: "))

    # Bank account creation
    if choice == 1:
        account_creation()

        # Money addition
    elif choice == 2:
            bill = int(input("How much money do you want to deposit into your account: "))
            money = monyadd(client_from_file()[5], bill, client_from_file()[4])
            clientfout(client_from_file()[0], client_from_file()[1], client_from_file()[2], client_from_file()[3],
                   client_from_file()[4], money)

    # Money withdraw
    elif choice == 3:
        if pass_check(input("Enter your password: "), client_from_file()[3]):
                withdraw_bill = int(input("How much money do you want to withdraw from your account: "))
                print("Please enter a number")
                clientfout(client_from_file()[0], client_from_file()[1], client_from_file()[2], client_from_file()[3],
                           client_from_file()[4], monywithdr(client_from_file()[5], withdraw_bill))

    # Display balance
    elif choice == 4:
        if pass_check(input("Enter your password: "), client_restored[3]):
            print("Your current balance is: " + str(client_from_file()[5]) + "\n")

    # Expected transactions
    elif choice == 5:
            transaction_money = int(input("How much money do you want to get: "))
            transaction_comment = input("Comments for this transaction: ")
            current_date = datetime.datetime.now()
            current_date.strftime('%m/%d/%y %H:%M:%S')
            transactions[transaction_comment + " (" + current_date.strftime('%m/%d/%y %H:%M:%S') + ")"] \
            = transaction_money
            print("\nYour expected transactions is successfully added!\nin transaction list")
            print("You have a " + str(len(transactions)) + " transactions\n")
            transactionfout(transactions)

    # Account limit setting
    elif choice == 6:
            account_limit = int(input("Enter maximum balance of money,\nthat can be stored in your account?: "))
            print("Please enter a number")
            clientfout(client_from_file()[0], client_from_file()[1], client_from_file()[2], client_from_file()[3],
                   account_limit, client_from_file()[5])
            print ("Your maximum balance of money is " + str(account_limit) + "!\n")

    # Apply transactions
    elif choice == 7:
        clientfout(client_from_file()[0], client_from_file()[1], client_from_file()[2], client_from_file()[3],
                   client_from_file()[4], apply_trans(client_from_file()[5], client_from_file()[4]))

    # Statistics on expected transactions
    elif choice == 8:
        amounts = {}
        for comment, amount in transactions.items():
            if amount not in amounts and amount > 0 :
                amounts[amount] = 1
            elif amount > 0:
                amounts[amount] += 1
        print("Expected:")
        for amount, freq in amounts.items():
            print(str(amount) + " eur: " + str(freq) + " transactions")
        print("\n")

    # Filtering of expected transactions
    elif choice == 9:
        transfiltr = int(input("Please, enter a lower filter\n"
                                       "for transactions summ: "))
        trans_filtering_logics(transactions, transfiltr)


    # Exit
    elif choice == 10:
        print("Thanks, goodbye!")
        break

    # Other operation numbers
    else:
            print("Wrong operation number, please try again!" + "\n")
