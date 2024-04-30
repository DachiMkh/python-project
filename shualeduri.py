# დავალება #1:#1:
# შექმენით მონცამეთა ბაზა და მისი სტრუქტურა, ბაზა წარმოდგენილი უნდა იყოს როგორც ლექსიკონი ან სია ( თქვენი სტრუქტურიდან გამომდინარე ),
# მოცემული გაქვთ ფუნქციონალები, რაც უნდა დავფაროთ:
# 1. ვარეგისტრირებთ მომხმარებელს ( კონსოლიდან მომხარებელს შემოაქვს სახელი, გვარი, და ანგარიშის ნომერი
# 2. ანგარიში ნომერი შეიცავს ხუთ სიმბოლოს, რომლის პირველი ორი სიმბოლოც არის TB და დანარჩენი არის რიცხვები ( მაგ: TB001 ) გთხოვთ
# შემოტანის დროს შეამოწმოთ ამ ფორმატზე
# 3. თუ ყველაფერი წარმატებით გააკეთა დაარეგისტრირეთ იუზერი და დაუბეჭდეთ კონსოლში "თქვენ გაიარეთ რეგისტრაცია წარმატებით"
def is_valid_bank_number(bank_number):
    if len(bank_number) != 5 or bank_number[:2] != "TB" or not bank_number[2:].isdigit():
        print("Invalid bank number")
        return False
    return True

def check_in_db(database, bank_no):
    for record in database:
        if record["bank_no"] == bank_no:
            return True
    print("Invalid bank number!")
    return False

def check_in_db_register(database, bank_no):
    for record in database:
        if record["bank_no"] == bank_no:
            print("Such bank number exists!")
            return True
    return False

def register_customer(database):
    name = input("Input your name: ")
    surname = input("Input your surname: ")
    bank_number = input("Input you bank number: ")
    while not is_valid_bank_number(bank_number) or check_in_db_register(database, bank_number):
        bank_number = input("Input you bank number: ")
    record = {
        "name": name,
        "surname": surname,
        "bank_no": bank_number,
        "balance": 0,
    }
    database.append(record)
    print("თქვენ გაიარეთ რეგისტრაცია წარმატებით")
# დავალება #2#2
# დავამატოთ ბალანსის შევსების ფუნქციონალი:
# მომხარებელს შემოაქვს ანგარიშის ნომერი ( აქაც უნდა იყოს გათვალისწინებული ვალიდაცია), შემდეგ შემოაქვს თანხის რაოდენობა, რაც უნდა
# რომ ბალანსზე შეიტანოს, თუ თანხა არის რიცხვი, მაშინ ვუსვავთ თანხას ბალანსზე და ვუბეჭდავთ "ბალანსი შეივსო {თანხა} ლარით"
def fill_balance(database):
    bank_number = input("Input your bank number to fill the balance: ")
    while not is_valid_bank_number(bank_number) or not check_in_db(database, bank_number):
        bank_number = input("Input your bank number to fill the balance: ")
    amount = input("Input the amount of money you want to fill your balance with: ")
    if amount.isdigit():
        for record in database:
            if record["bank_no"] == bank_number:
                # record["balance"] = record["balance"] + int(amount)
                record["balance"] += int(amount)
                print(f"ბალანსი შეივსო {amount} ლარით")
                return
# დავალება #3#3
# დავამატოთ გადარიცხვის ფუნქციონალი:
# 1. მომხარებელს შემოაქვს ანგარიშის ნომერი ( ვალიდაცია) სადაც უნდა, რომ გადარიცხოს (მაგ: TB021) ვამოწმებთ თუ არსებობს მოცემული ანგარიში
# ( თუ არ არსებობს დავუბეჭდოთ "ანგარიშის ნომერი არ არსებობს" და მივცეთ ახლიდან შემოტანის საშუალება )
# 2. შემოიტანოს თანხა ( რის გადარიხცვაც უნდა მაგ: 10 )
# 3. გადავამოწმოთ თუ მომხმარებელს ბალანსზე აქვს საკმარისი თანხა, მაშინ ჩამოვაჭრათ ბალანსიდან და დავუსვათ მითითებულ მომხარებელს მაგ: (
# TB001 ვაჭრით 10 ლარს და გადაქვაქვს TB021 ის ბალანსზე) თუ ყველა ოპერაცია წარმატებით გაიარა დაუბეჭდეთ "თქვენს წარმატებით
# გადაურიცხეთ თანხა {სახელი, გვარი} -ს
def check_amount_in_db(database, bank_no, amount_to_transfer):
    for record in database:
        if record["bank_no"] == bank_no:
            if record["balance"] < amount_to_transfer:
                print("Not enough money on account to transfer")
                return False
    return True

def check_amount(amount):
    if amount <= 0:
        return False
    else:
        return True

def transfer(database):
    bank_number_from = input("Input your bank number from where you want to transfer: ")
    bank_number_to = input("Input your bank number to where you want to transfer to: ")
    while not is_valid_bank_number(bank_number_from) or not is_valid_bank_number(bank_number_to) or not check_in_db(database, bank_number_from) or not check_in_db(database, bank_number_to):
        bank_number_from = input("Input your bank number from where you want to transfer: ")
        bank_number_to = input("Input your bank number to where you want to transfer to: ")
    amount = int(input("Write how much money you want to transfer: "))
    while not check_amount(amount) or not check_amount_in_db(database, bank_number_from, amount):
        amount = int(input("Write how much money you want to transfer: "))
    for record in database:
        if record["bank_no"] == bank_number_to:
            name = record["name"]
            surname = record["surname"]
            record["balance"] += amount
        if record["bank_no"] == bank_number_from:
            record["balance"] -= amount
    print(f"თქვენს წარმატებით გადაურიცხეთ თანხა {name} {surname}")

want_to_continue = True
database = []
while want_to_continue:
    want_to_register_customer = input("Register customer? ")
    if want_to_register_customer == "Y":
        register_customer(database)
    want_to_fill_balance = input("Fill balance? ")
    if want_to_fill_balance == "Y":
        fill_balance(database)
    want_to_transfer = input("Transfer? ")
    if want_to_transfer == "Y":
        transfer(database)
    print(database)
    want_to_continue = input("Continue? ")
    if want_to_continue == "Y":
        want_to_continue = True
    else:
        exit()

