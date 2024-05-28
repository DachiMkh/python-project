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

def user_id_creator():
    user_id=random.randint(1,10000)
    return user_id

def user_log (var1, var2, var3, var4):
    user_details = (f"{var1}, {var2}, {var3}, {var4} \n")
    with open("user.csv", "a") as file:
        file.write(user_details)

