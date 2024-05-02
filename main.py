import loan
import history as hs 
import transfer 
import client_main as cl
import balance 



actions = {
    "register_customer" : cl.register_customer,
    "bank_no_details" : cl.bank_no_details,
    "balance" : balance.topup_balance,
    "history" : hs.transfer_history,
    "transfer" : transfer.money_transfer,
    "loan" : loan.loanCalc
}

input_actions=input(f"Please enter action {actions.keys()}: ")

while input_actions in actions.keys():
    actions[input_actions]()
    input_actions=input(f"Please enter action {actions.keys()}: ")