'''
სესხის გამომთვლელი:
ანგარიშის შექმნის დროს ანგარიიშ მიანიჭეთ ფიქსირებული სესხის პროცენტი (მაგ: 8.2%), 
მომხარებელს უნდა შეეძლოს შემოიტანის სესხის თანხა თქვენ დაუთვალეთ წლიური საპროცენტო განაკვეთით 
გადასახდელი თანხა და დაუბეჭდეთ, შემდეგ კითხეთ თუ უნდა აღება, შემდეგ დაუსვით ბალანსზე.
'''

import csv
import client_main as main



def loanCalc():
    iban = input("Your IBAN: ")
    amount = int(input("How much: "))
    duration = int(input("Loan duration in months: "))
    for user in main.database:
        if user["bank_no"] == iban:
            interest_rate = user["percent"]
            total_interest = amount * interest_rate * (duration / 12)
            total_amount = amount + total_interest
            monthly_payment = total_amount / duration
            print(f"Yearly interest on your amount will be: {total_interest}")
            print(f"You'll have to pay a total of: {total_amount}")
            print(f"Your monthly payment will be: {monthly_payment}")
            ans = input("Do you want to proceed? (Y/N): ").lower()
            if ans == "y":
                user["balance"] += amount
                for_loan_csv(user["name"], iban, duration, monthly_payment)
            else:
                print("Loan not proceeded")
            return
    print("IBAN not found in the database.")

def for_loan_csv(name, iban, duration, monthly_payment):
    headers = ["Name     ", "IBAN     ", "Month    ", "Monthly Payment    "]
    try:
        with open("loan.csv", "a", newline='') as file:
            writer = csv.writer(file)
            if file.tell() == 0:
                writer.writerow(headers)
            for month in range(1, duration + 1):
                writer.writerow([f"{name}   ", f"{iban}   " ,  f"{month}   ",  f"{monthly_payment}   "])
        print(f"Loan payments logged successfully for {name} with IBAN {iban}")
    except Exception as e:
        print(f"An error occurred while logging loan payments: {e}")
