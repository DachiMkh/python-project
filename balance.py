'''
ბალანსი:
მომხმარებელს შეუძლიათ ფულის შეტანა თავიაანთ ანგარიშზე, ანგარიშის ნომრის მითითებით
'''

import client_main as main
import client_validator as cm
import history as h


def topup_balance():
    iban = input("please enter your iban: ")
    while cm.check_iban(iban) != True:
        iban = input("please enter valid iban: ")
    balance = int(input("enter your amount: "))
    for user in main.database:
        if user.get("bank_no") == iban:
            user["balance"] += balance
            var1, var2, var3, var4 = user["name"], user["surname"], user["bank_no"], balance
            h.trans_log(var1, var2, var3, var4)
            

