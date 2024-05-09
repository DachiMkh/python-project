import client_main as main
import client_validator as cv

def trans_log (var1, var2, var3, var4):
    transaction_details = (f"{var1}, {var2}, {var3}, {var4} \n")
    with open("transactions.txt", "a") as file:
        file.write(transaction_details)

def transfer_history():
    bank_no = input("enter your bank number: ")
    cv.check_iban(bank_no)
    print("Transaction History for Bank No:", bank_no)
    for record in main.database:
        if record["bank_no"] == bank_no:
            print("Transfer to:", record["bank_no"], "Amount:", record["balance"])
            return
        else:
            print("error")
            continue

