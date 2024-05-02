'''
ბალანსი:
მომხმარებელს შეუძლიათ ფულის შეტანა თავიაანთ ანგარიშზე, ანგარიშის ნომრის მითითებით
'''

import client_main as main


def topup_balance(iban, balance):
    for user in main.database:
        if user.get("bank_no") == iban:
            user["balance"] += balance