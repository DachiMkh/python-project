'''
სესხის გამომთვლელი:
ანგარიშის შექმნის დროს ანგარიიშ მიანიჭეთ ფიქსირებული სესხის პროცენტი (მაგ: 8.2%), 
მომხარებელს უნდა შეეძლოს შემოიტანის სესხის თანხა თქვენ დაუთვალეთ წლიური საპროცენტო განაკვეთით 
გადასახდელი თანხა და დაუბეჭდეთ, შემდეგ კითხეთ თუ უნდა აღება, შემდეგ დაუსვით ბალანსზე.
'''

import client_main as main


def loanCalc(iban, amount):
    for user in main.database:
        if user.get("bank_no") == iban:
            interest = amount * user["percentage"]
            print("Yearly interest on your amount will be:", interest)
            print("You'll have to pay a total of", amount + interest)
            ans = input("Do you want to proceed? (Y/N): ").lower
            if ans == "y":
                user["balance"] += amount