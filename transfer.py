from client_validator import check_client_info
import client_main as main
import history as h

def money_transfer():
    giver = input("who is giving the money: ")
    getter = input("who is reciveing the money: ")
    amount = int(input("how much: "))

    
    if giver and getter:
        for user in main.database:
            if user["bank_no"] == giver:
                giver_balance = user["balance"]

        for  user in main.database:
              if user["bank_no"] == getter:
                getter_balance = user["balance"]


        if giver_balance >= amount:
            print("Processing....")
            giver_balance -= amount
            getter_balance += amount
            main.database.append({"bank_no": giver, "bank_no": getter, "balance": amount})
            print("Transfer completed successfully.")
            for user in main.database:
                if user.get("bank_no") == giver:
                    var1, var2, var3, var4 = user["name"], user["surname"], user["bank_no"], amount
                    h.trans_log(var1, var2, var3, var4)
        else:
            print("Insufficient balance in giver's account.")
    else:
        print("One or both of the accounts do not exist.")