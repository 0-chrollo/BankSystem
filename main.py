import subAcc
from Bank import Account
from subAcc import Profile
import json
from storage import DataStorage

All_acc=[]

with open("C:\\Users\\lucas\Desktop\\Files\\ALL_ACCOUNTS.json", "r") as file:
    for acc in file:
        accD = json.loads(acc)
        All_acc.append(accD)
print("[SAVED ACCOUNTS]")
for account in All_acc:
    print(account)

name = input("\nEnter your name: ")
surname = input("Enter your surname: ")
email = input("Enter your Email: ")
age = int(input("Enter age: "))
if int(age) <= 16:
    print("Age not accepted!!")
pin = int(input("\n[Enter Pin: ]\n"))

main_account = Account(name, surname, email,age, pin, 0)
main_account.Created()
main_account.Deposit()
main_account.Withdrawal()
main_account.Balance()

subAcc.Profile.create = str(input("\nCreate Sub Account? "))
if subAcc.Profile.create == ["yes","Yes","y","Y"]:
    print("\nInitialising.....\n")
elif subAcc.Profile.create == ["no", "No", "n", "N"]:
    print("--------------------")

username = input("\nEnter a Username: ")
sub_amount = input("Enter an amount for Sub Account: ")
sub_account = Profile(username,sub_amount,main_account)

sub_account.stored_amount()

storage = DataStorage("C:\\Users\\lucas\Desktop\\Files\\ALL_ACCOUNTS.json")
ALL_ACCOUNTS = {"Name": main_account.name,
                "Surname": main_account.surname,
                "Email": main_account.email,
                "Age": main_account.age,
                "Deposited": main_account.deposit,
                }

storage.SaveData(ALL_ACCOUNTS)
loaded_data = storage.LoadData()
print(loaded_data)
file_exists = storage.hasFile()
print(file_exists)

print("\n***************************\n")

