from client_validator import check_client_info
import client_main as main

def money_transfer(giver, getter, amount):
    giver_record = check_client_info(giver)
    getter_record = check_client_info(getter)

    if giver_record and getter_record:
        giver_balance = float(giver_record.get("balance"))
        getter_balance = float(getter_record.get("balance"))

        if giver_balance >= amount:
            print("Processing....")
            giver_balance -= amount
            getter_balance += amount
            giver_record['balance'] = giver_balance
            getter_record['balance'] = getter_balance
            main.record.append({"bank_no": giver, "bank_no": getter, "balance": amount})
            print("Transfer completed successfully.")
        else:
            print("Insufficient balance in giver's account.")
    else:
        print("One or both of the accounts do not exist.")