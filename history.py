import client_main as main

def transfer_history(bank_no):
    print("Transaction History for Bank No:", bank_no)
    for record in main.record:
        if record["bank_no"] == bank_no:
            print("Transfer to:", record["bank_no"], "Amount:", record["balance"])
        else:
            print("error")