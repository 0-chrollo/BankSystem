

class Account:

    print("\n   @.[BANKING SYSTEM].@\n")
    create = input("\n  enter-[CREATE ACCOUNT]:- ")
    print("[************************]\n")
    details = []

    def __init__(self, name, surname, email,age, pin, balance=0):
        self.name = name
        self.surname = surname
        self.email = email
        self.age = age
        self.pin = pin
        self.balance = balance
        Account.details.append(self)

    def Deposit(self):
        self.deposit = int(input("\nDeposit an Amount: "))
        self.balance += self.deposit
        print("Deposited: " + str(self.deposit))

    def Withdrawal(self):
        self.amount = int(input("Withdraw an Amount: "))
        self.balance -= self.amount
        print("Withdrawn: " + str(self.amount))

    def Balance(self):
        print("\n[Available Balance: " + str(self.balance) + "]")

    def Created(self):
        print("\n[Account Succesfully Created!!]")
        for each_detail in Account.details:
            print("Name: " + each_detail.name, ",Surname: " +
                  each_detail.surname,
                  ",Age: " + str(each_detail.age),
                  ",Email: " + str(
                  each_detail.email),
                  )









