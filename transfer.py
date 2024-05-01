# მომხმარებლებს შეუძლიათ ფულის გადარიცხვა ორ ანგარიშს შორის, გადარიცხვამდე უნდა 
# შემოწმდეს ანგარიშების ვალიდურობა და გადამცემის საკმარისი ბალანსი.

from client_validator import check_client_info
import client_main

def money_transfer(giver, getter, amount):
    giver = check_client_info(giver)
    getter = check_client_info(getter)
    if giver and getter:
        if giver.get("balance") >= amount:
            print("Proccessing....")
            giver['balance'] -= amount
            getter['balance'] += amount
            client_main.record.append({"bank_no": giver, "bank_no": getter, "balance": amount})
    else:
        print("Does not exist")