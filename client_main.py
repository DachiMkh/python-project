# ანგარიშის შექმნა:

#     მომხმარებელები შექმნიან ახალ საბანკო ანგარიშსს მათი სახელისა და საწყისი ბალანსის შეყვანით, საწყისი ბალანსი არ უნდა იყოს 100 ლარზე მეტი.
#     სისტემა დაუგენერირებს უნიკალურ ანგარიშის ნომერს თითოეული ანგარიშისთვის (ფორმატი: TB0000 - TB9999).


from iban_generator import iban_creator
import client_validator as vl

database=[]

def register_customer():
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    vl.check_client_info(name,surname)

    amount = input("Please enter Amount: ")
    vl.check_start_balance(amount)

    iban = iban_creator()
    vl.check_iban(iban)
    vl.check_in_db_register(database,iban)

    record = {
        "name" : name, 
        "surname" : surname, 
        "bank_no" : iban,
        "balance" : amount
    }

    database.append(record)
    print(record["bank_no"])



def bank_no_details():
    iban=input("Please enter bank_no: ")
    vl.check_iban(iban)
    for record in database:
        if record["bank_no"] == iban:
            print(database)
        else:
            print("There is not such iban")

actions = {
    "register_customer" : register_customer,
    "bank_no_details" : bank_no_details
}


input_actions=input(f"Please enter action {actions.keys()}: ")

while input_actions in actions.keys():
    actions[input_actions]()
    input_actions=input(f"Please enter action {actions.keys()}: ")
