import loan
import history as hs
import transfer
import client_main as cl
import balance



actions = {
    "register": cl.register_customer,
    "bank_details": cl.bank_no_details,
    "balance": balance.topup_balance,
    "history": hs.transfer_history,
    "transfer": transfer.money_transfer,
    "loan": loan.loanCalc
}

while True:
    input_actions = input(f"Please enter action {actions.keys()}: ")
    if input_actions in actions:
        actions[input_actions]()
    else:
        print("Invalid action. Please try again.")
