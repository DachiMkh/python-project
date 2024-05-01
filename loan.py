'''
ანგარიშის შექმნის დროს ანგარიიშ მიანიჭეთ ფიქსირებული სესხის პროცენტი (მაგ: 8.2%), 
მომხარებელს უნდა შეეძლოს შემოიტანის სესხის თანხა თქვენ დაუთვალეთ წლიური საპროცენტო 
განაკვეთით გადასახდელი თანხა და დაუბეჭდეთ, შემდეგ კითხეთ თუ უნდა აღება, შემდეგ დაუსვით ბალანსზე.
'''
import ***

def loanCalc(amount):
    interest = amount * user["percentage"]
    print("Yearly interest on your amount will be:", interest)
    ans = input("Do you want to proceed? (Y/N): ").lower
    if ans == "y":
        user["balance"] += amount