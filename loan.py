'''
სესხის გამომთვლელი:
ანგარიშის შექმნის დროს ანგარიიშ მიანიჭეთ ფიქსირებული სესხის პროცენტი (მაგ: 8.2%), 
მომხარებელს უნდა შეეძლოს შემოიტანის სესხის თანხა თქვენ დაუთვალეთ წლიური საპროცენტო განაკვეთით 
გადასახდელი თანხა და დაუბეჭდეთ, შემდეგ კითხეთ თუ უნდა აღება, შემდეგ დაუსვით ბალანსზე.
'''

import client_main as main


def loanCalc():
    iban = input("you iban: ")
    amount = int(input("how much: "))
    amount2 = amount
    for user in main.database:
        if user["bank_no"] == iban:
            interest = int(amount * user["percent"])
            print("Yearly interest on your amount will be:", interest)
            print("You'll have to pay a total of", amount + interest)
            ans = input("Do you want to proceed? (Y/N): ").lower()
            if ans == "y":
                user["balance"] += amount2
            else:
                return 
