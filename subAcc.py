import Bank
from Bank import Account


class Profile:

    def __init__(self, username,sub_amount,bankaccount:Bank.Account):
        self.bankaccount = bankaccount
        self.username = username
        self.sub_amount = sub_amount

    def stored_amount(self):
        print("\n[Stored: " + str(self.sub_amount) + "] in Sub Account.")







