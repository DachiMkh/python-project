import library as l


def topup_balance(iban, balance):
    for user in l.users:
        if user.get("iban") == iban:
            user["balance"] += balance