
# 1. Build a new class called `BankAccount`...
class BankAccount:
    def __init__(self, userName, balance, status, account, deposit, check_balance, is_valid):
        self.userName = userName
        self.balance = balance
        self.status = status
        self.account = account
        self.deposit = deposit
        self.check_balance = check_balance
        self.is_valid = is_valid
    # def valid(self):
    #     self.valid = is_valid
        if self.status == "open":
            print("Your account is good")
            print(account)
        elif self.status == "0" or "closed":
            print("You have a bad record")
            
            
#  ... and instantiate a new account for a user named "Kiran".
kiran_account = BankAccount("Kiran", 1000, "closed", "BankAccount", 500, 1500, True)

# i. Confirm that Kiran's new account is of the type `BankAccount`.
print(type(kiran_account))

# ii. Confirm that the name on Kiran's account is "Kiran".
print(kiran_account.userName)

# iii. Confirm that Kiran's account has a balance of $1000.
print(kiran_account.balance)

# iv. Confirm that Kiran's account is `open`.
print(kiran_account.status)

# v. Set Kiran's balance to $2000. Confirm his new account balance.
kiran_account.balance = 2000
print(kiran_account.balance)

# Now you're on your own to write tests for the rest...
print(kiran_account.status)

# class Transfer:
#     pass # delete this line when you're ready to build the Transfer class

