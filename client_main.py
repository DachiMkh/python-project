# ანგარიშის შექმნა:

#     მომხმარებელები შექმნიან ახალ საბანკო ანგარიშსს მათი სახელისა და საწყისი ბალანსის შეყვანით, საწყისი ბალანსი არ უნდა იყოს 100 ლარზე მეტი.
#     სისტემა დაუგენერირებს უნიკალურ ანგარიშის ნომერს თითოეული ანგარიშისთვის (ფორმატი: TB0000 - TB9999).

import iban_generator as ib
import client_validator as vl

database = []

def register_customer():
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    vl.check_client_info(name, surname)

    amount = int(input("Please enter Amount: "))
    vl.check_start_balance(amount)

    iban = ib.iban_creator()
    vl.check_iban(iban)
    vl.check_in_db_register(database, iban)

    percent = ib.percent_creator()
    user_id = ib.user_id_creator()
    ib.user_log(name, surname, iban, user_id)

    record = {
        "name": name,
        "surname": surname,
        "bank_no": iban,
        "balance": amount,
        "percent": percent
    }

    database.append(record)
    print(record["bank_no"])




def bank_no_details():
    iban = input("Please enter bank_no: ")
    vl.check_iban(iban)
    for record in database:
        if record["bank_no"] == iban:
            print(record)
            return
    print("There is not such iban")
