import random 

def iban_creator():
    iban_number=""
    for i in range(4):
       number = random.randint(0,9)
       number = str(number)
       iban_number=iban_number+number
    iban_number="TB"+iban_number
    return iban_number 


def percent_creator():
    percent=(random.randint(5,20))/100
    return percent

