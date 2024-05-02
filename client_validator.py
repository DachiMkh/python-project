from iban_generator import iban_creator

def check_client_info(name,surname):
    if  not name.isdigit() or not surname.isdigit():
        return True
    else:
        print("Please Enter correct information")
        name = input("Enter your name: ")
        surname = input("Enter your surname: ")


def check_iban(iban):
    if len(iban) != 6 or iban[:2] != "TB" or not iban[2:].isdigit():
        print("Invalid Bank number!")
        return False
    return True

def check_in_db_register(database,iban):
    for record in database:
        if record["bank_no"] == iban:
            iban = iban_creator()

def check_start_balance(amount):
    if amount < 100 and amount > 0:
        return True
    
    while int(amount) > 100 and int(amount) < 0:
        print("Please Enter less than 100 and more than 0!")
        amount=input("Please enter amount: ")

    while int(amount) < 0  :
        print("Balance can not be negative")
        amount=input("Please enter amount: ")